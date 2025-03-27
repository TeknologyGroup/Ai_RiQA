#!/bin/bash
cd frontend
npm install
npm run build
mkdir -p ../backend/static
cp -r dist/* ../backend/static/
