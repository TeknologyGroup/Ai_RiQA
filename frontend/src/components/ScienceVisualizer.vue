<template>
  <div class="visualizer">
    <div class="visualization-container">
      <img v-if="imageData" :src="'data:image/png;base64,' + imageData" alt="Visualizzazione scientifica">
      <div v-else class="placeholder">
        Nessun dato da visualizzare
      </div>
    </div>
    
    <div class="controls">
      <select v-model="visualizationType">
        <option value="circuit">Circuito Quantistico</option>
        <option value="timeseries">Serie Temporale</option>
        <option value="3dplot">Visualizzazione 3D</option>
      </select>
      
      <button @click="exportImage">Esporta PNG</button>
    </div>
    
    <div v-if="analysisResults" class="analysis">
      <h3>Analisi Scientifica:</h3>
      <pre>{{ analysisResults }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    simulationData: Object
  },
  data() {
    return {
      visualizationType: 'circuit',
      imageData: null,
      analysisResults: null
    }
  },
  watch: {
    simulationData: {
      immediate: true,
      handler(newData) {
        if (newData) {
          this.generateVisualization(newData);
          this.analyzeData(newData);
        }
      }
    }
  },
  methods: {
    async generateVisualization(data) {
      const response = await fetch('/api/visualize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: this.visualizationType,
          data: data
        })
      });
      const result = await response.json();
      this.imageData = result.image;
    },
    
    async analyzeData(data) {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      this.analysisResults = await response.json();
    },
    
    exportImage() {
      if (!this.imageData) return;
      
      const link = document.createElement('a');
      link.href = `data:image/png;base64,${this.imageData}`;
      link.download = `riqa_visualization_${Date.now()}.png`;
      link.click();
    }
  }
}
</script>

<style scoped>
.visualizer {
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1rem;
  margin-top: 1rem;
}

.visualization-container {
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8fafc;
  margin-bottom: 1rem;
}

.placeholder {
  color: #64748b;
}

.controls {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.analysis {
  background-color: #f1f5f9;
  padding: 1rem;
  border-radius: 0.25rem;
  max-height: 200px;
  overflow-y: auto;
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
