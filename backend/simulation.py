# backend/simulation.py
import numpy as np
from scipy.integrate import solve_ivp

def simulate_complex_system(params):
    """Simula un sistema fisico complesso (es. oscillatore quantistico)."""
    def system(t, y, k=1.0, m=1.0):
        x, v = y
        dx_dt = v
        dv_dt = -k * x / m  # Equazione oscillatore armonico
        return [dx_dt, dv_dt]
    
    t_span = params.get('time_range', [0, 10])
    y0 = params.get('initial_conditions', [1.0, 0.0])
    sol = solve_ivp(system, t_span, y0, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], 100))
    return {'time': sol.t.tolist(), 'position': sol.y[0].tolist(), 'velocity': sol.y[1].tolist()}