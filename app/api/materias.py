from fastapi import APIRouter
from dao import materias_dao
from schemas.materias_schemas import MateriaCrear, MateriaMostrar, MateriaActualizar, MateriaCombo


materias = APIRouter(prefix="/materias", tags=["Materias"])
"""Router para gestionar las operaciones de materias"""


@materias.get("/", response_model=list[MateriaMostrar])
def listar_materias():
    """Lista todas las materias"""

    materias_traer = materias_dao.listar_materias()

    return [
        {
            "id_materia": f[0],
            "nombre": f[1],
            "carga_horaria": f[2],
        }
        for f in materias_traer
    ]


@materias.get("/combo", response_model=list[MateriaCombo])
def listar_materias_combo():
    """Lista materias para mostrar en un combobox"""

    materias_traer = materias_dao.listar_materias_combo()

    return [
        {
            "id_materia": f[0],
            "nombre": f[1],
        }
        for f in materias_traer
    ]


@materias.delete("/{id_materia}")
def eliminar_materia(id_materia: int):
    """Elimina una materia por su id"""

    materias_dao.eliminar_materia(id_materia)

    return {"ok": True, "id_eliminado": id_materia}


@materias.post("/", response_model=MateriaMostrar)
def guardar_materia(materia: MateriaCrear):
    """Guarda una nueva materia"""

    materia_nueva = materias_dao.crear_materias(
        nombre=materia.nombre,
        carga_horaria=materia.carga_horaria,
    )

    return {
        "id_materia": materia_nueva["id_materia"],
        "nombre": materia_nueva["nombre"],
        "carga_horaria": materia_nueva["carga_horaria"],
    }


@materias.put("/{id_materia}", response_model=MateriaMostrar)
def actualizar_materia(id_materia: int, materia: MateriaActualizar):
    """Actualiza los datos de una materia"""

    datos = materias_dao.actualizar_materia(
        id_materia=id_materia,
        nombre=materia.nombre,
        carga_horaria=materia.carga_horaria,
    )

    return {
        "id_materia": datos[0],
        "nombre": datos[1],
        "carga_horaria": datos[2],
    }