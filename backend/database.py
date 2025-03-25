"""
Modulo per la gestione del database per AI_RIQA.
Supporta SQLite e PostgreSQL in base alla configurazione.
"""

import os
import sqlite3
import psycopg2

# Configurazione del database
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlite")  # Default: SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "dbname=riqa user=postgres password=secret")  # Per PostgreSQL
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "riqa.db")  # Per SQLite

def get_connection():
    """
    Restituisce una connessione al database in base al tipo configurato.
    """
    if DATABASE_TYPE.lower() == "sqlite":
        return sqlite3.connect(SQLITE_DB_PATH)
    elif DATABASE_TYPE.lower() == "postgresql":
        return psycopg2.connect(DATABASE_URL)
    else:
        raise ValueError(f"Tipo di database '{DATABASE_TYPE}' non supportato. Usa 'sqlite' o 'postgresql'.")

def save_simulation(sim_type, params, result):
    """
    Salva i risultati di una simulazione nel database.
    Args:
        sim_type (str): Tipo di simulazione
        params (dict): Parametri della simulazione
        result (dict): Risultati della simulazione
    """
    conn = get_connection()
    cur = conn.cursor()
    query = "INSERT INTO experiments (type, parameters, result) VALUES (?, ?, ?)" if DATABASE_TYPE.lower() == "sqlite" else "INSERT INTO experiments (type, parameters, result) VALUES (%s, %s, %s)"
    cur.execute(query, (sim_type, str(params), str(result)))
    conn.commit()
    conn.close()

def init_db():
    """
    Inizializza il database creando la tabella experiments se non esiste.
    """
    conn = get_connection()
    cur = conn.cursor()
    if DATABASE_TYPE.lower() == "sqlite":
        cur.execute("""
            CREATE TABLE IF NOT EXISTS experiments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                parameters TEXT,
                result TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    elif DATABASE_TYPE.lower() == "postgresql":
        cur.execute("""
            CREATE TABLE IF NOT EXISTS experiments (
                id SERIAL PRIMARY KEY,
                type TEXT NOT NULL,
                parameters TEXT,
                result TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database inizializzato con {DATABASE_TYPE}")