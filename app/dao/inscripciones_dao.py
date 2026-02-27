import sqlite3 as sql
from db.db import conectar_bd





def crear_inscripciones(id_alumno: int, id_curso: int, fecha_inscripcion: str):
    """Crear inscripcion"""

    conn = conectar_bd()
    cursor = conn.cursor()


    try:


        cursor.execute("""

                       INSERT INTO inscripciones(id_alumno,id_curso,fecha_inscripcion) VALUES
                       (?,?,?)




                       """,(id_alumno,id_curso,fecha_inscripcion))

        conn.commit()

        return cursor.lastrowid

    except sql.Error as e:
        raise ValueError(f"No se ha podido crear la inscripcion, error: {e}") from e
    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def eliminar_inscripciones(id_inscripcion: int):
    """Eliminar inscripcion"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       DELETE FROM inscripciones
                       WHERE id_inscripcion = ?




                       """,(id_inscripcion,))


        conn.commit()

    except sql.Error as e:
        raise ValueError(f"No se ha  podido eliminar la inscripcion, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def actualizar_inscripcion(id_inscripcion: int,id_alumno: int, id_curso: int, fecha_inscripcion: str):
    """Actualizar Inscripcion"""
    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       UPDATE inscripciones
                       SET id_alumno = ?, id_curso = ?, fecha_inscripcion = ?
                       WHERE id_inscripcion = ?;

                       """,(id_alumno,id_curso,fecha_inscripcion,id_inscripcion))


        conn.commit()

        cursor.execute("""

                       SELECT i.id_inscripcion,a.id_alumno,c.id_curso, a.nombre || " " || a.apellido AS alumno,
                       c.grado || " " || c.division || " " || c.turno AS curso, i.fecha_inscripcion
                       FROM inscripciones AS i

                       INNER JOIN alumnos AS a ON i.id_alumno = a.id_alumno
                       INNER JOIN cursos AS c ON i.id_curso = c.id_curso

                        WHERE id_inscripcion = ?



                       """,(id_inscripcion,))

        return cursor.fetchone()

    except sql.Error as e:

        raise ValueError(f"No se ha podido actualizar la inscripcion,error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def listar_inscripcion():
    """Listar Inscripciones"""
    conn = conectar_bd()
    cursor = conn.cursor()

    try:


        cursor.execute("""

                       SELECT i.id_inscripcion,a.id_alumno,c.id_curso, a.nombre || " " || a.apellido AS alumno,
                       c.grado || " " || c.division || " " || c.turno AS curso, i.fecha_inscripcion
                       FROM inscripciones AS i

                       INNER JOIN alumnos AS a ON i.id_alumno = a.id_alumno
                       INNER JOIN cursos AS c ON i.id_curso = c.id_curso

                       """)

        return cursor.fetchall()

    except sql.Error as e:

        raise ValueError(f"No se ha podido listar las inscripciones,error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()
