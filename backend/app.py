"""
Backend FastAPI per RIQA Chatbot Interface con supporto per interfaccia grafica e connessioni remote.
"""

from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from core import RIQACore
from backend.database import save_simulation, get_connection
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
import asyncio
import os

app = FastAPI(title="RIQA Chatbot Server")
core = RIQACore()

# Monta i file statici per il frontend
app.mount("/static", StaticFiles(directory="../frontend/public"), name="static")

# Endpoint Chat per l'interfaccia
@app.post("/chat")
async def chat(message: str, client_id: str = "anonymous"):
    """
    Gestisce i messaggi della chat e avvia simulazioni basate sul contenuto.
    """
    sim_type = (
        "math" if "x" in message.lower() else
        "quantum" if "qubit" in message.lower() else
        "ballistic" if "v0" in message.lower() else
        "biological" if "tasso" in message.lower() else
        "astral"
    )
    params = (
        {"equation": message} if sim_type == "math" else
        {"initial_velocity": [20, 20]} if sim_type == "ballistic" else
        {"n_qubits": 2} if sim_type == "quantum" else
        {"rate": 0.1} if sim_type == "biological" else
        {"radius": 1.0}
    )
    result = core.run_simulation(sim_type, params)
    save_simulation(sim_type, params, result)
    return {"result": result, "client_id": client_id}

# Endpoint per caricamento file
@app.post("/upload")
async def upload_file(file: UploadFile = File(...), client_id: str = "anonymous"):
    """
    Carica file (immagini o PDF) ed elabora il contenuto per la chat.
    """
    content = await file.read()
    if file.filename.endswith(('.jpg', '.png')):
        img = Image.open(file.file)
        text = pytesseract.image_to_string(img)
        return await chat(text, client_id)
    return {"filename": file.filename, "result": "Formato non supportato"}

# Endpoint per generare grafici
@app.get("/graph/{sim_type}")
async def get_graph(sim_type: str):
    """
    Genera un grafico PNG basato sui risultati della simulazione.
    """
    result = core.run_simulation(sim_type, {})
    plt.plot(
        result.get("time", range(len(result))),
        result.get("position", list(result.values())[0]),
        color="#4299E1"
    )
    plt.savefig("graph.png")
    return FileResponse("graph.png")

# WebSocket per chat in tempo reale
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    """
    Stream dei risultati della chat in tempo reale.
    """
    await websocket.accept()
    data = await websocket.receive_json()
    sim_type = data.get("type", "math")
    params = data.get("params", {})
    client_id = data.get("client_id", "anonymous")
    result = core.run_simulation(sim_type, params)
    
    if isinstance(result, dict):
        for key, values in result.items():
            for i, value in enumerate(values):
                await websocket.send_json({"step": i, "key": key, "value": value, "client_id": client_id})
                await asyncio.sleep(0.1)
    else:
        await websocket.send_json({"result": result, "client_id": client_id})
    await websocket.close()

# Endpoint per simulazioni remote
@app.post("/simulate")
async def run_simulation(sim_type: str, params: dict, client_id: str = "anonymous"):
    """
    Esegue una simulazione remota e salva i risultati nel database.
    """
    result = core.run_simulation(sim_type, params)
    save_simulation(sim_type, params, result)
    return {"result": result, "client_id": client_id}

# WebSocket per simulazioni remote in streaming
@app.websocket("/ws/simulation")
async def websocket_simulation(websocket: WebSocket):
    """
    Stream dei risultati delle simulazioni remote in tempo reale.
    """
    await websocket.accept()
    data = await websocket.receive_json()
    sim_type = data.get("type", "math")
    params = data.get("params", {})
    client_id = data.get("client_id", "anonymous")
    result = core.run_simulation(sim_type, params)
    
    if isinstance(result, dict):
        for key, values in result.items():
            for i, value in enumerate(values):
                await websocket.send_json({"step": i, "key": key, "value": value, "client_id": client_id})
                await asyncio.sleep(0.1)
    else:
        await websocket.send_json({"result": result, "client_id": client_id})
    await websocket.close()

# Endpoint per risultati condivisi
@app.get("/shared_results")
async def get_shared_results():
    """
    Restituisce i risultati condivisi dagli utenti dal database.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT type, parameters, result FROM experiments")
    results = cur.fetchall()
    conn.close()
    return [{"type": r[0], "params": r[1], "result": r[2]} for r in results]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)