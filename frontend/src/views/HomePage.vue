<template>
  <div class="home-page p-6">
    <h1 class="text-3xl font-bold text-blue-600">Welcome to AI_RIQA</h1>
    <p class="text-gray-700 mt-2">An educational tool for scientific simulations.</p>
    <div class="mt-4">
      <router-link to="/simulation" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Start Simulation
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>
