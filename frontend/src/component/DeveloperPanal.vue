<template>
  <div class="developer-panel" :class="{ open: isOpen }">
    <button @click="isOpen = !isOpen">⚙️</button>
    <div v-if="isOpen">
      <h3>Sviluppatore</h3>
      <p>Debug: {{ debugLog }}</p>
      <p>Log: {{ simulationLog }}</p>
      <input v-model="themeColor" placeholder="Colore tema (es. #4299E1)" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      debugLog: 'Nessun errore',
      simulationLog: 'Nessuna simulazione',
      themeColor: '#4299E1'
    };
  }
};
</script>

<style>
.developer-panel { position: fixed; top: 10px; right: 10px; }
.open { background: #E6F0FA; padding: 10px; border-radius: 5px; }
</style>