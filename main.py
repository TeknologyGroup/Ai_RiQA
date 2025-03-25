import subprocess
import webbrowser

def start_app():
    """Avvia il server backend e apre il frontend nel browser."""
    subprocess.Popen(["python", "-m", "uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"])
    webbrowser.open("http://localhost:8000/index.html")

if __name__ == "__main__":
    start_app()