import requests
import os
from collections import defaultdict

API_URL = "https://api-inference.huggingface.co/models/mixtralai/Mixtral-8x7B-Instruct-v0.1"
HEADERS = {"Authorization": "Bearer your_token_HF", "Content-Type": "application/json"}

def generate_code(prompt):
    payload = {"inputs": prompt, "parameters": {"max_length": 500}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()[0]["generated_text"].strip()

def auto_generate_files(core_dir="../core", user_dir="user_files"):
    os.makedirs(user_dir, exist_ok=True)
    existing_files = defaultdict(list)
    for dir_path in [core_dir, user_dir]:
        for file in os.listdir(dir_path):
            with open(os.path.join(dir_path, file), "r") as f:
                existing_files[f.read()].append((dir_path, file))
    
    for content, files in existing_files.items():
        if len(files) > 1:
            summary = generate_code(f"Riassumi questo codice:\n{content}")
            with open(os.path.join(core_dir, f"summary_{files[0][1]}"), "w") as f:
                f.write(summary)
            for dir_path, file in files[1:]:
                os.remove(os.path.join(dir_path, file))
    
    new_code = generate_code("Crea un modulo Python per analisi dati avanzata")
    with open(os.path.join(core_dir, "advanced_analysis.py"), "w") as f:
        f.write(new_code)
