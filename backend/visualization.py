import matplotlib.pyplot as plt
from io import BytesIO
import base64

class VisualizationEngine:
    @staticmethod
    def plot_quantum_circuit(circuit_text):
        """Genera immagine del circuito quantistico"""
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.text(0.5, 0.5, circuit_text, family='monospace', ha='center', va='center')
        ax.axis('off')
        return VisualizationEngine._fig_to_base64(fig)

    @staticmethod
    def plot_simulation_results(data):
        """Genera grafici per simulazioni"""
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))
        
        # Plot time series
        axs[0].plot(data['time'], data['values'])
        axs[0].set_title('Andamento Temporale')
        
        # Plot phase space
        if 'x' in data and 'y' in data:
            axs[1].plot(data['x'], data['y'])
            axs[1].set_title('Spazio delle Fasi')
        
        return VisualizationEngine._fig_to_base64(fig)

    @staticmethod
    def _fig_to_base64(fig):
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        plt.close(fig)
        return base64.b64encode(buf.getvalue()).decode('utf-8')
