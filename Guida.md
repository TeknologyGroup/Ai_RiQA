
```markdown
# Guida Completa AI_RIQA v3.0

![AI_RIQA Logo](docs/assets/logo.png)

## 🌟 Novità nella Versione 3.0
- Autenticazione JWT avanzata
- Configurazione di produzione con Nginx
- Nuove simulazioni scientifiche
- Sistema di monitoraggio integrato
- Workflow CI/CD

## 🚀 Installazione Rapida

### Prerequisiti
```bash
# Linux
sudo apt install python3.10 python3-pip nodejs npm tesseract-ocr docker.io

# macOS
brew install python node tesseract docker
```

### 1. Clonazione e Setup
```bash
git clone https://github.com/TeknologyGroup/AI_RIQA.git
cd AI_RIQA
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configurazione
Crea `.env` nella root:
```ini
DATABASE_URL=sqlite:///riqa.db
JWT_SECRET=your-secret-key
API_PORT=8000
```

## 🔐 Autenticazione JWT

### Endpoint Disponibili
| Endpoint | Metodo | Descrizione |
|----------|--------|-------------|
| `/token` | POST | Ottieni token |
| `/register` | POST | Registra nuovo utente |
| `/users/me` | GET | Profilo utente |

**Esempio richiesta token:**
```bash
curl -X POST "http://localhost:8000/token" \
-H "Content-Type: application/json" \
-d '{"username":"admin","password":"secret"}'
```

## 🧪 Nuove Simulazioni

### Fisica Avanzata
```python
params = {
    "initial_conditions": [0, 0, 30, 30, 5],  # x,y,vx,vy,rotazione
    "air_resistance": 0.15,
    "magnus_effect": 0.03
}
response = requests.post("http://localhost:8000/simulate/advanced_physics", json=params)
```

### Quantum Entanglement
```python
params = {
    "n_qubits": 2,
    "gates": ["h_0", "cx_0_1", "h_1"],
    "shots": 2048
}
response = requests.post("http://localhost:8000/simulate/quantum_entanglement", json=params)
```

## 🛠️ Configurazione Produzione

### 1. Nginx + HTTPS
```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

### 2. Configurazione Nginx
```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/AI_RIQA/frontend/dist;
    }
}
```

## 📊 Monitoraggio

### Metriche Endpoint
| Endpoint | Descrizione |
|----------|-------------|
| `/metrics` | Metriche Prometheus |
| `/health` | Stato del servizio |

**Dashboard consigliate:**
- Grafana: Importa dashboard ID 11074
- Prometheus: Configura scrape endpoint `/metrics`

## 🔄 CI/CD Pipeline

`.github/workflows/deploy.yml`:
```yaml
name: Deploy AI_RIQA

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: |
          pip install -r requirements.txt
          pytest tests/
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: |
          docker-compose build
          scp -r . user@server:/var/www/AI_RIQA
          ssh user@server "cd /var/www/AI_RIQA && docker-compose up -d"
```

## 🐳 Docker Deployment

### 1. Costruisci i container
```bash
docker-compose -f docker-compose.prod.yml build
```

### 2. Avvia i servizi
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 🆘 Troubleshooting

### Errori Comuni e Soluzioni
| Problema | Soluzione |
|----------|----------|
| Moduli mancanti | `pip install -r requirements.txt` |
| Porte occupate | `sudo lsof -i :8000` poi `kill -9 PID` |
| Errori JWT | Verifica `JWT_SECRET` in `.env` |

### Comandi Utili
```bash
# Reset ambiente
./scripts/reset_environment.sh

# Log in tempo reale
docker-compose logs -f

# Test prestazioni
locust -f tests/load_test.py
```

## 📞 Supporto

**Canali ufficiali:**
- Email: support@teknologygroup.com
- Telegram: @AI_RIQA_support
- GitHub Issues: https://github.com/TeknologyGroup/AI_RIQA/issues

> ℹ️ **Documentazione completa**: Consulta `docs/` per guide avanzate

```

### Struttura della Documentazione:
1. **Introduzione**: Novità e prerequisiti
2. **Installazione**: Setup rapido
3. **Autenticazione**: JWT e sicurezza
4. **Simulazioni**: Nuove funzionalità
5. **Produzione**: Nginx, Docker, HTTPS
6. **Monitoraggio**: Metriche e health check
7. **CI/CD**: Automazione deployment
8. **Troubleshooting**: Soluzioni rapide

### File Aggiuntivi Consigliati:
1. `docs/production_setup.md`: Configurazione avanzata produzione
2. `docs/api_reference.md`: Documentazione API completa
3. `docs/development.md`: Guida per contributori

La guida è stata completamente riorganizzata per:
- Maggiore chiarezza
- Migliore organizzazione delle sezioni
- Istruzioni più dettagliate
- Soluzioni pronte all'uso
- Riferimenti incrociati
