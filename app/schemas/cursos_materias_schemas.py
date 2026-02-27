from pydantic import BaseModel


class CursoMateriaCrear(BaseModel):
    """Modelo para crear una asignación de materia a curso"""
    id_materia: int
    id_docente: int
    id_curso: int


class CursoMateriaActualizar(BaseModel):
    """Modelo para actualizar una asignación de materia a curso"""
    id_materia: int
    id_docente: int
    id_curso: int


class CursoMateriaMostrar(BaseModel):
    """Modelo para mostrar una asignación de materia a curso"""
    id_curso_materia: int
    id_materia: int
    id_docente: int
    id_curso: int
    nombre_materia: str
    nombre_docente: str
    nombre_curso: str