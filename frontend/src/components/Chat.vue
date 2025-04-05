<template>
  <div class="chat">
    <div v-for="(msg, index) in messages" :key="index" :class="msg.role">
      {{ msg.content }}
    </div>
    <input v-model="newMessage" @keyup.enter="send" placeholder="Type a message..." />
    <button @click="send">Send</button>
  </div>
</template>

<script>
export default {
  props: {
    messages: { type: Array, default: () => [] }
  },
  data() {
    return { newMessage: '' };
  },
  methods: {
    send() {
      if (this.newMessage.trim()) {
        this.$emit('send', this.newMessage);
        this.newMessage = '';
      }
    }
  }
};
</script>

<style scoped>
.chat { border: 1px solid #4299E1; padding: 10px; max-width: 600px; margin: 10px auto; }
.user { color: #2C5282; text-align: right; }
.ai { color: #4299E1; text-align: left; }
input { width: 80%; padding: 5px; margin-right: 10px; }
button { padding: 5px 10px; background-color: #4299E1; color: white; border: none; cursor: pointer; }
</style>
