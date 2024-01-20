<template>
  <el-button @click="beginAssess">开始评测</el-button>
</template>

<script setup>
import router from "@/router";

const beginAssess = () => {
  router.push('/main')
}
</script>


<style scoped>

</style>