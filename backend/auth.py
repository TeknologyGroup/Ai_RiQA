from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Dict, Optional
from uuid import uuid4
from pydantic import BaseModel

# Configurazione
SECRET_KEY = "your-secret-key-change-this-in-production"  # In produzione usa una chiave segreta complessa
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
KEY_EXPIRATION_DAYS = 90

# Strutture dati
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user_keys_db: Dict[str, str] = {}  # Sostituire con database reale in produzione

# Modelli
class TokenData(BaseModel):
    username: Optional[str] = None
    user_key: Optional[str] = None

class User(BaseModel):
    username: str
    hashed_password: str
    user_key: Optional[str] = None

# Funzioni di utilità
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def generate_user_key(username: str) -> str:
    """Genera e salva una chiave unica per l'utente con scadenza"""
    key_id = uuid4().hex[:12]
    timestamp = int(datetime.utcnow().timestamp())
    expiry = timestamp + (KEY_EXPIRATION_DAYS * 86400)
    user_key = f"ak_{key_id}_{timestamp}_{expiry}"
    user_keys_db[username] = user_key
    return user_key

def get_user_key(username: str) -> Optional[str]:
    """Recupera la chiave utente"""
    return user_keys_db.get(username)

def validate_user_key(key: str) -> bool:
    """Verifica se una chiave esiste nel sistema e non è scaduta"""
    if key not in user_keys_db.values():
        return False
    return not is_key_expired(key)

def is_key_expired(key: str) -> bool:
    """Verifica se una chiave è scaduta"""
    try:
        _, _, _, expiry = key.split('_')
        return datetime.utcnow().timestamp() > float(expiry)
    except:
        return True

# Funzioni JWT
def create_access_token(data: dict, user_key: str, expires_delta: timedelta = None):
    """Crea JWT includendo l'user key come claim"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({
        "exp": expire,
        "ukey": user_key  # Aggiunge l'user key al payload JWT
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, user_key=payload.get("ukey"))
    except JWTError:
        raise credentials_exception
    return token_data

async def verify_user_key(
    token: str = Depends(oauth2_scheme),
    x_user_key: Optional[str] = Header(None)
):
    """Verifica combinata di JWT e User Key"""
    if not x_user_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User key mancante"
        )
    
    # Verifica JWT
    payload = decode_token(token)
    username = payload.username
    
    # Verifica User Key
    stored_key = get_user_key(username)
    if not stored_key or stored_key != x_user_key or not validate_user_key(x_user_key):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User key non valida o scaduta"
        )
    
    return payload

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    # Verifica esistenza utente (da implementare con DB reale)
    user = get_user_from_db(username)
    if user is None:
        raise credentials_exception
    return user

# Funzioni fittizie per DB (da implementare)
def get_user_from_db(username: str) -> Optional[User]:
    # Implementare con database reale
    return User(username=username, hashed_password="fakehashedpass")

def create_db_user(username: str, password: str) -> User:
    # Implementare con database reale
    user_key = generate_user_key(username)
    return User(
        username=username,
        hashed_password=get_password_hash(password),
        user_key=user_key
    )
