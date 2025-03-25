import numpy as np
from scipy.integrate import solve_ivp
from qiskit import QuantumCircuit, execute, Aer

class RIQACore:
    def __init__(self):
        self.supported_simulations = ["math", "ballistic", "quantum", "biological", "astral"]

    def simulate_math(self, params):
        """Risolve equazioni matematiche."""
        def harmonic(t, y, k=1.0, m=1.0):
            x, v = y
            dx_dt = v
            dv_dt = -k * x / m
            return [dx_dt, dv_dt]
        t_span = params.get('time_range', [0, 10])
        y0 = params.get('initial_conditions', [1.0, 0.0])
        sol = solve_ivp(harmonic, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 100))
        return {'time': sol.t.tolist(), 'position': sol.y[0].tolist()}

    def simulate_ballistic(self, params):
        """Calcola traiettorie balistiche."""
        def motion(t, y, g):
            x, y, vx, vy = y
            return [vx, vy, 0, -g]
        t_span = params.get('time_range', [0, 10])
        y0 = [0, 0] + params.get('initial_velocity', [20 * np.cos(np.pi/4), 20 * np.sin(np.pi/4)])
        g = params.get('gravity', 9.81)
        sol = solve_ivp(motion, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 100))
        return {'x': sol.y[0].tolist(), 'y': sol.y[1].tolist(), 'time': sol.t.tolist()}

    def simulate_quantum(self, params):
        """Simula circuiti quantistici."""
        n_qubits = params.get('n_qubits', 2)
        qc = QuantumCircuit(n_qubits, n_qubits)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
        return result.get_counts()

    def simulate_biological(self, params):
        """Simula crescita biologica."""
        def growth(t, y, r):
            return [r * y[0]]
        t_span = params.get('time_range', [0, 10])
        y0 = [1.0]
        r = params.get('rate', 0.1)
        sol = solve_ivp(growth, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 100))
        return {'time': sol.t.tolist(), 'population': sol.y[0].tolist()}

    def simulate_astral(self, params):
        """Calcola orbite celesti."""
        r = params.get('radius', 1.0)
        t = np.linspace(0, 2 * np.pi, 100)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return {'x': x.tolist(), 'y': y.tolist()}

    def run_simulation(self, sim_type, params):
        if sim_type not in self.supported_simulations:
            raise ValueError(f"Simulazione '{sim_type}' non supportata")
        return getattr(self, f"simulate_{sim_type}")(params)