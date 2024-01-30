<template>
  <div style="margin: 0 0 30px 0">
    <el-card shadow="never">
      <div style="display:flex;flex-direction: row;align-items: center;justify-content:center">
        <div style="text-align: center">
          <el-button @click="prevPost">
            上一条
          </el-button>
          当前第{{currentPost}}条，共{{totalPost}}条
          <el-button @click="nextPost">
            下一条
          </el-button>
        </div>
      </div>
    </el-card>
  </div>

  <div class="content">
    <div style="width: 80%">
      <single-post :post-info="postContent" :comments="postComments"></single-post>
    </div>
  </div>
</template>

<script setup>
import router from "@/router";
import {onMounted, ref} from "vue";
import {ElMessage} from "element-plus";
import SinglePost from "@/components/Post/single-post.vue";
import request from "@/utils/request";

const currentPost = ref(1)
const totalPost = ref(100)
const canGetNext = ref(false)
const prevPost = () => {
  if(currentPost.value > 1){
    currentPost.value--
    getPost()
  }else{
    ElMessage.warning('已经是第一条了')
  }
}
const nextPost = () => {
  if(canGetNext.value === false){
    ElMessage.warning('您还没发布评论和点赞哦')
  }else if(currentPost.value < totalPost.value){
    currentPost.value++
    getPost()
  }
}

const postContent = ref("")
const postComments = ref([])
const getPost = () => {
  request.get(`main/${currentPost.value}`).then((json)=>{
    postComments.value = json.data;
    postContent.value = postComments.value[0].post
  })
}
onMounted(()=>{
  getPost()
})
</script>


<style scoped>
.content{
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
}
</style>