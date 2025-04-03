<template>
  <div class="simulation-panel">
    <h2>Scientific Simulation</h2>
    <form @submit.prevent="runSimulation">
      <div class="form-group">
        <label>Parameters:</label>
        <textarea v-model="parameters" rows="4"></textarea>
      </div>
      <button type="submit">Run Simulation</button>
    </form>
    <div v-if="loading" class="loading">Processing...</div>
    <div v-if="result" class="result">
      <h3>Results</h3>
      <pre>{{ result }}</pre>
    </div>
  </div>
</template>

<script>
import { runSimulation } from '@/services/api'

export default {
  data() {
    return {
      parameters: '',
      result: null,
      loading: false
    }
  },
  methods: {
    async runSimulation() {
      this.loading = true
      try {
        const response = await runSimulation({ 
          parameters: this.parameters 
        })
        this.result = response.data
      } catch (error) {
        console.error('Simulation error:', error)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
