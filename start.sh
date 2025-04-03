#!/bin/bash

# Build del frontend
echo "Building frontend..."
cd frontend
npm install
npm run build

# Crea la cartella static nel backend
echo "Preparing static files..."
mkdir -p ../backend/static
cp -r dist/* ../backend/static/

# Avvia il backend con Uvicorn
echo "Starting backend server..."
cd ../backend
uvicorn app:app --host 0.0.0.0 --port 8000 --reload &

# Messaggio di completamento
echo "Application is running on http://localhost:8000"
echo "Frontend is served from /static"
