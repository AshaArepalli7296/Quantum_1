import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Login from '../pages/Login.vue'
import CreditFraud from '../pages/frauds/CreditFraud.vue'
const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/frauds/credit', name: 'CreditFraud', component: CreditFraud },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router