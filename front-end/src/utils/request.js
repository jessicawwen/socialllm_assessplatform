import axios from 'axios'

const request = axios.create({
    baseURL: '/api',  // 注意！！ 这里是全局统一加上了 '/api' 前缀，也就是说所有接口都会加上'/api'前缀在，页面里面写接口的时候就不要加 '/api'了，否则会出现2个'/api'，类似 '/api/api/user'这样的报错，切记！！！
    timeout: 5000
})

request.interceptors.request.use(config => {
    let token = sessionStorage.getItem("token")
    if (!token) {
        config.headers['Authorization'] = '';  // 设置请求头
    }
    else {
        config.headers['Authorization'] = 'Bearer'+' '+token
    }
    config.headers['Content-Type'] = 'application/json;charset=utf-8';
    //config.headers['Content-Type'] = 'multipart/form-data'
    return config
}, error => {
    return Promise.reject(error)
});
request.interceptors.response.use(
    response => {
        let res = response;
        // 如果是返回的文件
        if (response.config.responseType === 'blob') {
            return res
        }
        // 兼容服务端返回的字符串数据
        if (typeof res === 'string') {
            res = res ? JSON.parse(res) : res
        }
        return res;
    },
    error => {
        console.log('err' + error) // for debug
        return Promise.reject(error)
    }
)


export default request
