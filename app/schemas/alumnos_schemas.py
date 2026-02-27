from pydantic import BaseModel


class AlumnoCrear(BaseModel):
    """Modelo para crear un alumno"""
    nombre: str
    apellido: str
    dni: str
    correo: str


class AlumnoMostrar(BaseModel):
    """Modelo para mostrar un alumno"""
    id_alumno: int
    nombre: str
    apellido: str
    dni: str
    correo: str


class AlumnoActualizar(BaseModel):
    """Modelo para actualizar un alumno"""
    nombre: str
    apellido: str
    dni: str
    correo: str


class AlumnoCombo(BaseModel):
    """Modelo para listar alumnos en un combobox"""
    id_alumno: int
    nombre: str