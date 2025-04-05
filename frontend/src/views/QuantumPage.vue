<template>
  <div class="quantum-page p-6">
    <h1 class="text-2xl font-bold text-blue-600">Quantum Simulations</h1>
    <QuantumLab @run-simulation="runSimulation" />
    <SimulationControls @run="updateParam" />
  </div>
</template>

<script>
import QuantumLab from '../components/QuantumLab.vue';
import SimulationControls from '../components/SimulationControls.vue';

export default {
  name: 'QuantumPage',
  components: {
    QuantumLab,
    SimulationControls
  },
  methods: {
    runSimulation(params) {
      console.log('Quantum Simulation Params:', params);
    },
    updateParam(params) {
      console.log('Simulation Controls Params:', params);
    }
  }
};
</script>
