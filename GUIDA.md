
# AI_RIQA Advanced Implementation Guide

## Table of Contents
- [Production Deployment with Nginx](#-production-deployment-with-nginx)
- [JWT Authentication System](#-jwt-authentication-system)
- [Advanced Simulation Examples](#-advanced-simulation-examples)
- [Security Configuration](#-security-configuration)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Monitoring & Metrics](#-monitoring--metrics)
- [Troubleshooting](#-troubleshooting)

## 🌐 Production Deployment with Nginx

### 1. Install Nginx
```bash
sudo apt update && sudo apt install -y nginx
sudo systemctl enable nginx
```

### 2. Configure `/etc/nginx/sites-available/ai_riqa`
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /static/ {
        alias /path/to/AI_RIQA/frontend/dist/;
        expires 30d;
        access_log off;
    }

    # Enable compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;
    gzip_min_length 1024;
}
```

### 3. Enable Configuration
```bash
sudo ln -s /etc/nginx/sites-available/ai_riqa /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl restart nginx
```

## 🔐 JWT Authentication System

### Backend Implementation (`backend/auth.py`)
```python
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# Configuration
SECRET_KEY = "your-256-bit-secret"  # Generate: openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class TokenData(BaseModel):
    username: str | None = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

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
    return token_data
```

### Integration with FastAPI (`backend/app.py`)
```python
from .auth import (
    get_current_user,
    create_access_token,
    get_password_hash,
    verify_password
)

# Add these routes
@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/")
async def read_users_me(
    current_user: TokenData = Depends(get_current_user)
):
    return {"username": current_user.username}
```

## 🧪 Advanced Simulation Examples

### 1. Physics Simulation with Air Resistance
```python
from scipy.integrate import solve_ivp

def projectile_motion_with_drag(params: dict):
    """
    Simulates projectile motion with air resistance
    Returns: {
        "time_points": [...],
        "x_positions": [...], 
        "y_positions": [...],
        "velocities": [...]
    }
    """
    def motion_equations(t, y, k, g):
        x, y, vx, vy = y
        dxdt = vx
        dydt = vy
        dvxdt = -k * vx * (vx**2 + vy**2)**0.5
        dvydt = -g - k * vy * (vx**2 + vy**2)**0.5
        return [dxdt, dydt, dvxdt, dvydt]
    
    # Default parameters
    k = params.get('drag_coefficient', 0.1)
    g = params.get('gravity', 9.81)
    v0 = params.get('initial_velocity', 20)
    angle = params.get('angle', 45)
    t_span = params.get('time_span', (0, 10))
    
    # Convert angle to radians
    angle_rad = np.radians(angle)
    vx0 = v0 * np.cos(angle_rad)
    vy0 = v0 * np.sin(angle_rad)
    
    # Solve differential equations
    solution = solve_ivp(
        motion_equations,
        t_span,
        [0, 0, vx0, vy0],
        args=(k, g),
        dense_output=True
    )
    
    return {
        "time_points": solution.t.tolist(),
        "x_positions": solution.y[0].tolist(),
        "y_positions": solution.y[1].tolist(),
        "velocities": (solution.y[2]**2 + solution.y[3]**2)**0.5.tolist()
    }
```

### 2. Quantum Circuit Simulation
```python
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def simulate_quantum_circuit(params: dict):
    """
    Simulates quantum circuit with variable gates
    Returns: {
        "counts": {"00": x, "01": y, ...},
        "histogram": "base64_encoded_image"
    }
    """
    n_qubits = params.get('qubits', 2)
    gates = params.get('gates', ['h', 'cx'])
    measurements = params.get('measurements', n_qubits)
    
    qc = QuantumCircuit(n_qubits, measurements)
    
    # Apply gates
    for gate in gates:
        if gate == 'h':
            qc.h(0)
        elif gate == 'x':
            qc.x(0)
        elif gate == 'cx':
            if n_qubits >= 2:
                qc.cx(0, 1)
        # Add more gates as needed
    
    qc.measure_all()
    
    # Simulate
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    
    # Generate histogram
    fig = plot_histogram(counts)
    fig.savefig('quantum_histogram.png')
    with open("quantum_histogram.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    
    return {
        "counts": counts,
        "histogram": encoded_image
    }
```

## 🛡️ Security Configuration

### 1. HTTPS with Let's Encrypt
```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
# Auto-renewal
sudo certbot renew --dry-run
```

### 2. Security Headers in Nginx
```nginx
# Add to server block
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
add_header Content-Security-Policy "default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval'";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

## 🔄 CI/CD Pipeline

### GitHub Actions (`.github/workflows/deploy.yml`)
```yaml
name: Deploy AI_RIQA

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest
          
      - name: Run tests
        run: |
          pytest tests/
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy to Production
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /var/www/AI_RIQA
            git pull origin main
            docker-compose down
            docker-compose up -d --build
```

## 📊 Monitoring & Metrics

### 1. Prometheus Integration
```python
from prometheus_client import make_asgi_app, Counter, Histogram
from fastapi import FastAPI

# Create metrics
REQUEST_COUNT = Counter(
    'request_count',
    'Total HTTP requests count',
    ['method', 'endpoint', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'request_latency_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

# Add middleware to app
@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.time()
    method = request.method
    endpoint = request.url.path
    
    try:
        response = await call_next(request)
    except Exception as e:
        REQUEST_COUNT.labels(method, endpoint, 500).inc()
        raise e
    
    duration = time.time() - start_time
    REQUEST_LATENCY.labels(method, endpoint).observe(duration)
    REQUEST_COUNT.labels(method, endpoint, response.status_code).inc()
    
    return response

# Add metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
```

### 2. Grafana Dashboard Setup
1. Install Grafana: 
   ```bash
   sudo apt-get install -y grafana
   sudo systemctl start grafana-server
   ```
2. Configure Prometheus as data source
3. Import FastAPI dashboard (ID 11074)

## 🚨 Troubleshooting

### Common Issues and Solutions

**1. Nginx 502 Bad Gateway**
```bash
# Check backend logs
journalctl -u your_backend_service

# Test backend manually
curl -v http://localhost:8000/health
```

**2. Database Connection Issues**
```bash
# PostgreSQL check
sudo -u postgres psql -c "\l"

# SQLite permissions
chmod 664 your_db_file.db
```

**3. Performance Testing**
```python
# Create load_test.py
from locust import HttpUser, task, between

class AI_RIQAUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def simulate_math(self):
        self.client.post("/simulate/math", json={
            "equation": "harmonic",
            "initial_conditions": [1.0, 0.0]
        })
```

Run with:
```bash
locust -f load_test.py
```

---

**License**: AI_RIQA © 2025 by Martino Battista is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/)
