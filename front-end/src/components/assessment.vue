<template>
  <div style="margin: 0 0 30px 0">
    <el-card shadow="never">
      <div style="display:flex;flex-direction: row;align-items: center;justify-content: space-between">
        <div style="text-align: left;">
          <img src="https://s1.aigei.com/src/img/png/1e/1ee2c1c23f4647a790ea7f8f22d0c2a3.png?imageMogr2/auto-orient/thumbnail/!282x282r/gravity/Center/crop/282x282/quality/85/%7CimageView2/2/w/282&e=1735488000&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:_CCFjFtKQrRXW9_2Buq4Ge-O6W4=" alt="" height="40" >
        </div>
        <div style="text-align: center">
          <el-button @click="prevPost">
            上一条
          </el-button>
          当前第{{postCount}}条，共{{totalPost}}条
          <el-button @click="nextPost">
            下一条
          </el-button>
        </div>
        <div></div>
      </div>
    </el-card>
  </div>

  <div class="content">
    <div style="width: 10%;margin:0 20px 0 0">
      <el-card style="height: 600px" shadow="never">

      </el-card>
    </div>
    <div style="width: 50%">
      <single-post :post-info="postArray[postCount - 1]" :comments="postComments"></single-post>
    </div>
    <div style="width:15%;margin:0 0 0 20px">
      <el-card style="height: 400px;" shadow="never">

      </el-card>
      <el-card style="height: 300px;margin-top:20px" shadow="never">

      </el-card>
    </div>
  </div>
</template>

<script setup>
import router from "@/router";
import {onMounted, ref} from "vue";
import {ElMessage} from "element-plus";
import SinglePost from "@/components/Post/single-post.vue";
import request from "@/utils/request";

const postCount = ref(1)
const totalPost = ref(100)
const canGetNext = ref(false)
const prevPost = () => {
  if(postCount.value > 1){
    postCount.value--
  }else{
    ElMessage.warning('已经是第一条了')
  }
}
const nextPost = () => {
  if(canGetNext.value === false){
    ElMessage.warning('您还没发布评论和点赞哦')
  }else if(postCount.value < totalPost.value){
    postCount.value++
  }
}

const postArray = ref([])
const postComments = ref([])
onMounted(()=>{
  postArray.value.push('朋友给我转的这个，真的笑晕[允悲]南京有个活请了盒马山姆，结果两家的摊位直接面对面......\n' +
      '山姆:为什么多是大包装?为会员带来更多节省\n' +
      '盒马:为什么多是小包装? 不需门票，小家庭单身族也无压力。\n' +
      '这就是商战吗[笑cry][笑cry][笑cry]盒马山姆不如直接打起来吧，这当面锣对面鼓的哈哈哈人少，还是小包装的合适点......吃不完罪恶感好强 #盒马大包装vs小包装，会员vs全员，你怎么选?我家山姆贴脸商战引围观##大包装小包装怎么选#')
  postArray.value.push('222')
  postComments.value.push({
    username:'w_w',
    content:'盒马山姆的会员卡我都办了，谁让我家是全家桶爱好者'
  })
  postComments.value.push({
    username:'glm',
    content:'哈哈，这个笑话挺有趣的！这种对话式的描绘确实能展现出盒马和山姆的差异，也调侃了现实生活中商业竞争的一些特点。盒马和山姆代表的不同商业模式在对比中展现了会员制和全员服务之间的差异，而以幽默的方式呈现也更容易引发共鸣。\n' +
            '\n' +
        '在商业竞争中，确实有时候公司会使用幽默来吸引消费者，而这样的对话也是很好的营销方式。至于大包装和小包装的选择，这取决于消费者的需求和偏好，不同的人可能会有不同的选择。笑话的最后一句话也是挺有趣的，似乎在调侃着如果两家直接对打，会是个有趣的场面，虽然商业战争应该是以竞争为主而非真正的打斗哈哈。'
  })
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