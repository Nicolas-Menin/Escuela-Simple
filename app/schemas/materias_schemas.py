from pydantic import BaseModel


class MateriaCrear(BaseModel):
    """Modelo para crear una materia"""
    nombre: str
    carga_horaria: int


class MateriaMostrar(BaseModel):
    """Modelo para mostrar una materia"""
    id_materia: int
    nombre: str
    carga_horaria: int


class MateriaActualizar(BaseModel):
    """Modelo para actualizar una materia"""
    nombre: str
    carga_horaria: int


class MateriaCombo(BaseModel):
    """Modelo para listar materias en un combobox"""
    id_materia: int
    nombre: str