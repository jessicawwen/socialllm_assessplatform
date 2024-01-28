from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import string
from datetime import datetime, timedelta
import jwt
from databases import Database
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# 其余代码保持不变

# JWT密钥和算法
SECRET_KEY = "ASSESSMENT"  # 应该使用随机生成的安全密钥
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300

# 创建token的函数
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 验证token的函数
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return payload
    except Exception:
        raise credentials_exception


def generate_random_username(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

# 数据库配置
DATABASE_URL = "mysql://root:ww010702@localhost/platform"

# 创建数据库实例
database = Database(DATABASE_URL)

# 数据模型
class User(BaseModel):
    username: str
    password: str

from typing import List

class FeedbackItem(BaseModel):
    pairsID: int
    result: str
    feedback: str

class FeedbackList(BaseModel):
    feedbacks: List[FeedbackItem]

# 启动和关闭数据库连接
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)


@app.get("/")
def read_root():
    return {"Hello": "World"}

# 用户登录
@app.post("/login")
async def login(user: User):
    query = "SELECT * FROM Users WHERE username = :username"
    db_user = await database.fetch_one(query, {"username": user.username})
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    # 创建token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user["username"],"user_id": db_user["userID"]}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


# 获取Pairs表中的数据
@app.get("/main/{post_id}")
async def read_pairs(post_id: int):  
    query = "SELECT pa.pairsID, po.post, pa.comment,pa.source FROM Pairs pa LEFT JOIN Posts po ON pa.postID = po.postID WHERE pa.postID = :post_id"
    pairs =  await database.fetch_all(query, {"post_id": post_id})
    result = [
        {
            "pairsID": pair["pairsID"],
            "username": generate_random_username(),
            "post": pair["post"],
            "comment": pair["comment"],
            "source": pair["source"]
        }
        for pair in pairs
    ]
    return result


# 接收前端的feedback并插入数据库
@app.post("/main/{post_id}")
async def receive_feedback(post_id: int, feedback_list: FeedbackList, current_user: User = Depends(get_current_user)):
    user_id = current_user["user_id"]

    for feedback in feedback_list.feedbacks:
        query = "INSERT INTO Remarks(pairsID, userID, result, feedback) VALUES(:pairsID, :userID, :result, :feedback)"
        values = {
            "pairsID": feedback.pairsID,
            "userID": user_id,
            "result": feedback.result,
            "feedback": feedback.feedback
        }
        await database.execute(query, values)

    return {"message": "Feedback received successfully"}
