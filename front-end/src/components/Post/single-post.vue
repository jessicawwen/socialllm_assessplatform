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

    <el-dialog
        title="生成评论"
        v-model="dialogVisible"
        width="50%">
      <div style="margin: 0 auto">
        <el-radio-group style="display: table" v-model="selectedComment">
          <div style="text-align: left;overflow-wrap: break-word">
            <el-radio :label="1">感觉山姆的甜品比较健康</el-radio>
          </div>
          <div style="text-align: left;display: flex">
            <el-radio :label="2">哈哈！这个笑话是相当搞笑的！</el-radio>
          </div>
          <div style="text-align: left;display: flex">
            <el-radio :label="3">这种幽默的描述方式让人捧腹不已，尤其是把两家企业摊位对峙比作是“当面锣对面鼓”，让人忍俊不禁。</el-radio>
          </div>
          <div style="text-align: left;display: flex">
            <el-radio :label="4">在下方填写您自己的评论</el-radio>
          </div>
        </el-radio-group>
        <div>
          <el-input
              type="textarea"
              :autosize="{ minRows: 3, maxRows: 4}"
              placeholder="请输入内容"
              v-model="textarea2">
          </el-input>
        </div>
      </div>
      <div slot="footer" class="dialog-footer" style="margin: 10px 0 0 0">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">发 布</el-button>
      </div>
    </el-dialog>
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