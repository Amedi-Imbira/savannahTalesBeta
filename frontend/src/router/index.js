import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import MissionView from '../views/MissionView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {path: '/signup', component: SignupView, name: 'signup'},
    {path: '/mission', component: MissionView, name: 'mission'},
    {path: '/login', component: LoginView, name: 'login'},
  ]
})

export default router
