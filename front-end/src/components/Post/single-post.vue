<template>
  <div class="main">
    <el-card class="info" shadow="never">
      {{ props.postInfo }}
    </el-card>
    <div class="button">
      <el-button type="primary" @click="submit">提交</el-button>
    </div>

    <div class="comments">
      <div v-for="count in index" :key="count">
        <el-card shadow="never" style="width: 90%;margin: 0 auto">
          <div class="comment">
            <div>
              <span style="color:#dc7a59">{{ comments[count]?.username }}:</span>
              <span>{{ comments[count]?.comment }}</span>
            </div>
            <div style="display: flex;justify-content: flex-end">
              <stars v-model:rating="rating[count]"></stars>
            </div>
          </div>
        </el-card>
      </div>

    </div>
  </div>
</template>

<script setup>
import SingleComment from "@/components/Post/single-comment.vue";
import { onMounted, reactive, ref, watch,toRaw } from "vue";
import stars from '../Stars/stars.vue'

const dialogVisible = ref(false)
const props = defineProps({
  postInfo: {
    type: String,
    default: ''
  },
  comments: {
    type: Array,
    default: []
  }
})
const comments = ref([])
watch(props,(newVal,oldVal)=>{
  comments.value = newVal.comments
  let len = comments.value.length
  for(let i = 0;i < len;i++){
    index.value.push(i)
    rating.value.push(0)
  }
})
const index = ref([])
const rating = ref([])
onMounted(()=>{
  
})


const submit = () => {
  let feedbacks = []
  for(let i = 0;i < 6;i++){
    feedbacks.push({
      pairsID:comments.value[i]?.pairsID,
      result:rating.value[i],
      feedback:""
    })
  }
  console.log(feedbacks)
}
</script>

<style scoped>
.main {
  width: 100%;
  margin: auto;
}

.info {
  border-radius: 12px;
  text-align: left;
}

.button {
  margin: 10px auto;
}

::v-deep .el-radio {
  display: block;
  margin: 10px 0;
}

.comment{
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content:space-between;
  width: 100%;
}
</style>