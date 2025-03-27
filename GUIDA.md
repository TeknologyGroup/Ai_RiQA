
```markdown
# Guida all'Installazione e Configurazione di AI_RIQA v2.0

![AI_RIQA Logo](static/logo.png)

## 📋 Prerequisiti
- **Python 3.10+** con pip
- **Node.js 16+** e npm
- **PostgreSQL** (opzionale, solo per deploy avanzato)
- **Tesseract OCR** (per elaborazione immagini):
  ```bash
  # Linux
  sudo apt install tesseract-ocr libtesseract-dev
  # macOS
  brew install tesseract
  ```

## 🛠️ Installazione

### 1. Clonare e configurare
```bash
git clone https://github.com/TeknologyGroup/AI_RIQA.git
cd AI_RIQA
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 2. Backend (FastAPI)
```bash
pip install -r requirements.txt
```

### 3. Frontend (Vue 3)
```bash
cd frontend
npm install
npm run build  # Per produzione
cd ..
```

## ⚙️ Configurazione

### File .env (creare nella root)
```ini
# Backend
DATABASE_URL=sqlite:///riqa.db
# Per PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost/riqa

# Frontend (in frontend/.env)
VITE_API_URL=http://localhost:8000
```

## 🚀 Avvio

### Metodo Consigliato (con script integrato)
```bash
./start.sh  # Avvia sia backend che frontend
```

### Manualmente:
```bash
# Backend
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload

# Frontend (in altro terminale)
cd frontend
npm run serve
```

## 🌐 Endpoint API Principali

| Endpoint | Metodo | Descrizione |
|----------|--------|-------------|
| `/simulate` | POST | Esegue simulazioni |
| `/simulate/{type}` | POST | Simulazione specifica |
| `/docs` | GET | Documentazione Swagger |

**Esempio chiamata:**
```bash
curl -X POST "http://localhost:8000/simulate/math" \
-H "Content-Type: application/json" \
-d '{"equation":"harmonic"}'
```

## 🐳 Docker Deployment

### 1. Costruisci l'immagine
```bash
docker compose build
```

### 2. Avvia i container
```bash
docker compose up -d
```

## 🔍 Struttura del Progetto Aggiornata

```
AI_RIQA/
├── backend/
│   ├── app.py          # Nuova API FastAPI
│   ├── core.py         # Logica simulazioni
│   ├── database.py     # Gestione DB
├── frontend/           # Vue 3
│   ├── public/         # File statici
│   └── src/            # Codice frontend
├── start.sh            # Script di avvio
└── docker-compose.yml  # Configurazione Docker
```

## 🚨 Risoluzione Problemi

### Errore "ModuleNotFound"
```bash
# Riavvio ambiente virtuale
deactivate && source venv/bin/activate
pip install -r requirements.txt
```

### Frontend non si connette al backend
1. Verifica `VITE_API_URL` in `frontend/.env`
2. Abilita CORS nel backend (già configurato in `app.py`)

### Problemi con PostgreSQL
```bash
sudo service postgresql restart
psql -h localhost -U your_user -d riqa -W
```

## 📊 Esempi di Simulazione

**Matematica:**
```python
import requests
response = requests.post(
    "http://localhost:8000/simulate/math",
    json={"equation": "harmonic", "initial_conditions": [1.0, 0.0]}
)
```

**Quantistica:**
```python
response = requests.post(
    "http://localhost:8000/simulate/quantum",
    json={"n_qubits": 2, "gates": ["h", "cx"]}
)
```

## 🔄 Workflow di Sviluppo

1. Modifica il frontend in `frontend/src/`
2. Testa le API su `http://localhost:8000/docs`
3. Per produzione:
   ```bash
   cd frontend && npm run build
   docker compose up --build -d
   ```

## 📞 Supporto

Per problemi critici:
- **Email**: [support@teknologygroup.com](mailto:support@teknologygroup.com)
- **Issues**: [GitHub Issues](https://github.com/TeknologyGroup/AI_RIQA/issues)

> ℹ️ **Nota**: La configurazione completa è disponibile in `docs/configuration.md`
```

### Novità nella Guida:
1. **Struttura semplificata** con focus sulle nuove funzionalità
2. **Configurazione .env** per gestione centralizzata
3. **Esempi API aggiornati** con la nuova struttura FastAPI
4. **Workflow Docker** integrato
5. **Sezione troubleshooting** ampliata
6. **Compatibilità** con l'architettura a microservizi

Per personalizzare:
1. Sostituisci i percorsi dei file con la tua struttura esatta
2. Aggiungi screenshot della nuova interfaccia
3. Includi esempi specifici del tuo dominio applicativo
