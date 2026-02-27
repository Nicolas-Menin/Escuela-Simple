from fastapi import APIRouter
from dao import cursos_dao
from schemas.cursos_schemas import CursoCrear, CursoMostar, CursoActualizar, CursoCombo


cursos = APIRouter(prefix="/cursos", tags=["Cursos"])
"""Router para gestionar las operaciones de cursos"""


@cursos.get("/", response_model=list[CursoMostar])
def listar_cursos():
    """Lista todos los cursos"""

    cursos_traer = cursos_dao.listar_cursos()

    return [
        {
            "id_curso": f[0],
            "grado": f[1],
            "division": f[2],
            "turno": f[3],
            "ciclo_lectivo": f[4],
        }
        for f in cursos_traer
    ]


@cursos.get("/combo", response_model=list[CursoCombo])
def listar_cursos_combo():
    """Lista cursos para mostrar en un combobox"""

    cursos_traer = cursos_dao.listar_cursos_combo()

    return [
        {
            "id_curso": f[0],
            "nombre": f[1],
        }
        for f in cursos_traer
    ]


@cursos.delete("/{id_curso}")
def eliminar_curso(id_curso: int):
    """Elimina un curso por su id"""

    cursos_dao.eliminar_curso(id_curso)

    return {"ok": True, "id_eliminado": id_curso}


@cursos.post("/")
def guardar_curso(curso: CursoCrear):
    """Guarda un nuevo curso"""

    curso_nuevo = cursos_dao.crear_curso(
        grado=curso.grado,
        division=curso.division,
        turno=curso.turno,
        ciclo_lectivo=curso.ciclo_lectivo,
    )

    return curso_nuevo


@cursos.put("/{id_curso}", response_model=CursoMostar)
def actualizar_curso(curso: CursoActualizar, id_curso: int):
    """Actualiza los datos de un curso"""

    return cursos_dao.actualizar_curso(
        id_curso=id_curso,
        grado=curso.grado,
        division=curso.division,
        turno=curso.turno,
        ciclo_lectivo=curso.ciclo_lectivo,
    )