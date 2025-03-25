"""
Client per connettersi al server RIQA_Advanced.
"""

import requests
import websocket
import json
import uuid

SERVER_URL = "http://[TUO_SERVER_IP]:8000"  # Sostituisci con l'IP del server
CLIENT_ID = str(uuid.uuid4())

def run_remote_simulation(sim_type, params):
    """Esegue una simulazione remota."""
    response = requests.post(
        f"{SERVER_URL}/simulate",
        json={"sim_type": sim_type, "params": params, "client_id": CLIENT_ID}
    )
    return response.json()

def stream_simulation(sim_type, params):
    """Stream dei risultati in tempo reale."""
    ws = websocket.WebSocket()
    ws.connect(f"ws://{SERVER_URL.split('//')[1]}/ws/simulation")
    ws.send(json.dumps({"type": sim_type, "params": params, "client_id": CLIENT_ID}))
    
    while True:
        try:
            message = ws.recv()
            print(json.loads(message))
        except:
            break
    ws.close()

if __name__ == "__main__":
    # Test simulazione remota
    result = run_remote_simulation("math", {"equation": "harmonic"})
    print("Risultato Remoto:", result)
    
    # Test streaming
    print("Streaming simulazione quantistica:")
    stream_simulation("quantum", {"n_qubits": 2})