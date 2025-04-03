from transformers import pipeline
from typing import Dict, Any
import warnings

class AIModelHub:
    def __init__(self):
        self.models = {
            'quantum_opt': pipeline('text-generation', model='mistralai/Mixtral-8x7B-Instruct-v0.1'),
            'math_solver': pipeline('text2text-generation', model='google/flan-t5-large')
        }
    
    def optimize_quantum_circuit(self, circuit_code: str) -> Dict[str, Any]:
        prompt = f"Ottimizza questo circuito quantistico:\n{circuit_code}"
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = self.models['quantum_opt'](prompt, max_length=500)
        return {'optimized': result[0]['generated_text']}

    def solve_math_expression(self, expression: str) -> Dict[str, Any]:
        result = self.models['math_solver'](expression)
        return {'solution': result[0]['generated_text']}
