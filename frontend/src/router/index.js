import Vue from 'vue';
import VueRouter from 'vue-router';
import App from '../App.vue'; // Adjust path if needed

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: App
  }
  // Add more routes as needed
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
