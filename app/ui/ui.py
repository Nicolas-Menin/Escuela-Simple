from ui.views.hamburguesa_view import FrameHamburguesa
import customtkinter as ctk


class App(ctk.CTk):
    """Ventana principal del sistema escolar."""

    def __init__(self):
        """Inicializa la interfaz principal y el menú de navegación."""
        super().__init__()
        self.title("Sistema Escolar")
        self.geometry(self.centrar_pantalla(1400, 800))
        self.hmbgr = False
        self.frame_hamburguesa = FrameHamburguesa(self)
        self.resizable(False, False)

        self.frame_principal = ctk.CTkFrame(
            self,
            width=1400,
            height=800,
            fg_color="#2A2A2A"
        )
        self.frame_principal.place(x=0, y=0)

        self.titulo = ctk.CTkLabel(
            self.frame_principal,
            text="SISTEMA ESCOLAR",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#ffffff"
        )
        self.titulo.place(x=550, y=20)

        self.detalle = ctk.CTkFrame(
            self.frame_principal,
            width=360,
            height=3,
            fg_color="#1f6aa5"
        )
        self.detalle.place(x=500, y=65)

        self.btn_alumnos = ctk.CTkButton(
            self.frame_principal,
            text="ALUMNOS",
            width=200,
            height=100,
            corner_radius=15,
            command=lambda: self.cargar_frame("alumno")
        )
        self.btn_alumnos.place(x=350, y=200)

        self.btn_docentes = ctk.CTkButton(
            self.frame_principal,
            text="DOCENTES",
            width=200,
            height=100,
            corner_radius=15,
            command=lambda: self.cargar_frame("docente")
        )
        self.btn_docentes.place(x=600, y=200)

        self.btn_materias = ctk.CTkButton(
            self.frame_principal,
            text="MATERIAS",
            width=200,
            height=100,
            corner_radius=15,
            command=lambda: self.cargar_frame("materia")
        )
        self.btn_materias.place(x=850, y=200)

        self.btn_cursos = ctk.CTkButton(
            self.frame_principal,
            text="CURSOS",
            width=200,
            height=100,
            corner_radius=15,
            command=lambda: self.cargar_frame("curso")
        )
        self.btn_cursos.place(x=350, y=350)

        self.btn_inscripciones = ctk.CTkButton(
            self.frame_principal,
            text="INSCRIPCIONES",
            width=200,
            height=100,
            corner_radius=15,
            command=lambda: self.cargar_frame("inscripciones")
        )
        self.btn_inscripciones.place(x=600, y=350)

        self.btn_asignaturas = ctk.CTkButton(
            self.frame_principal,
            text="ASIGNATURAS",
            width=200,
            height=100,
            corner_radius=15,
            command=lambda: self.cargar_frame("curso_materia")
        )
        self.btn_asignaturas.place(x=850, y=350)

        self.btn_menu = ctk.CTkButton(
            self,
            text="☰",
            width=40,
            command=self.alternar_menu
        )
        self.btn_menu.place(x=-100, y=10)

    def cargar_frame(self, frame_elegido):
        """Oculta el menú principal y muestra el módulo seleccionado."""
        self.frame_principal.place_forget()
        self.frame_hamburguesa.place(x=0, y=0)
        self.frame_hamburguesa.elegir_frame(
            self.frame_hamburguesa.lista_frames[frame_elegido]
        )
        self.frame_hamburguesa.tkraise()
        self.btn_menu.place(x=150, y=10)
        self.btn_menu.tkraise()

    def alternar_menu(self):
        """Muestra u oculta el menú hamburguesa."""
        if self.hmbgr:
            self.frame_hamburguesa.place(x=0)
            self.btn_menu.place(x=150)
        else:
            self.frame_hamburguesa.place(x=-300)
            self.btn_menu.place(x=10)
        self.hmbgr = not self.hmbgr

    def centrar_pantalla(self, x, y):
        """Centra la ventana en la pantalla."""
        ancho = self.winfo_screenwidth()
        largo = self.winfo_screenheight()

        pantalla_x = (ancho - x) // 2
        pantalla_y = (largo - y) // 2

        return f"{x}x{y}+{pantalla_x}+{pantalla_y}"