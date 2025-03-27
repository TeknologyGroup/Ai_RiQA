# backend/simulation.py
import numpy as np
from scipy.integrate import solve_ivp
from functools import lru_cache
from pydantic import BaseModel, confloat
from typing import Tuple

class SimulationParameters(BaseModel):
    time_range: Tuple[confloat(gt=0), confloat(gt=0)] = (0, 10)
    initial_conditions: Tuple[float, float] = (1.0, 0.0)
    k: confloat(gt=0) = 1.0  # Costante elastica
    m: confloat(gt=0) = 1.0  # Massa

@lru_cache(maxsize=100)
def simulate_complex_system(params: SimulationParameters):
    """Simula un sistema fisico complesso con validazione input e caching."""
    def system(t, y, k=params.k, m=params.m):
        x, v = y
        dx_dt = v
        dv_dt = -k * x / m
        return [dx_dt, dv_dt]
    
    sol = solve_ivp(
        system,
        params.time_range,
        params.initial_conditions,
        method='RK45',
        t_eval=np.linspace(*params.time_range, 100)
    )  # Aggiunto parentesi mancante qui
    
    return {
        'time': sol.t.tolist(),
        'position': sol.y[0].tolist(),
        'velocity': sol.y[1].tolist(),
        'energy': (params.k * sol.y[0]**2 + params.m * sol.y[1]**2).tolist()  # Nuova metrica
    }
