import sqlite3 as sq
import os

DB_FILE = "web_traffic.db"
SCHEMA_FILE = "schema.sql"

def init_db():
    if not os.path.exists(DB_FILE):
        print(f"ERROR: Connot find '{SCHEMA_FILE}'. ensure you are running this from the root directory")
        return
    conn = sq.connect(DB_FILE)
    cousor = conn.cursor()

    with open(SCHEMA_FILE, 'r') as f:
        schema_script = f.read()

    cousor.executescript(schema_script)
    conn.commit()
    conn.close()

    print(f"DATABASE: '{DB_FILE}' initialized successfully with schema from '{SCHEMA_FILE}'.")


if __name__ == "__main__":
    init_db()