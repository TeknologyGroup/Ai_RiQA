<template>
  <div id="app">
    <div class="header">
      <h1>RIQA Scientific Platform</h1>
      <div class="auth-section" v-if="user">
        <span>Benvenuto, {{ user.name }}</span>
        <button @click="logout">Logout</button>
      </div>
      <button v-else @click="login">Login</button>
    </div>

    <div class="main-container">
      <div class="sidebar">
        <button @click="activeTab = 'chat'" :class="{active: activeTab === 'chat'}">
          Chat Scientifico
        </button>
        <button @click="activeTab = 'quantum'" :class="{active: activeTab === 'quantum'}">
          Laboratorio Quantistico
        </button>
        <button @click="activeTab = 'simulations'" :class="{active: activeTab === 'simulations'}">
          Simulazioni Avanzate
        </button>
      </div>

      <div class="content">
        <div v-if="activeTab === 'chat'" class="chat-tab">
          <select v-model="section" class="section-select">
            <option value="math">Matematica</option>
            <option value="ballistic">Balistica</option>
            <option value="quantum">Quantistica</option>
            <option value="biological">Biologica</option>
            <option value="astral">Astrale</option>
          </select>
          <chat :messages="messages" @send="sendMessage" />
          <button @click="saveConversation" class="save-btn">
            Salva Conversazione
          </button>
        </div>

        <div v-if="activeTab === 'quantum'" class="quantum-tab">
          <quantum-lab @run-simulation="runQuantumSimulation" />
          <div v-if="quantumResults" class="results">
            <h3>Risultati Quantistici:</h3>
            <pre>{{ quantumResults }}</pre>
          </div>
        </div>

        <div v-if="activeTab === 'simulations'" class="simulations-tab">
          <simulation-controls @run="runAdvancedSimulation" />
          <div v-if="simulationResults" class="results">
            <h3>Risultati Simulazione:</h3>
            <pre>{{ simulationResults }}</pre>
          </div>
        </div>
      </div>
    </div>

    <developer-panel class="dev-panel" />
  </div>
</template>

<script>
import Chat from './components/Chat.vue';
import DeveloperPanel from './components/DeveloperPanel.vue';
import QuantumLab from './components/QuantumLab.vue';
import SimulationControls from './components/SimulationControls.vue';

export default {
  components: { 
    Chat, 
    DeveloperPanel,
    QuantumLab,
    SimulationControls
  },
  data() {
    return {
      activeTab: 'chat',
      section: 'math',
      messages: [],
      user: null,
      quantumResults: null,
      simulationResults: null,
      websocket: null
    };
  },
  created() {
    this.loadSavedData();
    this.initWebSocket();
  },
  beforeUnmount() {
    if (this.websocket) {
      this.websocket.close();
    }
  },
  methods: {
    async sendMessage(message) {
      this.messages.push({ role: 'user', content: message });
      
      try {
        const response = await fetch('/simulate', {
          method: 'POST',
          headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.user?.token || ''}`
          },
          body: JSON.stringify({ 
            message, 
            section: this.section,
            parameters: {
              client_id: this.user?.id || 'anonymous'
            }
          })
        });
        
        const data = await response.json();
        this.messages.push({ 
          role: 'ai', 
          content: data.result,
          rawData: data
        });
      } catch (error) {
        this.messages.push({
          role: 'error',
          content: `Errore: ${error.message}`
        });
      }
    },
    
    async runQuantumSimulation(params) {
      try {
        const response = await fetch('/simulate', {
          method: 'POST',
          headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.user?.token || ''}`
          },
          body: JSON.stringify({
            section: 'quantum',
            parameters: params
          })
        });
        this.quantumResults = await response.json();
      } catch (error) {
        console.error("Quantum simulation error:", error);
      }
    },
    
    async runAdvancedSimulation(params) {
      if (this.websocket) {
        this.websocket.send(JSON.stringify({
          section: params.type,
          parameters: params
        }));
      }
    },
    
    initWebSocket() {
      const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsUrl = `${wsProtocol}//${window.location.host}/ws/simulate`;
      
      this.websocket = new WebSocket(wsUrl);
      
      this.websocket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.status === 'success') {
          this.simulationResults = data.result;
        } else {
          console.error("Simulation error:", data.message);
        }
      };
    },
    
    async login() {
      // Implementa la tua logica di login
      this.user = { 
        id: 'demo-user', 
        name: 'Demo User',
        token: 'demo-token'
      };
    },
    
    logout() {
      this.user = null;
    },
    
    saveConversation() {
      localStorage.setItem('riqa_conversation', JSON.stringify({
        messages: this.messages,
        section: this.section
      }));
    },
    
    loadSavedData() {
      const saved = localStorage.getItem('riqa_conversation');
      if (saved) {
        const data = JSON.parse(saved);
        this.messages = data.messages || [];
        this.section = data.section || 'math';
      }
    }
  }
};
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #2c3e50;
  color: white;
}

.main-container {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 200px;
  background-color: #34495e;
  padding: 1rem;
}

.sidebar button {
  display: block;
  width: 100%;
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  background: none;
  border: none;
  color: white;
  text-align: left;
  cursor: pointer;
}

.sidebar button.active {
  background-color: #3498db;
}

.content {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
}

.section-select {
  margin-bottom: 1rem;
  padding: 0.5rem;
}

.save-btn {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #27ae60;
  color: white;
  border: none;
  cursor: pointer;
}

.dev-panel {
  margin-top: auto;
  padding: 1rem;
  background-color: #ecf0f1;
}

.results {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  max-height: 300px;
  overflow-y: auto;
}
</style>
