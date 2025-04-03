from qiskit import QuantumCircuit, execute, Aer
from scipy.integrate import solve_ivp
import numpy as np

class RIQACore:
    # [...] Mantieni il codice esistente
    
    def simulate_quantum_entanglement(self, params: Dict) -> Dict:
        """Nuova simulazione di entanglement quantistico"""
        n_qubits = params.get('n_qubits', 2)
        qc = QuantumCircuit(n_qubits, n_qubits)
        
        # Applica gate in base ai parametri
        for gate in params.get('gates', ['h', 'cx']):
            if gate == 'h':
                qc.h(0)
            elif gate == 'cx':
                qc.cx(0, 1)
                
        qc.measure_all()
        
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc, backend, shots=params.get('shots', 1024))
        counts = job.result().get_counts(qc)
        
        return {
            'counts': counts,
            'entropy': self._calculate_entropy(counts),
            'circuit': qc.draw(output='text')
        }
    
    def _calculate_entropy(self, counts: Dict) -> float:
        """Helper per calcolo entropia"""
        total = sum(counts.values())
        probs = [v/total for v in counts.values()]
        return -sum(p * np.log2(p) for p in probs if p > 0)
