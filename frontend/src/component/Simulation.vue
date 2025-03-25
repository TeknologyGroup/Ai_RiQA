// frontend/src/components/Simulation.vue
<template>
  <div>
    <h2>Simulazione Avanzata</h2>
    <button @click="startSimulation">Avvia</button>
    <div id="plot"></div>
  </div>
</template>
<script>
import Plotly from 'plotly.js-dist';
export default {
  methods: {
    async startSimulation() {
      const response = await fetch('/simulate', {
        method: 'POST',
        body: JSON.stringify({ type: 'quantum', input: { n_qubits: 3 } })
      });
      const data = await response.json();
      Plotly.newPlot('plot', [{ y: Object.values(data.result), type: 'bar' }], { title: 'Risultati Quantistici' });
    }
  }
}
</script>