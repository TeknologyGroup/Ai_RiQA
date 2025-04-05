<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Scientific Simulations</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- Input Parameters -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Simulation Parameters</h2>
        <form @submit.prevent="startSimulation">
          <div class="mb-4">
            <label class="block text-sm font-medium mb-2">Simulation Type</label>
            <select v-model="simType" class="w-full p-2 border rounded">
              <option value="wormhole">Wormhole</option>
              <option value="quantum">Quantum</option>
              <option value="zeta">Zeta Function</option>
            </select>
          </div>
          
          <div class="mb-4">
            <label class="block text-sm font-medium mb-2">Parameters (JSON)</label>
            <textarea 
              v-model="parameters" 
              class="w-full p-2 border rounded h-32"
              placeholder='{"param1": value1, "param2": value2}'>
            </textarea>
          </div>
          
          <button 
            type="submit" 
            class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            :disabled="isRunning">
            {{ isRunning ? 'Running...' : 'Start Simulation' }}
          </button>
        </form>
      </div>
      
      <!-- Results -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Results</h2>
        <div v-if="isRunning" class="mb-4">
          <div class="h-2 bg-gray-200 rounded-full">
            <div 
              class="h-2 bg-blue-600 rounded-full" 
              :style="{width: progress + '%'}">
            </div>
          </div>
          <p class="text-sm mt-2">Progress: {{ progress }}%</p>
        </div>
        
        <div v-if="error" class="text-red-600 mb-4">{{ error }}</div>
        
        <div v-if="result" class="mt-4">
          <pre class="bg-gray-100 p-4 rounded overflow-auto">{{ result }}</pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import { io } from 'socket.io-client';

export default {
  name: 'SimulationPage',
  setup() {
    const simType = ref('wormhole');
    const parameters = ref('{}');
    const isRunning = ref(false);
    const progress = ref(0);
    const result = ref(null);
    const error = ref(null);
    let socket = null;

    const startSimulation = () => {
      isRunning.value = true;
      progress.value = 0;
      result.value = null;
      error.value = null;
      
      try {
        const params = JSON.parse(parameters.value);
        socket.emit('start_simulation', {
          type: simType.value,
          ...params
        });
      } catch (e) {
        error.value = 'Invalid JSON parameters';
        isRunning.value = false;
      }
    };

    onMounted(() => {
      socket = io(process.env.VUE_APP_WS_URL || 'http://localhost:3000');
      
      socket.on('simulation_update', (data) => {
        progress.value = data.progress;
      });
      
      socket.on('simulation_complete', (data) => {
        isRunning.value = false;
        result.value = data;
      });
      
      socket.on('simulation_error', (err) => {
        isRunning.value = false;
        error.value = err.error;
      });
    });

    onUnmounted(() => {
      if (socket) socket.disconnect();
    });

    return {
      simType,
      parameters,
      isRunning,
      progress,
      result,
      error,
      startSimulation
    };
  }
};
</script>
