from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Optional
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

app = FastAPI()

# Modelli
class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user_key: str

# Endpoint pubblici
@app.post("/register", response_model=Token)
async def register_user(user_data: UserCreate):
    # Verifica se l'utente esiste già (implementazione fittizia)
    if get_user_from_db(user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username già registrato"
        )
    
    # Crea utente e genera chiave
    user = create_db_user(user_data.username, user_data.password)
    user_key = user.user_key
    
    # Crea token JWT
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

# Endpoint protetti
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/protected-data")
async def get_protected_data(
    current_user: TokenData = Depends(verify_user_key)
):
    return {
        "message": "Accesso consentito a dati protetti",
        "username": current_user.username,
        "user_key_valid": True
    }

@app.post("/rotate-key")
async def rotate_user_key(
    current_user: TokenData = Depends(verify_user_key)
):
    """Genera una nuova chiave invalidando la vecchia"""
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

# Middleware aggiuntivo (esempio)
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
