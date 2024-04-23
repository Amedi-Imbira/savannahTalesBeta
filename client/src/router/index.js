import { createRouter, createWebHistory } from 'vue-router'
import LandingPageView from '@/views/LandingPageView.vue'
import MissionPageView from '@/views/MissionPageView.vue'
import LoginPageView from '@/views/LoginPageView.vue'
import SignupPageView from '@/views/SignupPageView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: LandingPageView, name: 'LandingPageView'},
    {path: '/about', component: MissionPageView, name: 'MissionPageView'},
    {path: '/signup', component: SignupPageView, name: SignupPageView},
    {path: '/login', component: LoginPageView, name: LoginPageView},

    // {
    //   path: '/',
    //   name: 'home',
    //   component: HomeView
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
