"""
Backend FastAPI per AI_RIQA
Integrazione del core di simulazione con API REST
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os
from typing import Dict, Any
from pydantic import BaseModel

# Importa il core dalla stessa directory
from .core import RIQACore

app = FastAPI(
    title="AI_RIQA API",
    description="API per simulazioni avanzate",
    version="1.0.0"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inizializza il core
core = RIQACore()

# Modello Pydantic per la richiesta di simulazione
class SimulationRequest(BaseModel):
    sim_type: str
    params: Dict[str, Any]

# Endpoint principale
@app.get("/")
async def root():
    return {
        "message": "Benvenuto in AI_RIQA",
        "version": core.version,
        "supported_simulations": core.supported_simulations
    }

# Endpoint per le simulazioni
@app.post("/simulate")
async def simulate(request: SimulationRequest):
    try:
        result = core.run_simulation(request.sim_type, request.params)
        return {
            "status": "success",
            "simulation_type": request.sim_type,
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore interno: {str(e)}")

# Endpoint specifici per ogni tipo di simulazione
@app.post("/simulate/math")
async def simulate_math(params: Dict[str, Any]):
    return await simulate(SimulationRequest(sim_type="math", params=params))

@app.post("/simulate/ballistic")
async def simulate_ballistic(params: Dict[str, Any]):
    return await simulate(SimulationRequest(sim_type="ballistic", params=params))

@app.post("/simulate/quantum")
async def simulate_quantum(params: Dict[str, Any]):
    return await simulate(SimulationRequest(sim_type="quantum", params=params))

@app.post("/simulate/biological")
async def simulate_biological(params: Dict[str, Any]):
    return await simulate(SimulationRequest(sim_type="biological", params=params))

@app.post("/simulate/astral")
async def simulate_astral(params: Dict[str, Any]):
    return await simulate(SimulationRequest(sim_type="astral", params=params))

# Configurazione file statici (solo se necessario)
static_dir = Path(__file__).parent.parent / "frontend" / "dist"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
