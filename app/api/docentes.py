from fastapi import APIRouter
from dao import docentes_dao
from schemas.docentes_schemas import DocenteCrear, DocenteMostar, DocenteActualizar, DocenteCombo


docentes = APIRouter(prefix="/docentes", tags=["Docente"])
"""Router para gestionar las operaciones de docentes"""


@docentes.get("/", response_model=list[DocenteMostar])
def listar_docentes():
    """Lista todos los docentes"""

    docentes_traer = docentes_dao.listar_docentes()
    return [
        {
            "id_docente": f[0],
            "nombre": f[1],
            "apellido": f[2],
            "dni": f[3],
            "profesion": f[4],
            "correo": f[5],
        }
        for f in docentes_traer
    ]


@docentes.get("/combo", response_model=list[DocenteCombo])
def listar_docentes_combo():
    """Lista docentes para mostrar en un combobox"""

    docentes_traer = docentes_dao.listar_docentes_combo()
    return [
        {
            "id_docente": f[0],
            "nombre": f[1],
        }
        for f in docentes_traer
    ]


@docentes.delete("/{id_docente}")
def eliminar_docente(id_docente: int):
    """Elimina un docente por su id"""

    docentes_dao.eliminar_docente(id_docente)
    return {"ok": True, "docente_eliminado": id_docente}


@docentes.post("/")
def guardar_docente(docente: DocenteCrear):
    """Guarda un nuevo docente"""

    docente_nuevo = docentes_dao.crear_docente(
        nombre=docente.nombre,
        apellido=docente.apellido,
        dni=docente.dni,
        profesion=docente.profesion,
        correo=docente.correo,
    )

    return docente_nuevo


@docentes.put("/{id_docente}", response_model=DocenteMostar)
def actualizar_docente(id_docente: int, docente: DocenteActualizar):
    """Actualiza los datos de un docente"""

    return docentes_dao.actualizar_docente(
        id_docente=id_docente,
        nombre=docente.nombre,
        apellido=docente.apellido,
        dni=docente.dni,
        profesion=docente.profesion,
        correo=docente.correo,
    )