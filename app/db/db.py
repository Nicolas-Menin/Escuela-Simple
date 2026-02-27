from db.connection import conectar_bd

def creacion_tablas():
    """Creacion de todas las tablas"""
    creacion_tabla_alumnos()
    creacion_tabla_docentes()
    creacion_tabla_materias()
    creacion_tabla_cursos()
    creacion_tabla_inscripciones()
    creacion_tabla_curso_materia()

def creacion_tabla_alumnos():
    """Creacion de tabla alumnos"""
    conn = conectar_bd()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""

                   CREATE TABLE IF NOT EXISTS alumnos(
                       id_alumno INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       apellido TEXT NOT NULL,
                       dni TEXT NOT NULL,
                       correo TEXT NOT NULL UNIQUE
                   )

                   """)

    conn.commit()
    conn.close()

def creacion_tabla_docentes():
    """Creacion de tabla docentes"""
    conn = conectar_bd()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()


    cursor.execute("""

                   CREATE TABLE IF NOT EXISTS docentes(
                       id_docente INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       apellido TEXT NOT NULL,
                       dni TEXT NOT NULL,
                       profesion TEXT NOT NULL,
                       correo TEXT NOT NULL UNIQUE
                   )

                   """)

    conn.commit()
    conn.close()


def creacion_tabla_materias():
    """Creacion de tabla materias"""
    conn = conectar_bd()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""

                    CREATE TABLE IF NOT EXISTS materias(
                        id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        carga_horaria INTEGER NOT NULL



                    )





                   """)

    conn.commit()
    conn.close()




def creacion_tabla_cursos():
    """Creacion de tabla cursos"""
    conn = conectar_bd()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""

                   CREATE TABLE IF NOT EXISTS cursos(
                       id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                       grado TEXT NOT NULL,
                       division TEXT NOT NULL,
                       turno TEXT NOT NULL,
                       ciclo_lectivo TEXT NOT NULL



                   )



                   """)

    conn.commit()
    conn.close()

def creacion_tabla_inscripciones():
    """Creacion de tabla inscripciones"""
    conn = conectar_bd()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    cursor.execute("""


                   CREATE TABLE IF NOT EXISTS inscripciones(
                       id_inscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
                       id_alumno INTEGER NOT NULL,
                       id_curso INTEGER NOT NULL,
                       fecha_inscripcion TEXT NOT NULL,
                       FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno),
                       FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)




                   )



                   """)

    conn.commit()
    conn.close()

def creacion_tabla_curso_materia():
    """Creacion de tabla curso_materia"""
    conn = conectar_bd()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""

                    CREATE TABLE IF NOT EXISTS cursos_materias(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_materia INTEGER NOT NULL,
                        id_docente INTEGER NOT NULL,
                        id_curso INTEGER NOT NULL,
                        FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
                        FOREIGN KEY (id_materia) REFERENCES materias(id_materia),
                        FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)


                    )




                   """)

    conn.commit()
    conn.close()