<template>
  <div class="simulation-controls">
    <h2>Simulazioni Avanzate</h2>
    
    <div class="control-group">
      <label>Tipo di Simulazione:</label>
      <select v-model="params.type">
        <option value="math">Matematica</option>
        <option value="ballistic">Balistica</option>
        <option value="quantum_entanglement">Entanglement Quantistico</option>
        <option value="chaotic">Sistemi Caotici</option>
      </select>
    </div>
    
    <div v-if="params.type === 'math'" class="params-group">
      <h3>Parametri Matematici:</h3>
      <!-- Aggiungi parametri specifici -->
    </div>
    
    <div v-if="params.type === 'ballistic'" class="params-group">
      <h3>Parametri Balistici:</h3>
      <!-- Aggiungi parametri specifici -->
    </div>
    
    <button @click="runSimulation" class="run-btn">
      Avvia Simulazione
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      params: {
        type: 'math',
        // Altri parametri specifici per tipo
      }
    }
  },
  methods: {
    runSimulation() {
      this.$emit('run', this.params);
    }
  }
}
</script>

<style scoped>
.simulation-controls {
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.control-group {
  margin-bottom: 1rem;
}

.control-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.control-group select {
  padding: 0.5rem;
  width: 100%;
}

.params-group {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 4px;
}

.run-btn {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
