<template>
  <el-card shadow="never" style="width: 90%;margin: 0 auto">
    <div class="main">
      <div>
        <span style="color:#dc7a59">{{props.comment.username}}:</span>
        <span>{{props.comment.content}}</span>
      </div>
      <div style="display: flex;justify-content: flex-end">
        <el-button>点赞</el-button>
      </div>
    </div>
  </el-card>
</template>

<script setup>
const props = defineProps({
  comment:{
    type:Object,
    default:{}
  }
})
</script>

<style scoped>
.main{
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content:space-between;
  width: 100%;
}
</style>