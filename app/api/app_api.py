from fastapi import FastAPI
from api.alumnos import alumnos
from api.cursos_materias import cursos_materias
from api.cursos import cursos
from api.docentes import docentes
from api.inscripciones import inscripciones
from api.materias import materias



app = FastAPI(title="Sistema Escolar")


# Incluir Routers

app.include_router(alumnos)
app.include_router(cursos_materias)
app.include_router(cursos)
app.include_router(docentes)
app.include_router(inscripciones)
app.include_router(materias)
