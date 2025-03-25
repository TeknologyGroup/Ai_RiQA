from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from core import RIQACore
from backend.database import save_simulation
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
import os

app = FastAPI()
core = RIQACore()
app.mount("/static", StaticFiles(directory="../frontend/public"), name="static")

@app.post("/chat")
async def chat(message: str, client_id: str = "anonymous"):
    sim_type = "math" if "x" in message else "quantum" if "qubit" in message else "ballistic" if "v0" in message else "biological" if "tasso" in message else "astral"
    params = {"equation": message} if sim_type == "math" else {"initial_velocity": [20, 20]} if sim_type == "ballistic" else {"n_qubits": 2} if sim_type == "quantum" else {"rate": 0.1} if sim_type == "biological" else {"radius": 1.0}
    result = core.run_simulation(sim_type, params)
    save_simulation(sim_type, params, result)
    return {"result": result, "client_id": client_id}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    if file.filename.endswith(('.jpg', '.png')):
        img = Image.open(file.file)
        text = pytesseract.image_to_string(img)
        return await chat(text)
    return {"filename": file.filename, "result": "Formato non supportato"}

@app.get("/graph/{sim_type}")
async def get_graph(sim_type: str):
    result = core.run_simulation(sim_type, {})
    plt.plot(result.get("time", range(len(result))), result.get("position", list(result.values())[0]))
    plt.savefig("graph.png")
    return FileResponse("graph.png")

@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_json()
    result = core.run_simulation(data["type"], data["params"])
    await websocket.send_json(result)
    await websocket.close()