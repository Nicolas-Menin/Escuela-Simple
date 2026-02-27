import sqlite3 as sql
from db.db import conectar_bd




def crear_materias(nombre: str, carga_horaria: int):
    """Crear materia"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       INSERT INTO materias(nombre,carga_horaria) VALUES
                       (?,?)



                       """,(nombre,carga_horaria))


        conn.commit()

        id_materia = cursor.lastrowid

        return {
            "id_materia": id_materia,
            "nombre": nombre,
            "carga_horaria": carga_horaria
        }

    except sql.Error as e:

        raise ValueError(f"No se ha podido crear la materia, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def eliminar_materia(id_materia: int):
    """Eliminar materia"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       DELETE FROM materias
                       WHERE id_materia = ?




                       """,(id_materia,))
        conn.commit()
    except sql.Error as e:

        raise ValueError(f"No se ha podido eliminar la materia, error: {e}") from e


def actualizar_materia(id_materia: int,nombre: str, carga_horaria: int):
    """Actualizar Materia"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       UPDATE materias
                       SET nombre = ?, carga_horaria = ?
                       WHERE id_materia = ?


                       """,(nombre,carga_horaria,id_materia))

        conn.commit()

        cursor.execute("""

                       SELECT * FROM materias

                       WHERE id_materia = ?



                       """,(id_materia,))

        conn.commit()

        datos = cursor.fetchone()
        return datos

    except sql.Error as e:

        raise ValueError(f"No se ha podido actualizar los datos de la materia, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def listar_materias():
    """Listar materias"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       SELECT * FROM materias

                       ORDER BY id_materia ASC




                       """)

        conn.commit()

        return cursor.fetchall()

    except sql.Error as e:

        raise ValueError(f"No se ha podido listar las materias, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def listar_materias_combo():
    """Listar materias para combobox"""
    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       SELECT id_materia, nombre FROM materias



                       """)

        return cursor.fetchall()


    except sql.Error as e:
        raise ValueError(f"No se ha podido listar las materias para el combobox, error: {e}") from e
