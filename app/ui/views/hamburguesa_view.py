import customtkinter as ctk
from ui.views.alumnos_view import FrameAlumnos
from ui.views.docentes_view import FrameDocente
from ui.views.materias_view import FrameMateria
from ui.views.cursos_view import FrameCurso
from ui.views.inscripciones_view import FrameInscripciones
from ui.views.cursos_materias_views import FrameCursoMateria


class FrameHamburguesa(ctk.CTkFrame):
    """Menú lateral que gestiona la navegación entre módulos."""

    def __init__(self, master):
        """Inicializa el menú y crea los frames principales."""
        super().__init__(master, width=200, height=800, fg_color="#3b3b3b")

        self.lista_frames = {
            "alumno": FrameAlumnos(master),
            "docente": FrameDocente(master),
            "materia": FrameMateria(master),
            "curso": FrameCurso(master),
            "curso_materia": FrameCursoMateria(master),
            "inscripciones": FrameInscripciones(master),
        }

        self.boton_alumnos = ctk.CTkButton(
            self,
            corner_radius=0,
            text="ALUMNOS",
            width=200,
            height=50,
            fg_color="#4d4d4d",
            hover_color="#2a2a2a",
            command=lambda: self.elegir_frame(self.lista_frames["alumno"])
        )
        self.boton_alumnos.place(x=0, y=100)

        self.boton_docentes = ctk.CTkButton(
            self,
            corner_radius=0,
            text="DOCENTES",
            width=200,
            height=50,
            fg_color="#4d4d4d",
            hover_color="#2a2a2a",
            command=lambda: self.elegir_frame(self.lista_frames["docente"])
        )
        self.boton_docentes.place(x=0, y=150)

        self.boton_materias = ctk.CTkButton(
            self,
            corner_radius=0,
            text="MATERIAS",
            width=200,
            height=50,
            fg_color="#4d4d4d",
            hover_color="#2a2a2a",
            command=lambda: self.elegir_frame(self.lista_frames["materia"])
        )
        self.boton_materias.place(x=0, y=200)

        self.boton_inscripciones = ctk.CTkButton(
            self,
            corner_radius=0,
            text="INSCRIPCIONES",
            width=200,
            height=50,
            fg_color="#4d4d4d",
            hover_color="#2a2a2a",
            command=lambda: self.elegir_frame(self.lista_frames["inscripciones"])
        )
        self.boton_inscripciones.place(x=0, y=250)

        self.boton_cursos = ctk.CTkButton(
            self,
            corner_radius=0,
            text="CURSOS",
            width=200,
            height=50,
            fg_color="#4d4d4d",
            hover_color="#2a2a2a",
            command=lambda: self.elegir_frame(self.lista_frames["curso"])
        )
        self.boton_cursos.place(x=0, y=300)

        self.boton_asignatura = ctk.CTkButton(
            self,
            corner_radius=0,
            text="ASIGNATURAS",
            width=200,
            height=50,
            fg_color="#4d4d4d",
            hover_color="#2a2a2a",
            command=lambda: self.elegir_frame(self.lista_frames["curso_materia"])
        )
        self.boton_asignatura.place(x=0, y=350)

    def elegir_frame(self, frame_elegido):
        """Muestra el frame seleccionado y oculta los demás."""
        for frame in self.lista_frames.values():
            frame.place_forget()

        frame_elegido.place(x=0, y=0)

        if hasattr(frame_elegido, "cargar_datos"):
            frame_elegido.cargar_datos()