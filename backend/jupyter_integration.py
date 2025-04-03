import nbformat
from nbconvert import PythonExporter
import io

class NotebookIntegrator:
    @staticmethod
    def create_notebook(experiment_data):
        notebook = nbformat.v4.new_notebook()
        
        # Aggiungi celle con i dati dell'esperimento
        notebook.cells.append(nbformat.v4.new_code_cell(
            f"# RIQA Experiment: {experiment_data['type']}\n"
            f"session_id = '{experiment_data['session_id']}'"
        ))
        
        # Aggiungi analisi automatica
        notebook.cells.append(nbformat.v4.new_code_cell(
            "from riqa_analysis import analyze_results\n"
            f"results = analyze_results({experiment_data['results']})"
        ))
        
        return notebook
    
    @staticmethod
    def export_to_python(notebook):
        exporter = PythonExporter()
        body, _ = exporter.from_notebook_node(notebook)
        return body
