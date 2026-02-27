from fastapi import APIRouter
from dao import inscripciones_dao
from schemas.inscripciones_schemas import InscripcionesCrear, InscripcionMostrar, InscripcionActualizar


inscripciones = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])
"""Router para gestionar las operaciones de inscripciones"""


@inscripciones.get("/", response_model=list[InscripcionMostrar])
def listar_inscripciones():
    """Lista todas las inscripciones"""

    inscripciones_traer = inscripciones_dao.listar_inscripcion()

    return [
        {
            "id_inscripcion": f[0],
            "id_alumno": f[1],
            "id_curso": f[2],
            "alumno": f[3],
            "curso": f[4],
            "fecha_inscripcion": f[5],
        }
        for f in inscripciones_traer
    ]


@inscripciones.post("/")
def guardar_inscripcion(inscripcion: InscripcionesCrear):
    """Guarda una nueva inscripción"""

    id_inscripcion = inscripciones_dao.crear_inscripciones(
        id_alumno=inscripcion.id_alumno,
        id_curso=inscripcion.id_curso,
        fecha_inscripcion=inscripcion.fecha_inscripcion,
    )

    return {"id_inscripcion": id_inscripcion}


@inscripciones.delete("/{id_inscripcion}")
def eliminar_inscripcion(id_inscripcion: int):
    """Elimina una inscripción por su id"""

    inscripciones_dao.eliminar_inscripciones(id_inscripcion)


@inscripciones.put("/{id_inscripcion}", response_model=InscripcionMostrar)
def actualizar_inscripcion(inscripcion: InscripcionActualizar, id_inscripcion: int):
    """Actualiza los datos de una inscripción"""

    inscripcion_actualizar = inscripciones_dao.actualizar_inscripcion(
        id_inscripcion=id_inscripcion,
        id_alumno=inscripcion.id_alumno,
        id_curso=inscripcion.id_curso,
        fecha_inscripcion=inscripcion.fecha_inscripcion,
    )

    return {
        "id_inscripcion": inscripcion_actualizar[0],
        "id_alumno": inscripcion_actualizar[1],
        "id_curso": inscripcion_actualizar[2],
        "alumno": inscripcion_actualizar[3],
        "curso": inscripcion_actualizar[4],
        "fecha_inscripcion": inscripcion_actualizar[5],
    }