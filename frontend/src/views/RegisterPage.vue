<template>
  <div class="register-page p-6">
    <h1 class="text-2xl font-bold text-blue-600">Register</h1>
    <form @submit.prevent="register" class="mt-4">
      <div class="mb-4">
        <label class="block text-gray-700">Username</label>
        <input v-model="username" type="text" class="w-full p-2 border rounded" placeholder="Choose username" />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700">Password</label>
        <input v-model="password" type="password" class="w-full p-2 border rounded" placeholder="Choose password" />
      </div>
      <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Register
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    register() {
      // Placeholder per logica di registrazione
      console.log('Registered:', this.username, this.password);
      this.$router.push('/login');
    }
  }
};
</script>
