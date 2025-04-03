import axios from 'axios'

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:5000/api'
})

export const runSimulation = (data) => api.post('/simulate', data)
export const runQuantumAnalysis = (data) => api.post('/quantum', data)
export const generateAIContent = (prompt) => api.post('/generate', { prompt })

export default api
