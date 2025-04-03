<template>
  <div id="app">
    <h1>RIQA Chatbot</h1>
    <select v-model="section">
      <option value="math">Matematica</option>
      <option value="ballistic">Balistica</option>
      <option value="quantum">Quantistica</option>
      <option value="biological">Biologica</option>
      <option value="astral">Astrale</option>
    </select>
    <chat :messages="messages" @send="sendMessage" />
    <button @click="saveWork">Salva</button>
    <button @click="login">Login</button>
    <developer-panel />
  </div>
</template>

<script>
import Chat from './components/Chat.vue';
import DeveloperPanel from './components/DeveloperPanel.vue';

export default {
  components: { Chat, DeveloperPanel },
  data() {
    return {
      section: 'math',
      messages: [],
      user: null
    };
  },
  methods: {
    async sendMessage(message) {
      this.messages.push({ role: 'user', content: message });
      const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          message, 
          client_id: this.user?.id || 'anonymous',
          section: this.section
        })
      });
      const data = await response.json();
      this.messages.push({ role: 'ai', content: JSON.stringify(data.result) });
    },
    async saveWork() {
      console.log('Salvataggio su cloud o dispositivo...');
      // Puoi implementare il salvataggio locale o con Netlify Functions
    },
    login() {
      // Semplice autenticazione mock (puoi implementare Netlify Identity dopo)
      this.user = { id: 'demo-user', name: 'Demo User' };
      alert("Modalità demo attiva - nessuna autenticazione reale");
    }
  }
};
</script>
