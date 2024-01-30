<template>
  <el-card shadow="never" style="width: 90%;margin: 0 auto">
    <div class="main">
      <div>
        <span style="color:#dc7a59">{{props.comment.username}}:</span>
        <span>{{props.comment.comment}}</span>
      </div>
      <div style="display: flex;justify-content: flex-end">
        <stars v-model:rating="rating"></stars>
      </div>
    </div>
  </el-card>
</template>

<script setup>
import stars from '../Stars/stars.vue';
import { ref } from 'vue';
const props = defineProps({
  comment:{
    type:Object,
    default:{}
  }
})
const rating = ref(0)
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