import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import assessment from "@/components/assessment.vue";
import main from '@/components/main.vue'
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
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});


export default router