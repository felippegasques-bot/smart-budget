import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect("gastos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        valor REAL,
        categoria TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()

def adicionar_gasto(descricao, valor, categoria):
    conn = conectar()
    cursor = conn.cursor()

    data = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    INSERT INTO gastos (descricao, valor, categoria, data)
    VALUES (?, ?, ?, ?)
    """, (descricao, valor, categoria, data))

    conn.commit()
    conn.close()

def listar_gastos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gastos")
    dados = cursor.fetchall()

    conn.close()
    return dados