<template>
  <div class="login-page p-6">
    <h1 class="text-2xl font-bold text-blue-600">Login</h1>
    <form @submit.prevent="login" class="mt-4">
      <div class="mb-4">
        <label class="block text-gray-700">Username</label>
        <input v-model="username" type="text" class="w-full p-2 border rounded" placeholder="Enter username" />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700">Password</label>
        <input v-model="password" type="password" class="w-full p-2 border rounded" placeholder="Enter password" />
      </div>
      <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Login
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // Placeholder per logica di login
      console.log('Login attempted with:', this.username, this.password);
      this.$router.push('/');
    }
  }
};
</script>
