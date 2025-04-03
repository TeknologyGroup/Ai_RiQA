# Fase di build per il frontend
FROM node:16 as frontend-builder

WORKDIR /app
COPY frontend/package*.json ./frontend/
RUN cd frontend && npm install

COPY frontend ./frontend
RUN cd frontend && npm run build

# Fase principale per il backend
FROM python:3.10-slim

WORKDIR /app

# Installa le dipendenze di sistema
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e installa i requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il backend
COPY backend ./backend
COPY ai ./ai

# Copia il frontend buildato
COPY --from=frontend-builder /app/frontend/dist ./backend/static

# Copia gli altri file necessari
COPY main.py .
COPY run.py .

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
