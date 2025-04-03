<template>
  <div class="quantum-controls">
    <h2>Simulatore Quantistico</h2>
    
    <div class="params">
      <label>Qubits: <input v-model.number="params.n_qubits" type="number" min="1" max="5"></label>
      <label>Shots: <input v-model.number="params.shots" type="number" min="100" max="10000"></label>
      
      <div class="gates">
        <h3>Gate Quantistici:</h3>
        <label v-for="gate in availableGates" :key="gate">
          <input type="checkbox" v-model="params.gates" :value="gate"> {{ gate }}
        </label>
      </div>
    </div>
    
    <button @click="runSimulation">Esegui Simulazione</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      availableGates: ['h', 'cx', 'x', 'y', 'z', 'swap'],
      params: {
        n_qubits: 2,
        shots: 1024,
        gates: ['h', 'cx']
      }
    }
  },
  methods: {
    runSimulation() {
      this.$emit('run', this.params)
    }
  }
}
</script>

<style scoped>
.quantum-controls {
  border: 1px solid #ddd;
  padding: 20px;
  margin: 20px 0;
}
.params {
  margin: 15px 0;
}
.gates {
  margin-top: 10px;
}
label {
  display: block;
  margin: 5px 0;
}
</style>
