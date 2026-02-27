from pydantic import BaseModel


class DocenteCrear(BaseModel):
    """Modelo para crear un docente"""
    nombre: str
    apellido: str
    dni: str
    profesion: str
    correo: str


class DocenteMostar(BaseModel):
    """Modelo para mostrar un docente"""
    id_docente: int
    nombre: str
    apellido: str
    dni: str
    profesion: str
    correo: str


class DocenteActualizar(BaseModel):
    """Modelo para actualizar un docente"""
    nombre: str
    apellido: str
    dni: str
    profesion: str
    correo: str


class DocenteCombo(BaseModel):
    """Modelo para listar docentes en un combobox"""
    id_docente: int
    nombre: str