import numpy as np
from scipy import stats
import pandas as pd

class DataAnalyzer:
    @staticmethod
    def analyze_quantum_results(counts):
        """Analisi statistica dei risultati quantistici"""
        states = list(counts.keys())
        values = list(counts.values())
        total = sum(values)
        
        return {
            'entropy': stats.entropy(values, base=2),
            'uniformity': stats.chisquare(values).pvalue,
            'dominant_state': states[np.argmax(values)],
            'dominance_ratio': max(values) / total
        }

    @staticmethod
    def time_series_analysis(data):
        """Analisi di serie temporali per simulazioni"""
        df = pd.DataFrame(data)
        return {
            'autocorrelation': df.autocorr().to_dict(),
            'fft_analysis': np.abs(np.fft.fft(df.values)).tolist()
        }
