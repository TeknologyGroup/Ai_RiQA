<template>
  <div class="chat-container">
    <div v-for="(msg, index) in messages" :key="index" :class="msg.role">
      {{ msg.content }}
    </div>
    <input v-model="input" @keyup.enter="send" placeholder="Scrivi o carica..." />
    <button @click="send">Invia</button>
    <button @click="record">Microfono</button>
    <input type="file" @change="uploadFile" />
  </div>
</template>

<script>
export default {
  props: ['messages'],
  data() {
    return { input: '' };
  },
  methods: {
    send() {
      if (this.input) {
        this.$emit('send', this.input);
        this.input = '';
      }
    },
    record() {
      // Implementare input vocale con Web Speech API
      console.log('Registrazione vocale...');
    },
    async uploadFile(event) {
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append('file', file);
      const response = await fetch('/upload', { method: 'POST', body: formData });
      const data = await response.json();
      this.$emit('send', data.result);
    }
  }
};
</script>