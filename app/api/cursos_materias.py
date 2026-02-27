from fastapi import APIRouter
from dao import cursos_materia_dao
from schemas.cursos_materias_schemas import CursoMateriaCrear, CursoMateriaMostrar, CursoMateriaActualizar


cursos_materias = APIRouter(prefix="/curso_materia", tags=["Curso_Materia"])
"""Router para gestionar la relación entre cursos, materias y docentes"""


@cursos_materias.delete("/{id_curso_materia}")
def eliminar_curso_materia(id_curso_materia: int):
    """Elimina una asignación de curso y materia por su id"""

    cursos_materia_dao.eliminar_curso_materia(id_curso_materia)
    return {"ok": True, "id_eliminado": id_curso_materia}


@cursos_materias.post("/")
def guardar_curso_materia(curso_materia: CursoMateriaCrear):
    """Guarda una nueva asignación de curso, materia y docente"""

    id_curso_materia = cursos_materia_dao.crear_curso_materia(
        id_materia=curso_materia.id_materia,
        id_docente=curso_materia.id_docente,
        id_curso=curso_materia.id_curso
    )

    return {"id_curso_materia": id_curso_materia}


@cursos_materias.put("/{id_curso_materia}", response_model=CursoMateriaMostrar)
def actualizar_curso_materia(curso_materia: CursoMateriaActualizar, id_curso_materia: int):
    """Actualiza una asignación de curso, materia y docente"""

    asignacion = cursos_materia_dao.actualizar_curso_materia(
        id_curso_materia,
        curso_materia.id_materia,
        curso_materia.id_docente,
        curso_materia.id_curso
    )

    return {
        "id_curso_materia": asignacion[0],
        "id_materia": asignacion[1],
        "id_docente": asignacion[2],
        "id_curso": asignacion[3],
        "nombre_materia": asignacion[4],
        "nombre_docente": asignacion[5],
        "nombre_curso": asignacion[6]
    }


@cursos_materias.get("/", response_model=list[CursoMateriaMostrar])
def listar_cursos_materias():
    """Lista todas las asignaciones de cursos y materias"""

    tabla = cursos_materia_dao.listar_cursos_materias()
    return [
        {
            "id_curso_materia": f[0],
            "id_materia": f[1],
            "id_docente": f[2],
            "id_curso": f[3],
            "nombre_materia": f[4],
            "nombre_docente": f[5],
            "nombre_curso": f[6]
        }
        for f in tabla
    ]