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
    <button v-if="!user" @click="login">Login</button>
    <button v-else @click="logout">Logout</button>
    <developer-panel />
  </div>
</template>

<script>
import Chat from './components/Chat.vue';
import DeveloperPanel from './components/DeveloperPanel.vue';
import { auth, googleProvider } from './firebase';
import { signInWithPopup, signOut } from 'firebase/auth';

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
        body: JSON.stringify({ message, client_id: this.user?.uid || 'anonymous' })
      });
      const data = await response.json();
      this.messages.push({ role: 'ai', content: JSON.stringify(data.result) });
    },
    async saveWork() {
      // Simula salvataggio (da integrare con Google Drive API)
      console.log('Salvataggio su cloud o dispositivo...');
    },
    async login() {
      try {
        const result = await signInWithPopup(auth, googleProvider);
        this.user = result.user;
      } catch (error) {
        console.error("Errore di login:", error);
      }
    },
    async logout() {
      await signOut(auth);
      this.user = null;
    }
  },
  created() {
    auth.onAuthStateChanged(user => this.user = user);
  }
};
</script>
