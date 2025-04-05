import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from '../views/HomePage.vue';
import AnalysisPage from '../views/AnalysisPage.vue';
import LoginPage from '../views/LoginPage.vue';
import QuantumPage from '../views/QuantumPage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import SimulationPage from '../views/SimulationPage.vue';
import VisualizationPage from '../views/VisualizationPage.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/analysis', name: 'Analysis', component: AnalysisPage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/quantum', name: 'Quantum', component: QuantumPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  { path: '/simulation', name: 'Simulation', component: SimulationPage },
  { path: '/visualization', name: 'Visualization', component: VisualizationPage }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
