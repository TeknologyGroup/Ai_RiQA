import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import store from './store'
import './assets/tailwind.css'

// Componenti
import HomePage from './views/HomePage.vue'
import SimulationPage from './views/SimulationPage.vue'
import QuantumPage from './views/QuantumPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomePage },
    { path: '/simulate', component: SimulationPage },
    { path: '/quantum', component: QuantumPage }
  ]
})

const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
