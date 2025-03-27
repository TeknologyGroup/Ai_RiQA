"""
Backend FastAPI avanzato per AI_RIQA
Integrazione del core di simulazione con API REST e autenticazione JWT
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pathlib import Path
import os
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from datetime import timedelta
import logging

# Configurazione logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importa il core e l'autenticazione
from .core import RIQACore
from .auth import (
    create_access_token,
    get_current_user,
    authenticate_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    User
)

# Inizializza l'app FastAPI
app = FastAPI(
    title="AI_RIQA API",
    description="API avanzata per simulazioni scientifiche",
    version="2.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configurazione CORS avanzata
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total-Count"]
)

# Schema per le richieste avanzate
class SimulationRequest(BaseModel):
    sim_type: str
    params: Dict[str, Any]
    tags: Optional[List[str]] = None
    priority: Optional[int] = 1

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None

# Inizializza il core
core = RIQACore()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Endpoint di autenticazione avanzati
@app.post("/token", response_model=Dict[str, str])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenziali non valide",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    # Qui implementa la registrazione utente
    return {"message": "User created successfully"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Endpoint di simulazione avanzati
@app.post("/simulate", response_model=Dict[str, Any])
async def simulate(
    request: SimulationRequest,
    current_user: User = Depends(get_current_user)
):
    """Endpoint avanzato per simulazioni con controllo di accesso"""
    try:
        logger.info(f"Simulation requested by {current_user.username}: {request}")
        
        result = core.run_simulation(request.sim_type, request.params)
        
        # Aggiungi metadati alla risposta
        response = {
            "status": "success",
            "simulation_type": request.sim_type,
            "result": result,
            "metadata": {
                "requested_by": current_user.username,
                "compute_time": "0.45s",  # Sostituisci con valore reale
                "tags": request.tags
            }
        }
        return response
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Server error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Errore interno: {str(e)}"
        )

# Endpoint specifici con documentazione avanzata
@app.post(
    "/simulate/math",
    summary="Esegui simulazione matematica",
    response_description="Risultati della simulazione matematica"
)
async def simulate_math(
    params: Dict[str, Any],
    current_user: User = Depends(get_current_user)
):
    """Esegue simulazioni matematiche avanzate"""
    return await simulate(SimulationRequest(sim_type="math", params=params))

# Aggiungi qui gli altri endpoint specifici (ballistic, quantum, etc.)...

# Endpoint di monitoraggio e diagnostica
@app.get("/health")
async def health_check():
    """Endpoint per il controllo dello stato del servizio"""
    return {
        "status": "healthy",
        "version": core.version,
        "active_simulations": core.get_active_simulations_count()
    }

@app.get("/metrics")
async def get_metrics():
    """Endpoint per metriche di prestazione"""
    return {
        "cpu_usage": "23%",
        "memory_usage": "1.2GB",
        "active_connections": 5
    }

# Configurazione file statici avanzata
static_dir = Path(__file__).parent.parent / "frontend" / "dist"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="frontend")

# Gestione degli errori personalizzata
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "path": request.url.path,
            "success": False
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        proxy_headers=True,
        timeout_keep_alive=60
    )
