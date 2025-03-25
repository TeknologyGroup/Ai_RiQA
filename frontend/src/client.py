import requests
import websocket
import json
import uuid

SERVER_URL = "http://localhost:8000"
CLIENT_ID = str(uuid.uuid4())

def send_message(message):
    response = requests.post(f"{SERVER_URL}/chat", json={"message": message, "client_id": CLIENT_ID})
    return response.json()

if __name__ == "__main__":
    result = send_message("Risolvi x^2 - 4 = 0")
    print(result)