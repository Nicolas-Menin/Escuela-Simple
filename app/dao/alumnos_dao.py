import sqlite3 as sql
from db.db import conectar_bd




def crear_alumno(nombre: str, apellido: str,dni: str, correo: str):
    """Creacion de alumno"""
    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       INSERT INTO alumnos(nombre,apellido,dni,correo) VALUES
                        (?,?,?,?)




                       """,(nombre,apellido,dni,correo))

        conn.commit()
        id_alumno = cursor.lastrowid

        return {
                "id_alumno": id_alumno,
                "nombre": nombre,
                "apellido": apellido,
                "dni": dni,
                "correo": correo
        }

    except sql.Error as e:
        raise ValueError(f"No se ha podido crear el alumno, error: {e}") from e

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def eliminar_alumno(id_alumno: int):
    """Eliminar alumno"""

    conn = conectar_bd()
    cursor = conn.cursor()


    try:


        cursor.execute("""

                       DELETE FROM alumnos
                       WHERE id_alumno = ?




                       """,(id_alumno,))

        conn.commit()

    except sql.Error as e:

        raise ValueError(f"No se ha podido eliminar el alumno, error: {e}") from e
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()



def actualizar_alumno(id_alumno: int, nombre: str, apellido: str,dni: str, correo: str):
    """Actualizar alumno"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       UPDATE alumnos
                       SET nombre = ?, apellido = ?, dni = ?, correo = ?
                       WHERE id_alumno = ?

                       """,(nombre,apellido,dni,correo,id_alumno))

        conn.commit()

        cursor.execute("""

                       SELECT * FROM alumnos
                       WHERE id_alumno = ?



                       """,(id_alumno,))

        fila = cursor.fetchone()

        return {
            "id_alumno": fila[0],
            "nombre": fila[1],
            "apellido":fila[2],
            "dni": fila[3],
            "correo": fila[4]
        }

    except sql.Error as e:

        raise ValueError(f"No se ha podido actualizar los datos del alumno, error: {e}") from e
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


def listar_alumnos():
    """Listar alumnos"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                        SELECT * FROM alumnos

                        ORDER BY id_alumno ASC



                       """)
        alumnos = cursor.fetchall()
        return alumnos

    except sql.Error as e:
        raise ValueError(f"No se a podido cargar los alumnos, error: {e}") from e

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


def listar_alumnos_combo():
    """Listar alumnos para combobox"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                        SELECT id_alumno, nombre || " " || apellido as alumno
                        FROM alumnos


                       """)
        return cursor.fetchall()

    except sql.Error as e:
        raise ValueError(f"No se a podido cargar los alumnos para el combobox, error: {e}") from e

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()