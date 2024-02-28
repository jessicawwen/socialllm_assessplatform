<template>
  <div class="login-container">
    <header class="login-header">SocialGLM Assessment</header>

    <el-card class="login-card">
      <el-form ref="loginForm" class="login-form">
        <el-form-item label="账号">
          <el-input v-model="username" placeholder="请输入账号"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item style="text-align: center;">
          <el-button type="primary" @click="handleLogin">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import router from '@/router';
import request from '@/utils/request';
import { ref } from 'vue';
const username = ref('')
const password = ref('')
const handleLogin = () => {
  let data = {
    username:username.value,
    password:password.value
  }
  request.post('/login',data).then(res=>{
    if(res.status===200){
      sessionStorage.setItem('token',res.data.access_token)
      router.push('/main')
    }
  })
}
</script>

<style scoped>
.el-button{
  display: block;
  margin:0 auto;
}
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.login-header {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.login-card {
  width: 500px;
}

.login-form {
  margin: 20px;
}
</style>
