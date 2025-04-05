<template>
  <div id="app">
    <nav class="p-4 bg-blue-500 text-white">
      <router-link to="/" class="mr-4 hover:underline">Home</router-link>
      <router-link to="/simulation" class="mr-4 hover:underline">Simulation</router-link>
      <router-link to="/quantum" class="mr-4 hover:underline">Quantum</router-link>
      <router-link to="/analysis" class="mr-4 hover:underline">Analysis</router-link>
      <router-link to="/visualization" class="mr-4 hover:underline">Visualization</router-link>
      <router-link to="/login" class="mr-4 hover:underline">Login</router-link>
      <router-link to="/register" class="hover:underline">Register</router-link>
    </nav>
    <router-view class="p-6" />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  color: #2C5282;
}
</style>
