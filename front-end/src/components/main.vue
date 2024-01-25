<template>
  <el-button @click="beginAssess">开始评测</el-button>
</template>

<script setup>
import router from "@/router";
import request from "@/utils/request";
import {onMounted} from "vue";
const beginAssess = () => {
  router.push('/main')
}
onMounted(()=>{
  request.get('').then((json)=>{
    console.log(json)
  })
})
</script>


<style scoped>

</style>