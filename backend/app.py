from fastapi import FastAPI, Depends, HTTPException, status, Header, WebSocket, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta
from typing import Optional
from pathlib import Path
import asyncio
from .auth import (
    create_access_token,
    get_password_hash,
    verify_password,
    get_current_user,
    verify_user_key,
    generate_user_key,
    get_user_key,
    create_db_user,
    User,
    TokenData,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from pydantic import BaseModel
from .core import RIQACore
from .visualization import VisualizationEngine
from .analysis import DataAnalyzer
from .ai import AIModelHub

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta la cartella static per il frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

core = RIQACore()

# Modelli
class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user_key: str

class SimulationRequest(BaseModel):
    message: str
    section: str
    parameters: Optional[dict] = None

class VisualizationRequest(BaseModel):
    type: str = 'circuit'
    data: dict

class AnalysisRequest(BaseModel):
    type: str = 'quantum'
    data: dict

class OptimizationRequest(BaseModel):
    type: str
    code: str

# Endpoint pubblici
@app.post("/register", response_model=Token)
async def register_user(user_data: UserCreate):
    if get_user_from_db(user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username già registrato"
        )
    
    user = create_db_user(user_data.username, user_data.password)
    user_key = user.user_key
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        user_key=user_key,
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_key": user_key
    }

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username o password errati",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_key = get_user_key(user.username)
    if not user_key:
        user_key = generate_user_key(user.username)
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        user_key=user_key,
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_key": user_key
    }

# Endpoint scientifici
@app.post("/simulate")
async def run_simulation(
    request: SimulationRequest,
    current_user: TokenData = Depends(verify_user_key)
):
    try:
        result = core.run_simulation(
            request.section,
            request.parameters or {"message": request.message}
        )
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.websocket("/ws/simulate")
async def websocket_simulation(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            result = core.run_simulation(data['section'], data.get('parameters', {}))
            await websocket.send_json({
                "status": "success",
                "result": result
            })
    except Exception as e:
        await websocket.send_json({
            "status": "error",
            "message": str(e)
        })
    finally:
        await websocket.close()

# Nuovi endpoint per visualizzazione e analisi
@app.post("/visualize")
async def visualize_data(
    request: VisualizationRequest,
    current_user: TokenData = Depends(verify_user_key)
):
    try:
        if request.type == 'circuit':
            image = VisualizationEngine.plot_quantum_circuit(request.data.get('circuit', ''))
        else:
            image = VisualizationEngine.plot_simulation_results(request.data)
        
        return {"status": "success", "image": image}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/analyze")
async def analyze_data(
    request: AnalysisRequest,
    current_user: TokenData = Depends(verify_user_key)
):
    try:
        if request.type == 'quantum':
            results = DataAnalyzer.analyze_quantum_results(request.data.get('counts', {}))
        else:
            results = DataAnalyzer.time_series_analysis(request.data)
        
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/optimize")
async def optimize_code(
    request: OptimizationRequest,
    current_user: TokenData = Depends(verify_user_key)
):
    try:
        if request.type == 'quantum':
            result = AIModelHub().optimize_quantum_circuit(request.code)
        else:
            result = AIModelHub().solve_math_expression(request.code)
        
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# Endpoint protetti
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/rotate-key")
async def rotate_user_key(current_user: TokenData = Depends(verify_user_key)):
    new_key = generate_user_key(current_user.username)
    return {
        "message": "Chiave rigenerata con successo",
        "new_key": new_key
    }

# Funzioni di utilità
def authenticate_user(username: str, password: str) -> Optional[User]:
    user = get_user_from_db(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def get_user_from_db(username: str) -> Optional[User]:
    # Implementazione fittizia - sostituire con DB reale
    if username == "testuser":
        return User(
            username="testuser",
            hashed_password=get_password_hash("testpass"),
            user_key="ak_testkey_1234567890_9999999999"
        )
    return None

# Middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

# Frontend route - deve essere l'ultima route
@app.get("/{full_path:path}")
async def serve_frontend(request: Request, full_path: str):
    static_path = Path("static") / "index.html"
    if not static_path.exists():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(static_path)
