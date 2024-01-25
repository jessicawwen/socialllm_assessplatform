from databases import Database
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from databases import Database

# 初始化FastAPI应用
app = FastAPI()

# 数据库配置
DATABASE_URL = "mysql://root:ww010702@localhost/platform"

# 创建数据库实例
database = Database(DATABASE_URL)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)


# 数据模型
class User(BaseModel):
    username: str
    password: str

class Pair(BaseModel):
    post: str
    comment: str

class Feedback(BaseModel):
    pairsID: int
    userID: int
    result: str
    feedback: str

# 启动和关闭数据库连接
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# 用户登录
@app.post("/login")
async def login(user: User):
    query = "SELECT * FROM Users WHERE username = :username"
    db_user = await database.fetch_one(query, {"username": user.username})
    if db_user is None or db_user['password'] != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return {"message": "User logged in successfully"}

# 获取Pairs表中的数据
@app.get("/main")
async def read_pairs():
    query = "SELECT post, comment FROM Pairs"
    return await database.fetch_all(query)

# 接收前端的feedback并插入数据库
@app.post("/feedback")
async def receive_feedback(feedback: Feedback):
    query = "INSERT INTO Remarks(pairsID, userID, result, feedback) VALUES(:pairsID, :userID, :result, :feedback)"
    values = {**feedback.dict()}
    await database.execute(query, values)
    return {"message": "Feedback received successfully"}
