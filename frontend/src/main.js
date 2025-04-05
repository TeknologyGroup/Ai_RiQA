import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import { createPinia } from 'pinia';
import App from './App.vue';
import './assets/tailwind.css';

// Importa i componenti
import HomePage from './views/HomePage.vue';
import SimulationPage from './views/SimulationPage.vue';
import QuantumPage from './views/QuantumPage.vue';
import VisualizationPage from './views/VisualizationPage.vue';
import AnalysisPage from './views/AnalysisPage.vue';
import LoginPage from './views/LoginPage.vue';
import RegisterPage from './views/RegisterPage.vue';

// Configurazione del router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomePage },
    { path: '/simulate', component: SimulationPage, meta: { requiresAuth: true } },
    { path: '/quantum', component: QuantumPage, meta: { requiresAuth: true } },
    { path: '/visualize', component: VisualizationPage, meta: { requiresAuth: true } },
    { path: '/analyze', component: AnalysisPage, meta: { requiresAuth: true } },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage }
  ]
});

// Middleware di autenticazione
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('access_token');
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

// Crea l'app Vue
const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(pinia);
app.mount('#app');
