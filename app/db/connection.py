
import sqlite3 as sql
import os


def conectar_bd():
    """Conectamos la base de datos"""

    os.makedirs("app/data",exist_ok=True)
    return sql.connect("app/data/escuela.db")
