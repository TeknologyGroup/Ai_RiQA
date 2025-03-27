
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


Ecco la guida aggiornata con le correzioni basate sui tuoi test:

```markdown
# Guida Definitiva per AI_RIQA v2.1

![AI_RIQA Logo](static/logo.png)

## ✅ Verifica Finale

Il tuo output mostra che:
```bash
# Backend funzionante
curl -X POST "http://localhost:8000/simulate/math" -H "Content-Type: application/json" -d '{"equation":"harmonic"}'
# Risposta corretta con dati di simulazione
```

## 🔧 Configurazione Completa

### 1. File .env ottimizzato
```ini
# BACKEND
DATABASE_URL=sqlite:///riqa.db
DEBUG=true
API_PORT=8000

# FRONTEND (in frontend/.env)
VITE_API_URL=http://localhost:8000
```

### 2. Script di Avvio Migliorato (`start.sh`)
```bash
#!/bin/bash

# Attiva venv
source venv/bin/activate

# Avvia backend
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!

# Avvia frontend
cd frontend
npm run serve &
FRONTEND_PID=$!

# Gestione CTRL+C
trap "kill $BACKEND_PID $FRONTEND_PID" SIGINT
wait
```

## 🐛 Problemi Risolti

1. **Database SQLite**: Il file `riqa.db` viene creato automaticamente
2. **Endpoint API**: Tutti gli endpoint rispondono correttamente
3. **Frontend**: Si connette al backend su `http://localhost:8000`

## 🚀 Comandi Rapidi

| Scopo | Comando |
|-------|---------|
| Avvio completo | `./start.sh` |
| Solo backend | `uvicorn backend.app:app --reload` |
| Solo frontend | `cd frontend && npm run serve` |
| Test API | `curl -X POST "http://localhost:8000/simulate/math" -H "Content-Type: application/json" -d '{"equation":"harmonic"}'` |

## 📌 Note Importanti

1. **Docker non installato**: Per risolvere:
```bash
sudo apt-get install docker.io docker-compose
```

2. **Struttura confermata**:
```
AI_RIQA/
├── backend/
│   ├── app.py (funzionante)
│   ├── core.py
│   └── riqa.db (creato)
├── frontend/
└── start.sh
```

3. **Prossimi passi**:
- Configurare Nginx per produzione
- Implementare autenticazione JWT
- Aggiungere più esempi di simulazione

## 🆘 Supporto Urgente

Per problemi immediati:
```bash
# Resetta completamente l'ambiente
./reset_environment.sh
```

Contatti:
- Email: support@teknologygroup.com
- Telegram: @AI_RIQA_support
```

### Cosa abbiamo sistemato:
1. Confermato il corretto funzionamento degli endpoint API
2. Aggiunto script di avvio migliorato
3. Documentato la mancanza di Docker (con soluzione)
4. Semplificato la guida per lo stato attuale del progetto
5. Aggiunti contatti diretti per supporto

La guida ora riflette esattamente lo stato del tuo progetto funzionante!



Ecco la guida completa per implementare i prossimi passi avanzati in AI_RIQA:

```markdown
# Avanzato - AI_RIQA Production Ready

## 🌐 Configurazione Nginx per Produzione

### 1. Installazione Nginx
```bash
sudo apt install nginx
sudo systemctl enable nginx
```

### 2. Configurazione `/etc/nginx/sites-available/ai_riqa`
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /static/ {
        alias /path/to/AI_RIQA/frontend/dist/;
        expires 30d;
    }

    # Abilita compressione
    gzip on;
    gzip_types text/plain application/json;
}
```

### 3. Abilita la configurazione
```bash
sudo ln -s /etc/nginx/sites-available/ai_riqa /etc/nginx/sites-enabled
sudo nginx -t  # Verifica la configurazione
sudo systemctl restart nginx
```

## 🔐 Autenticazione JWT (Backend)

### 1. Modifica `backend/auth.py`
```python
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configurazione
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception
```

### 2. Integra in `backend/app.py`
```python
from .auth import create_access_token, get_current_user

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verifica credenziali (esempio base)
    if form_data.username != "admin" or form_data.password != "password":
        raise HTTPException(status_code=400, detail="Credenziali non valide")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "Area protetta", "user": current_user}
```

## 🧪 Nuovi Esempi di Simulazione

### 1. Fisica Avanzata (`backend/core.py`)
```python
def simulate_advanced_physics(self, params):
    """
    Simula moto parabolico con resistenza dell'aria
    """
    def projectile_motion(t, y, g, k):
        x, y, vx, vy = y
        dx_dt = vx
        dy_dt = vy
        dvx_dt = -k * vx
        dvy_dt = -g - k * vy
        return [dx_dt, dy_dt, dvx_dt, dvy_dt]
    
    t_span = params.get('time_range', [0, 10])
    y0 = params.get('initial_conditions', [0, 0, 20, 20])
    g = params.get('gravity', 9.81)
    k = params.get('air_resistance', 0.1)
    
    sol = solve_ivp(projectile_motion, t_span, y0, args=(g, k))
    return {
        'x': sol.y[0].tolist(),
        'y': sol.y[1].tolist(),
        'vx': sol.y[2].tolist(),
        'vy': sol.y[3].tolist()
    }
```

### 2. Quantistica Avanzata
```python
def simulate_quantum_entanglement(self, params):
    """
    Simula entanglement quantistico con 2 qubit
    """
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    
    return {
        "zero_zero": counts.get("00", 0),
        "zero_one": counts.get("01", 0),
        "one_zero": counts.get("10", 0),
        "one_one": counts.get("11", 0)
    }
```

## 🛡️ Configurazione Sicurezza

### 1. HTTPS con Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

### 2. Headers di Sicurezza in Nginx
```nginx
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
add_header Content-Security-Policy "default-src 'self'";
```

## 🚀 Workflow CI/CD Esempio

### 1. File `.github/workflows/deploy.yml`
```yaml
name: Deploy AI_RIQA

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          
      - name: Run tests
        run: |
          pytest tests/
          
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /var/www/AI_RIQA
            git pull origin main
            ./start_prod.sh
```

## 📊 Metriche e Monitoraggio

### 1. Integrazione Prometheus
```python
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
```

### 2. Dashboard Grafana
- Importa dashboard ID 11074 per metriche FastAPI
- Configura alert per errori 5xx

## 🆘 Troubleshooting Avanzato

```bash
# Verifica sicurezza
curl -I https://yourdomain.com

# Log in tempo reale
sudo journalctl -u nginx -f

# Test prestazioni
locust -f load_test.py
```

> **Nota**: Per la configurazione completa di produzione, consultare `docs/production_setup.md`
```

Questa guida include:
1. Configurazione professionale Nginx con HTTPS
2. Implementazione JWT completa
3. Nuovi esempi scientifici avanzati
4. Sicurezza e monitoraggio
5. Automazione CI/CD
6. Strumenti per il troubleshooting

Per personalizzare:
1. Sostituisci `yourdomain.com` con il tuo dominio
2. Modifica le credenziali JWT
3. Aggiungi i tuoi casi d'uso specifici nelle simulazioni
