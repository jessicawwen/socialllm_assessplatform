<template>
  <div class="main">
    <el-card class="info" shadow="never">
      {{props.postInfo}}
    </el-card>
    <div class="button">
      <el-button type="primary" @click="generateComments">生成评论</el-button>
    </div>
    <div class="comments">
      <div v-for="item in props.comments" :key="item.content">
        <single-comment :comment="item"></single-comment>
      </div>
    </div>
  </div>
</template>

<script setup>
import SingleComment from "@/components/Post/single-comment.vue";
import {ref} from "vue";

const dialogVisible = ref(false)
const generateComments = () => {
  dialogVisible.value = true
}
const props = defineProps({
  postInfo:{
    type:String,
    default:''
  },
  comments:{
    type:Array,
    default:[]
  }
})
const selectedComment = ref(1)
</script>

<style scoped>
.main{
  width: 100%;
  margin: auto;
}
.info{
  border-radius: 12px;
  text-align: left;
}
.button{
  margin:10px auto;
}
::v-deep .el-radio{
  display: block;
  margin:10px 0;
}

/* /deep/ .el-radio__label{
  white-space: normal;
}

/deep/ .el-checkbox__label{
  white-space: normal;
}*/

</style>