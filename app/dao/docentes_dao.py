import sqlite3 as sql
from db.db import conectar_bd






def crear_docente(nombre: str, apellido: str, dni: str, profesion: str, correo: str):
    """Crear docente"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       INSERT INTO docentes(nombre,apellido,dni,profesion,correo) VALUES
                       (?,?,?,?,?)



                       """,(nombre,apellido,dni,profesion,correo))

        conn.commit()

        id_docente = cursor.lastrowid

        return {
            "id_docente": id_docente,
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "profesion": profesion,
            "correo": correo


        }

    except sql.Error as e:
        raise ValueError(f"No se ha podido crear el docente, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def eliminar_docente(id_docente: int):
    """Eliminar docente"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       DELETE FROM docentes
                       WHERE id_docente = ?




                       """,(id_docente,))

        conn.commit()

    except sql.Error as e:
        raise ValueError(f"No se ha podido eliminar el docente, error: {e}") from e
    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def actualizar_docente(id_docente: int,nombre: str,apellido: str,dni:str,profesion:str,correo: str):
    """Actualizar docente"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                        UPDATE docentes
                        SET nombre = ?, apellido = ?, dni = ?, profesion = ?, correo = ?
                        WHERE id_docente = ?


                       """,(nombre,apellido,dni,profesion,correo,id_docente))

        conn.commit()

        cursor.execute("""

                       SELECT * FROM docentes
                       WHERE id_docente = ?


                       """,(id_docente,))

        fila = cursor.fetchone()

        return {
            "id_docente": fila[0],
            "nombre": fila[1],
            "apellido":fila[2],
            "dni": fila[3],
            "profesion": fila[4],
            "correo": fila[5]
        }

    except sql.Error as e:
        raise ValueError(f"No se ha podido actualizar los datos del docente, error: {e}") from e
    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def listar_docentes():
    """Listar alumnos"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                        SELECT * FROM docentes

                        ORDER BY id_docente ASC




                       """)


        return cursor.fetchall()

    except sql.Error as e:
        raise ValueError(f"No se ha podido listar a los docentes, error: {e}") from e
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


def listar_docentes_combo():
    """Listar docentes para combobox"""
    conn = conectar_bd()
    cursor = conn.cursor()


    try:

        cursor.execute("""

                       SELECT id_docente, nombre || " " || apellido AS docente
                       FROM docentes




                       """)

        return cursor.fetchall()

    except sql.Error as e:
        raise ValueError(f"No se ha podido listar a los docentes, error: {e}") from e


    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()