from pydantic import BaseModel


class InscripcionesCrear(BaseModel):
    """Modelo para crear una inscripción"""
    id_alumno: int
    id_curso: int
    fecha_inscripcion: str


class InscripcionActualizar(BaseModel):
    """Modelo para actualizar una inscripción"""
    id_alumno: int
    id_curso: int
    fecha_inscripcion: str


class InscripcionMostrar(BaseModel):
    """Modelo para mostrar una inscripción"""
    id_inscripcion: int
    id_alumno: int
    id_curso: int
    alumno: str
    curso: str
    fecha_inscripcion: str