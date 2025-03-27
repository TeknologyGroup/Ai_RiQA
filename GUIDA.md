Ecco la guida completa per avviare AI_RIQA in formato Markdown (`.md`), ottimizzata per il tuo progetto:

```markdown
# Guida all'Installazione e Configurazione di AI_RIQA

![AI_RIQA Logo](static/logo.png) <!-- Aggiungi il percorso del logo se disponibile -->

## 📋 Prerequisiti
- **Sistema Operativo**: Windows 10/11, macOS 12+, o Linux (Debian/Ubuntu)
- **Python**: 3.10+ ([Download](https://www.python.org/downloads/))
- **Node.js**: 16+ ([Download](https://nodejs.org/))
- **Git** (opzionale)
- **Tesseract OCR** (per elaborazione immagini):
  ```bash
  # Linux
  sudo apt install tesseract-ocr
  
  # macOS
  brew install tesseract
  
  # Windows
  # Scarica da https://github.com/UB-Mannheim/tesseract/wiki
  ```

## 🚀 Installazione Rapida

### 1. Clonare il repository
```bash
git clone https://github.com/TeknologyGroup/AI_RIQA.git
cd AI_RIQA
```

### 2. Configurazione ambiente Python
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 3. Frontend Vue.js
```bash
cd frontend
npm install
cd ..
```

## 🗄️ Configurazione Database

### Opzione A: SQLite (Default)
```bash
python backend/database.py
# Crea automaticamente riqa.db
```

### Opzione B: PostgreSQL (Produzione)
```bash
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql -c "CREATE DATABASE riqa;"
sudo -u postgres psql -c "CREATE USER riqa_admin WITH PASSWORD 'Martynb85.';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE riqa TO riqa_admin;"

# Imposta variabili d'ambiente
export DATABASE_TYPE="postgresql"
export DATABASE_URL="dbname=riqa user=riqa_admin password=Martynb85. host=localhost"
python backend/database.py
```

## 🔥 Avvio del Sistema

### Backend (FastAPI)
```bash
python backend/app.py
# Accessibile su http://localhost:8000
```

### Frontend (Vue.js)
```bash
cd frontend
npm run serve
# Accessibile su http://localhost:8080
```

## 🔐 Configurazione Firebase
1. Crea progetto su [Firebase Console](https://console.firebase.google.com/)
2. Modifica `frontend/src/firebase.js`:
```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};
```

## 🧪 Test di Funzionamento
1. **Test API Backend**:
   ```bash
   curl -X POST "http://localhost:8000/chat" \
   -H "Content-Type: application/json" \
   -d '{"message": "Risolvi x^2 - 4 = 0"}'
   ```

2. **Simulazione Quantistica**:
   ```python
   import requests
   response = requests.post(
       "http://localhost:8000/simulate",
       json={"sim_type": "quantum", "params": {"n_qubits": 2}}
   )
   print(response.json())
   ```

## 🐳 Deploy con Docker (Opzionale)
```bash
docker build -t ai_riqa .
docker run -p 8000:8000 ai_riqa
```

## 🚨 Risoluzione Problemi

### Problema: Moduli Python mancanti
```bash
pip install --force-reinstall -r requirements.txt
```

### Problema: Porte occupate
```bash
# Linux/macOS
sudo lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Problema: Connessione PostgreSQL fallita
Verifica:
1. Il servizio è attivo: `sudo systemctl status postgresql`
2. Le credenziali in `DATABASE_URL` sono corrette
3. Le regole in `/etc/postgresql/*/main/pg_hba.conf` includono:
   ```
   host    riqa    riqa_admin    127.0.0.1/32    md5
   ```

## 📊 Esempi di Comandi
| Categoria       | Esempio di Input          | Output Atteso               |
|----------------|--------------------------|----------------------------|
| Matematica     | `Risolvi x^2 - 4 = 0`    | Soluzioni e grafico         |
| Fisica         | `v0=20, angolo=45°`      | Traiettoria parabolica      |
| Quantistica    | `Simula 2 qubit`         | Matrice densità             |

## 📞 Supporto
Per assistenza contattare:  
**Martino Battista**  
📧 [martinobattista@gmail.com](mailto:martinobattista@gmail.com)  
🌐 [https://github.com/TeknologyGroup](https://github.com/TeknologyGroup)

---

> ℹ️ **Nota**: Per configurazioni avanzate, consultare la documentazione nel file `docs/ADVANCED_SETUP.md`
```

### Caratteristiche della guida:
1. **Formattazione chiara** con emoji per migliorare la leggibilità
2. **Sezioni logiche** con flusso di installazione intuitivo
3. **Comandi pronti all'uso** copiabili direttamente
4. **Tabelle riassuntive** per input/output di esempio
5. **Soluzioni rapide** per problemi comuni
6. **Multi-piattaforma** con istruzioni per Windows/Linux/macOS

Puoi personalizzare ulteriormente:
- Aggiungere screenshot per i passaggi chiave
- Includere un diagramma dell'architettura
- Aggiungere una sezione FAQ basata su problemi riscontrati
