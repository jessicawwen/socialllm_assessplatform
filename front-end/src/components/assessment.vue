<template>
  <div style="margin: 0 0 30px 0">
    <el-card shadow="never">
      <div style="display:flex;flex-direction: row;align-items: center;justify-content:center">
        <div style="text-align: center">
          <el-button @click="prevPost">
            上一条
          </el-button>
          当前第{{ currentPost }}条，共{{ totalPost }}条
          <el-button @click="nextPost">
            下一条
          </el-button>
        </div>
      </div>
    </el-card>
  </div>

  <div class="main">
    <el-card class="info" shadow="never">
      {{ postContent }}
    </el-card>
    <div class="button">
      <el-button type="primary" @click="submit">提交</el-button>
    </div>

    <div class="comments">
      <div v-for="(comment, index) in postComments" :key="index">
        <el-card shadow="never" style="width: 90%;margin: 0 auto">
          <div class="comment">
            <div>
              <span style="color:#dc7a59">{{ comment?.username }}:</span>
              <span>{{ comment.comment }}</span>
            </div>
            <div style="display: flex;justify-content: flex-end">
              <stars v-model:rating="rating[index]"></stars>
            </div>
          </div>
        </el-card>
      </div>

    </div>
  </div>

  <div>
    <el-dialog v-model="dialogvisible" width="50%">
      <h2>请问您不喜欢这条评论的原因是什么？</h2>
      <el-card style="margin: 20px auto;">
        {{ feedbackComment }}
      </el-card>
      <el-input type="textarea" v-model="feedbackContent"></el-input>
      <el-button type="primary" @click="feedbackSubmit" style="margin: 20px auto;">提交</el-button>
    </el-dialog>
  </div>
</template>

<script setup>
import router from "@/router";
import { onMounted, ref } from "vue";
import { ElMessage } from "element-plus";
import SinglePost from "@/components/Post/single-post.vue";
import request from "@/utils/request";
import stars from "./Stars/stars.vue";
const currentPost = ref(1)
const totalPost = ref(100)
const canGetNext = ref(false)
const prevPost = () => {
  if (currentPost.value > 1) {
    currentPost.value--
    getPost()
  } else {
    ElMessage.warning('已经是第一条了')
  }
}
const nextPost = () => {
  if (currentPost.value < totalPost.value) {
    currentPost.value++
    getPost()
  }else{
    ElMessage.warning('已经是最后一条了')
  }
}

const postContent = ref("")
const postComments = ref([])
const getPost = () => {
  request.get(`main/${currentPost.value}`).then((json) => {
    postComments.value = json.data;
    postContent.value = postComments.value[0].post
    rating.value = new Array(postComments.value.length).fill(0)
  })
}
onMounted(() => {
  getPost()
})
const rating = ref([])
const dialogvisible = ref(false)
const feedbackContent = ref('')
const feedbackComment = ref('')
function hasZero(array) {
    return array.includes(0);
}
const submit = () => {
  if(hasZero(rating.value)){
    ElMessage.error('请给所有评价打分！')
  }else{
    let temp = postComments.value.findIndex(item => {
    return item.source === 'weibobot'
  })
  if (rating.value[temp] <= 2) {
    dialogvisible.value = true
    feedbackComment.value = postComments.value[temp].comment
  } else {
    let feedbacks = []
    let len = postComments.value.length
    for (let i = 0; i < len; i++) {
      feedbacks.push({
        pairsID: postComments.value[i].pairsID.toString(),
        result: rating.value[i].toString(),
        feedback: ''
      })
    }
    request.post(`main/${currentPost.value}`, {feedbacks:feedbacks}).then((res) => {
      if (res.status === 200) {
        ElMessage.success('提交成功！')
        nextPost()
      }
    })
  }
  }
}
const feedbackSubmit = () => {
  let feedbacks = []
  let len = postComments.value.length
  for (let i = 0; i < len; i++) {
    feedbacks.push({
      pairsID: postComments.value[i].pairsID.toString(),
      result: rating.value[i].toString(),
      feedback: ''
    })
  }
  let temp = postComments.value.findIndex(item => {
    return item.source === 'weibobot'
  })
  feedbacks[temp].feedback = feedbackContent.value
  request.post(`main/${currentPost.value}`, {feedbacks:feedbacks}).then((res) => {
    if (res.status === 200) {
      ElMessage.success('提交成功！')
      nextPost()
    }
  })
}
</script>


<style scoped>
.content {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
}

.main {
  width: 80%;
  margin: auto;
}

.info {
  border-radius: 12px;
  text-align: left;
  margin: 0 auto;
}

.button {
  margin: 10px auto;
}

::v-deep .el-radio {
  display: block;
  margin: 10px 0;
}

.comment {
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
}
</style>