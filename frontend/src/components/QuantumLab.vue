<template>
  <div class="quantum-lab">
    <h2>Laboratorio Quantistico</h2>
    
    <div class="control-group">
      <label>Numero di Qubits:</label>
      <input type="number" v-model.number="params.n_qubits" min="1" max="5">
    </div>
    
    <div class="control-group">
      <label>Numero di Shot:</label>
      <input type="number" v-model.number="params.shots" min="100" max="10000">
    </div>
    
    <div class="gates-section">
      <h3>Gate Quantistici:</h3>
      <div class="gates-grid">
        <label v-for="gate in availableGates" :key="gate">
          <input type="checkbox" v-model="params.gates" :value="gate">
          {{ gate }}
        </label>
      </div>
    </div>
    
    <button @click="runSimulation" class="run-btn">
      Esegui Simulazione
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      availableGates: ['h', 'cx', 'x', 'y', 'z', 'swap', 'rx', 'ry', 'rz'],
      params: {
        n_qubits: 2,
        shots: 1024,
        gates: ['h', 'cx']
      }
    }
  },
  methods: {
    runSimulation() {
      this.$emit('run-simulation', this.params);
    }
  }
}
</script>

<style scoped>
.quantum-lab {
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

.control-group input {
  padding: 0.5rem;
  width: 100%;
}

.gates-section {
  margin-top: 1.5rem;
}

.gates-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  margin-top: 0.5rem;
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

.run-btn:hover {
  background-color: #2980b9;
}
</style>
