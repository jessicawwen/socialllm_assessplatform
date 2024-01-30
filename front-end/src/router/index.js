import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import assessment from "@/components/assessment.vue";
import main from '@/components/main.vue'
import stars from '@/components/Stars/stars.vue'
const routes = [
    {
        path: '/',
        name:'/',
        component: main
    },
    {
        path: '/main',
        name: 'main',
        component: assessment
    },
    {
        path:'/stars',
        name:'star',
        component:stars
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});


export default router