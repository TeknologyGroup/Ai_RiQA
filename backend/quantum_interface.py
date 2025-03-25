# backend/quantum_interface.py
from qiskit import QuantumCircuit, execute, Aer

def run_advanced_quantum_sim(params):
    n_qubits = params.get('n_qubits', 2)
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))  # Porta Hadamard su tutti i qubit
    qc.cx(0, 1)  # Entanglement
    qc.measure_all()
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    return result.get_counts()