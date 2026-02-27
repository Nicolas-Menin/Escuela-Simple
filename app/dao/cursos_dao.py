import sqlite3 as sql
from db.db import conectar_bd




def crear_curso(grado: str, division: str, turno: str, ciclo_lectivo: str):
    """Crear curso"""


    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                        INSERT INTO cursos(grado,division,turno,ciclo_lectivo) VALUES
                        (?,?,?,?)



                       """,(grado,division,turno,ciclo_lectivo))

        conn.commit()
        id_curso = cursor.lastrowid
        return {
            "id_curso": id_curso,
            "grado": grado,
            "division": division,
            "turno": turno,
            "ciclo_lectivo": ciclo_lectivo
        }

    except sql.Error as e:
        raise ValueError(f"No se ha podido crear el curso, error: {e}") from e


    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def eliminar_curso(id_curso: int):
    """Eliminar curso"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       DELETE FROM cursos
                       WHERE id_curso = ?



                       """,(id_curso,))

        conn.commit()

    except sql.Error as e:
        raise ValueError(f"No se ha podido eliminar el curso, error: {e}") from e


    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def actualizar_curso(id_curso: int, grado: str, division: str, turno: str, ciclo_lectivo: str):
    """Actualizar datos de curso"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       UPDATE cursos
                       SET  grado = ?, division = ?, turno = ?, ciclo_lectivo = ?
                       WHERE id_curso = ?


                       """,(grado,division,turno,ciclo_lectivo,id_curso))

        conn.commit()

        cursor.execute("""


                       SELECT * FROM cursos

                       WHERE id_curso = ?



                       """,(id_curso,))

        datos = cursor.fetchone()

        return {
            "id_curso": datos[0],
            "grado": datos[1],
            "division": datos[2],
            "turno": datos[3],
            "ciclo_lectivo": datos[4]
        }

    except sql.Error as e:
        raise ValueError(f"No se ha podido actualizar los datos del curso, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def listar_cursos():
    """Listar cursos"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       SELECT * FROM cursos

                       ORDER BY id_curso ASC



                       """)

        conn.commit()

        return cursor.fetchall()

    except sql.Error as e:
        raise ValueError(f"No se a podido listar los cursos, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()



def listar_cursos_combo():
    """Listar cursos"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       SELECT id_curso,
                       grado || " " || division || " " || turno AS nombre
                       FROM cursos





                       """)


        return cursor.fetchall()

    except sql.Error as e:
        raise ValueError(f"No se a podido listar los cursos, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()