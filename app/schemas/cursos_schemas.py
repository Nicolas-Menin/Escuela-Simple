from pydantic import BaseModel


class CursoCrear(BaseModel):
    """Modelo para crear un curso"""
    grado: str
    division: str
    turno: str
    ciclo_lectivo: str


class CursoMostar(BaseModel):
    """Modelo para mostrar un curso"""
    id_curso: int
    grado: str
    division: str
    turno: str
    ciclo_lectivo: str


class CursoActualizar(BaseModel):
    """Modelo para actualizar un curso"""
    grado: str
    division: str
    turno: str
    ciclo_lectivo: str


class CursoCombo(BaseModel):
    """Modelo para listar cursos en un combobox"""
    id_curso: int
    nombre: str