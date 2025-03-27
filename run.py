#!/usr/bin/env python3
import sys
from pathlib import Path

# Configurazione automatica dei path
sys.path.append(str(Path(__file__).parent))

from backend.app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
