<template>
  <el-button @click="beginAssess">开始评测</el-button>
  <stars v-model:rating="val1"></stars>
</template>

<script setup>
import router from "@/router";
import request from "@/utils/request";
import {onMounted, watch} from "vue";
import stars from ".//Stars/stars.vue"
import {ref} from "vue";
const beginAssess = () => {
  router.push('/main')
}
const val1 = ref(0)
watch(val1,(newVal,oldVal)=>{
  console.log(newVal)
})
onMounted(()=>{
  
})
</script>


<style scoped>

</style>