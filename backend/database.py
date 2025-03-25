import sqlite3  # Usiamo SQLite per semplicità

def get_connection():
    return sqlite3.connect("riqa.db")

def save_simulation(sim_type, params, result):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO experiments (type, parameters, result) VALUES (?, ?, ?)", (sim_type, str(params), str(result)))
    conn.commit()
    conn.close()

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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