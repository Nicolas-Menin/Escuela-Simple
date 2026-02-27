import sqlite3 as sql
from db.db import conectar_bd





def crear_curso_materia(id_materia: int, id_docente: int, id_curso: int):
    """Crear curso_materia"""

    conn = conectar_bd()
    cursor = conn.cursor()


    try:

        cursor.execute("""

                       INSERT INTO cursos_materias(id_materia,id_docente,id_curso) VALUES
                       (?,?,?)


                       """,(id_materia,id_docente,id_curso))


        conn.commit()

        return cursor.lastrowid

    except sql.Error as e:
        raise ValueError(f"No se ha podido crear el curso_materia, error: {e}") from e
    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def eliminar_curso_materia(id_curso_materia: int):
    """Eliminar curso_materia"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       DELETE FROM cursos_materias
                       WHERE id = ?


                       """,(id_curso_materia,))

        conn.commit()

    except sql.Error as e:
        raise ValueError(f"No se ha podido eliminar el curso_materia, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def actualizar_curso_materia(id_curso_materia: int, id_materia: int, id_docente: int, id_curso: int):
    """Actualizar curso_materia"""

    conn = conectar_bd()
    cursor = conn.cursor()

    try:

        cursor.execute("""

                       UPDATE cursos_materias
                       SET id_materia = ?, id_docente = ?, id_curso = ?
                       WHERE id = ?


                       """,(id_materia,id_docente,id_curso,id_curso_materia))

        conn.commit()

        cursor.execute("""

                       SELECT cm.id, m.id_materia, d.id_docente,c.id_curso,
                        m.nombre, d.nombre || " " || d.apellido AS docente,c.grado || " " || c.division || " " || c.turno AS curso,


                        FROM cursos_materias AS cm

                        INNER JOIN materias AS m ON cm.id_materia = m.id_materia
                        INNER JOIN docentes AS d ON cm.id_docente = d.id_docente
                        INNER JOIN cursos AS c ON cm.id_curso = c.id_curso

                        WHERE cm.id = ?
                       """,(id_curso_materia,))

        return cursor.fetchone()

    except sql.Error as e:
        raise ValueError(f"No se ha podido actualizar el curso_materia, error: {e}") from e


    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def listar_cursos_materias():
    """Listas cursos_mataerias"""

    conn = conectar_bd()
    cursor = conn.cursor()


    try:

        cursor.execute("""

                       SELECT cm.id, m.id_materia, d.id_docente,c.id_curso,
                        m.nombre, d.nombre || " " || d.apellido AS docente,c.grado || " " || c.division || " " || c.turno AS curso

                        FROM cursos_materias AS cm

                        INNER JOIN materias AS m ON cm.id_materia = m.id_materia
                        INNER JOIN docentes AS d ON cm.id_docente = d.id_docente
                        INNER JOIN cursos AS c ON cm.id_curso = c.id_curso

                       """)



        return cursor.fetchall()

    except sql.Error as e:
        raise ValueError(f"No se ha podido listar cursos_materias, error: {e}") from e

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

