from ui.views.alumnos_view import FrameAlumnos
from ui.views.docentes_view import FrameDocente
from ui.views.materias_view import FrameMateria
from ui.views.cursos_view import FrameCurso
from ui.views.inscripciones_view import FrameInscripciones
from ui.views.cursos_materias_views import FrameCursoMateria
import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar")
        self.geometry(self.centrar_pantalla(1400,800))
        self.hmbgr = False
        self.resizable(False,False)
        self.lista_frames = {"alumno": FrameAlumnos(self),
                             "docente": FrameDocente(self),
                             "materia": FrameMateria(self),
                             "curso": FrameCurso(self),
                             "curso_materia": FrameCursoMateria(self),
                             "inscripciones": FrameInscripciones(self)}

        self.frame_hmbgr = ctk.CTkFrame(
            self,
            width=200,
            height=800,
            fg_color="#3b3b3b"
        )
        self.frame_hmbgr.place(x=-300, y=0)
        self.btn_menu = ctk.CTkButton(
            self,
            text="☰",
            width=40,
            command=self.alternar_menu
        )
        self.btn_menu.place(x=10, y=10)


        self.alternar_menu()

        self.boton_alumnos = ctk.CTkButton(self.frame_hmbgr,
                                           corner_radius=0,
                                           text="ALUMNOS",
                                           width=200,
                                           height=50,
                                           fg_color="#4d4d4d",
                                           hover_color="#2a2a2a",
                                           command=lambda : self.elegir_frame(self.lista_frames["alumno"])

                                           )
        self.boton_alumnos.place(x=0,y=100)
        self.boton_docentes = ctk.CTkButton(self.frame_hmbgr,
                                           corner_radius=0,
                                           text="DOCENTES",
                                           width=200,
                                           height=50,
                                           fg_color="#4d4d4d",
                                           hover_color="#2a2a2a",
                                           command=lambda : self.elegir_frame(self.lista_frames["docente"]))
        self.boton_docentes.place(x=0,y=150)
        self.boton_materias = ctk.CTkButton(self.frame_hmbgr,
                                           corner_radius=0,
                                           text="MATERIAS",
                                           width=200,
                                           height=50,
                                           fg_color="#4d4d4d",
                                           hover_color="#2a2a2a",
                                           command=lambda :self.elegir_frame(self.lista_frames["materia"]))
        self.boton_materias.place(x=0,y=200)
        self.boton_inscripciones = ctk.CTkButton(self.frame_hmbgr,
                                           corner_radius=0,
                                           text="INSCRIPCIONES",
                                           width=200,
                                           height=50,
                                           fg_color="#4d4d4d",
                                           hover_color="#2a2a2a",
                                           command=lambda :self.elegir_frame(self.lista_frames["inscripciones"]))
        self.boton_inscripciones.place(x=0,y=250)
        self.boton_cursos = ctk.CTkButton(self.frame_hmbgr,
                                           corner_radius=0,
                                           text="CURSOS",
                                           width=200,
                                           height=50,
                                           fg_color="#4d4d4d",
                                           hover_color="#2a2a2a",
                                           command=lambda : self.elegir_frame(self.lista_frames["curso"]))
        self.boton_cursos.place(x=0,y=300)

        self.boton_asignatura = ctk.CTkButton(self.frame_hmbgr,
                                           corner_radius=0,
                                           text="ASIGNATURAS",
                                           width=200,
                                           height=50,
                                           fg_color="#4d4d4d",
                                           hover_color="#2a2a2a",
                                           command=lambda : self.elegir_frame(self.lista_frames["curso_materia"]))
        self.boton_asignatura.place(x=0,y=350)


    def elegir_frame(self,frame_elegido):

        for frame in self.lista_frames.values():
            frame.place_forget()

        frame_elegido.place(x=0,y=0)
        self.frame_hmbgr.tkraise()
        self.btn_menu.tkraise()

    def alternar_menu(self):

        if self.hmbgr:

            self.frame_hmbgr.place(x=0)
            self.btn_menu.place(x=150)
        else:
            self.frame_hmbgr.place(x=-300)
            self.btn_menu.place(x=10)
        self.hmbgr = not self.hmbgr

    def centrar_pantalla(self,x,y):

        ancho = self.winfo_screenwidth()
        largo = self.winfo_screenheight()


        pantalla_x = (ancho - x) // 2
        pantalla_y = (largo - y) // 2

        return f"{x}x{y}+{pantalla_x}+{pantalla_y}"

