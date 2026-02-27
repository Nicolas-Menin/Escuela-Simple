from fastapi import APIRouter
from dao import alumnos_dao
from schemas.alumnos_schemas import AlumnoCrear, AlumnoMostrar, AlumnoActualizar, AlumnoCombo


alumnos = APIRouter(prefix="/alumnos", tags=["Alumnos"])
"""Router para gestionar las operaciones de alumnos"""


@alumnos.get("/", response_model=list[AlumnoMostrar])
def listar_alumnos():
    """Lista todos los alumnos"""

    traer_alumnos = alumnos_dao.listar_alumnos()
    return [
        {
            "id_alumno": f[0],
            "nombre": f[1],
            "apellido": f[2],
            "dni": f[3],
            "correo": f[4],
        }
        for f in traer_alumnos
    ]


@alumnos.delete("/{id_alumno}")
def eliminar_alumno(id_alumno: int):
    """Elimina un alumno por su id"""

    alumnos_dao.eliminar_alumno(id_alumno)
    return {"ok": True, "id_eliminado": id_alumno}


@alumnos.post("/")
def guardar_alumno(alumno: AlumnoCrear):
    """Guarda un nuevo alumno"""

    nuevo_alumno = alumnos_dao.crear_alumno(
        nombre=alumno.nombre,
        apellido=alumno.apellido,
        dni=alumno.dni,
        correo=alumno.correo,
    )

    return nuevo_alumno


@alumnos.put("/{id_alumno}", response_model=AlumnoMostrar)
def actualizar_alumno(id_alumno: int, alumno: AlumnoActualizar):
    """Actualiza los datos de un alumno"""

    return alumnos_dao.actualizar_alumno(
        id_alumno=id_alumno,
        nombre=alumno.nombre,
        apellido=alumno.apellido,
        dni=alumno.dni,
        correo=alumno.correo,
    )


@alumnos.get("/combo", response_model=list[AlumnoCombo])
def listar_alumnos_combo():
    """Lista alumnos para mostrar en un combobox"""

    alumnos_combo = alumnos_dao.listar_alumnos_combo()

    return [
        {
            "id_alumno": f[0],
            "nombre": f[1],
        }
        for f in alumnos_combo
    ]