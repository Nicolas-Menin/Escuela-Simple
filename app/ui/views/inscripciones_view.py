from tkinter import ttk
from CTkCalendar import CTkCalendar
from ui.views.mensajes import Mensaje
import customtkinter as ctk
import requests


class FrameInscripciones(ctk.CTkFrame):
    """Frame para gestionar inscripciones de alumnos a cursos"""

    def __init__(self,master):
        """Inicializa la interfaz de inscripciones y carga datos"""
        super().__init__(master,width=1400,height=800,fg_color="#2A2A2A")

        self.columnas = ["id_inscripcion","id_alumno","id_curso",
                         "alumno","curso","fecha_inscripcion"]
        self.arbol_inscripciones(self.columnas)

        self.alumnos = None
        self.estado_calendario = False
        self.cursos = None

        self.etiqueta_titulo = ctk.CTkLabel(self,
                                            text="Inscripciones de alumnos a cursos",
                                            font=("Consolas",50))
        self.etiqueta_titulo.place(x=400,y=50)

        self.plantilla = ctk.CTkLabel(self,width=500,height=400,
                                      corner_radius=40,text="",
                                      fg_color="#404040",bg_color="#2A2A2A")
        self.plantilla.place(x=250,y=170)

        self.registar_alumno = ctk.CTkLabel(self,text="ELEGIR\nALUMNO",
                                            font=("Consolas",20))
        self.registar_alumno.place(x=300,y=200)

        self.registrar_curso = ctk.CTkLabel(self,text="ELEGIR\nCURSO",
                                            font=("Consolas",20))
        self.registrar_curso.place(x=300,y=275)

        self.registrar_fecha_inscripcion = ctk.CTkLabel(self,
                                            text="FECHA\nINSCRIPCION",
                                            font=("Consolas",20))
        self.registrar_fecha_inscripcion.place(x=260,y=350)

        self.cbox_alumnos = ctk.CTkComboBox(self,width=250,justify="center",
                                            variable=ctk.StringVar(
                                            value="Seleccione uno de los alumnos"),
                                            state="readonly")
        self.cbox_alumnos.place(x=400,y=210)

        self.cbox_curso = ctk.CTkComboBox(self,width=250,justify="center",
                                          variable=ctk.StringVar(
                                          value="Seleccione uno de los cursos"),
                                          state="readonly")
        self.cbox_curso.place(x=400,y=280)

        self.lista_cbox = [self.cbox_alumnos,self.cbox_curso]

        self.entrada_fecha_inscripcion = ctk.CTkEntry(self,width=200,
                                           placeholder_text="Fecha inscripcion XX/XX/XXXX...",
                                           placeholder_text_color="#3aaaff")
        self.entrada_fecha_inscripcion.place(x=400,y=350)

        self.boton_calendario = ctk.CTkButton(self,text="📅",width=30,
                                              command=self.mostrar_calendario)
        self.boton_calendario.place(x=600,y=350)

        self.boton_guardar = ctk.CTkButton(self,text="GUARDAR",
                                           corner_radius=30,
                                           fg_color="#50c735",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#4be628",
                                           command=self.guardar_inscripcion)
        self.boton_guardar.place(x=500,y=450)

        self.boton_eliminar = ctk.CTkButton(self,text="ELIMINAR",
                                           corner_radius=30,
                                           fg_color="#c73535",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#e62828",
                                           command=self.eliminar_inscripcion)
        self.boton_eliminar.place(x=500,y=500)

        self.boton_actualizar = ctk.CTkButton(self,text="ACTUALIZAR",
                                           corner_radius=30,
                                           fg_color="#c78a35",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#e68d28",
                                           command=self.actualizar_inscripcion)
        self.boton_actualizar.place(x=350,y=500)

        self.boton_nuevo = ctk.CTkButton(self,text="NUEVO",
                                           corner_radius=30,
                                           fg_color="#3574c7",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#287ee6",
                                           command=self.nueva_inscripcion)
        self.boton_nuevo.place(x=350,y=450)

        self.calendario = CTkCalendar(self,command=self.insertar_fecha)

        self.listar_inscripciones()
        self.cargar_alumnos()
        self.cargar_cursos()
        self.mostrar_calendario()

        self.bind("<Button-1>", lambda e: self.calendario.place_forget())
        self.tabla_inscripciones.bind("<<TreeviewSelect>>",self._llenar_campos)


    def vaciar_tabla(self):

        for i in self.tabla_inscripciones.get_children():

            self.tabla_inscripciones.delete(i)

    def cargar_datos(self):
        self.vaciar_tabla()
        self.listar_inscripciones()
        self.cargar_alumnos()
        self.cargar_cursos()

    def _llenar_campos(self,evento):
        """Llena los campos con los datos de la inscripción seleccionada"""
        seleccion = self.tabla_inscripciones.selection()
        if not seleccion:
            return

        datos = self.tabla_inscripciones.item(seleccion[0],"values")
        self._vaciar_campos()
        self.cbox_alumnos.set(value=datos[3])
        self.cbox_curso.set(value=datos[4])
        self.entrada_fecha_inscripcion.insert(0,datos[5])

    def _vaciar_campos(self):
        """Limpia los campos del formulario"""
        for cbox in self.lista_cbox:
            cbox.set(value="")
        self.entrada_fecha_inscripcion.delete(0,"end")

    def mostrar_calendario(self):
        """Muestra u oculta el calendario"""
        if self.estado_calendario:
            self.calendario.place(x=610,y=350)
        else:
            self.calendario.place_forget()

        self.estado_calendario = not self.estado_calendario

    def insertar_fecha(self,fecha):
        """Inserta la fecha seleccionada en el campo"""
        self.entrada_fecha_inscripcion.delete(0,"end")
        self.entrada_fecha_inscripcion.insert(0,fecha)

    def arbol_inscripciones(self,columnas):
        """Crea la tabla de inscripciones"""
        self.tabla_inscripciones = ttk.Treeview(self,columns=columnas,
                                        show="headings",height=30)

        for i in columnas:
            self.tabla_inscripciones.heading(i,text=i.upper())

        for i in columnas:
            if i in ["id_inscripcion","id_alumno","id_curso"]:
                self.tabla_inscripciones.column(i,width=0,minwidth=0,stretch=False)
            else:
                self.tabla_inscripciones.column(i,minwidth=140,width=140,stretch=False)

        self.tabla_inscripciones.column("#0",minwidth=0,width=0,stretch=False)
        self.tabla_inscripciones.place(x=1030,y=200)



    def cargar_alumnos(self):
        """Carga alumnos en el combobox"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/alumnos/combo",timeout=5)
            if pedido.status_code == 200:
                self.alumnos = pedido.json()
                nombres = [i["nombre"] for i in self.alumnos]
                self.cbox_alumnos.configure(values=nombres)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO CARGAR LOS ALUMNOS CORRECTAMENTE",
                    "cancel","OK",None)

    def cargar_cursos(self):
        """Carga cursos en el combobox"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/cursos/combo",timeout=5)
            if pedido.status_code == 200:
                self.cursos = pedido.json()
                nombres = [i["nombre"] for i in self.cursos]
                self.cbox_curso.configure(values=nombres)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO CARGAR LOS CURSOS CORRECTAMENTE",
                    "cancel","OK",None)

    def _obtener_id_alumno(self):
        """Devuelve el id del alumno seleccionado"""
        if not self.alumnos:
            return
        for alumno in self.alumnos:
            if alumno["nombre"] == self.cbox_alumnos.get():
                return alumno["id_alumno"]
        return None

    def _obtener_id_curso(self):
        """Devuelve el id del curso seleccionado"""
        if not self.cursos:
            return
        for curso in self.cursos:
            if curso["nombre"] == self.cbox_curso.get():
                return curso["id_curso"]
        return None

    def _obtener_id_inscripciones(self,columna):
        """Devuelve el id de la inscripción seleccionada"""
        datos = self.tabla_inscripciones.item(columna,"values")
        return datos[0]

    def _obtener_datos(self):
        """Obtiene los datos ingresados para enviar al backend"""
        if self.cbox_alumnos.get() in ["Seleccione uno de los alumnos",""]:
            return
        if self.cbox_curso.get() in ["Seleccione uno de los cursos",""]:
            return
        if self.entrada_fecha_inscripcion.get() == "":
            return

        return {
            "id_alumno": self._obtener_id_alumno(),
            "id_curso": self._obtener_id_curso(),
            "fecha_inscripcion": self.entrada_fecha_inscripcion.get()
        }

    def _obtenner_datos_combo(self):
        """Obtiene los nombres seleccionados en los combobox"""
        return {"alumno": self.cbox_alumnos.get(),
                "curso": self.cbox_curso.get()}

    def _llenar_arbol(self,id_inscripcion,datos):
        """Inserta una nueva inscripción en la tabla"""
        informacion_cbox = self._obtenner_datos_combo()

        self.tabla_inscripciones.insert("","end",values=(
            id_inscripcion["id_inscripcion"],
            datos["id_alumno"],
            datos["id_curso"],
            informacion_cbox["alumno"],
            informacion_cbox["curso"],
            datos["fecha_inscripcion"]
        ))

    def _cargar_arbol(self,inscripciones):
        """Carga todas las inscripciones en la tabla"""
        for inscripcion in inscripciones:
            self.tabla_inscripciones.insert("","end",values=(
                inscripcion["id_inscripcion"],
                inscripcion["id_alumno"],
                inscripcion["id_curso"],
                inscripcion["alumno"],
                inscripcion["curso"],
                inscripcion["fecha_inscripcion"]
            ))

    def nueva_inscripcion(self):
        """Limpia selección y campos para nueva inscripción"""
        seleccion = self.tabla_inscripciones.selection()
        if seleccion:
            self.tabla_inscripciones.selection_remove(seleccion[0])
        self._vaciar_campos()

    def guardar_inscripcion(self):
        """Envía los datos al backend para guardar inscripción"""
        datos = self._obtener_datos()
        if not datos:
            return Mensaje(self,"ERROR","COMPLETE LOS CAMPOS!","cancel","OK",None)

        try:
            pedido = requests.post("http://127.0.0.1:8000/inscripciones",
                                   json=datos, timeout=5)
            if pedido.status_code == 200:
                self._llenar_arbol(pedido.json(),datos)
                self._vaciar_campos()
                Mensaje(self,"GUARDADO",
                        "SE HA GUARDADO CORRECTAMENTE LA INSCRIPCION",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO GUARDAR LA INSCRIPCION CORRECTAMENTE",
                    "cancel","OK",None)

    def _eliminar_columna(self,columna):
        """Elimina una fila de la tabla"""
        self.tabla_inscripciones.delete(columna)

    def eliminar_inscripcion(self):
        """Elimina la inscripción seleccionada"""
        seleccion = self.tabla_inscripciones.selection()
        if not seleccion:
            return Mensaje(self,"ERROR",
                           "NO SE HA SELECCIONADO NINGUNA ASIGNACION EN LA TABLA!",
                           "cancel","OK",None)

        id_inscripcion = self._obtener_id_inscripciones(seleccion[0])

        try:
            pedido = requests.delete(
                f"http://127.0.0.1:8000/inscripciones/{id_inscripcion}",
                json=id_inscripcion,timeout=5)

            if pedido.status_code == 200:
                self.tabla_inscripciones.selection_remove(seleccion[0])
                self._eliminar_columna(seleccion[0])
                self._vaciar_campos()
                Mensaje(self,"ELIMINADO",
                        "SE HA ELIMINADO CORRECTAMENTE LA INSCRIPCION",
                        "check","OK",None)

        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ELIMINAR LA INSCRIPCION CORRECTAMENTE",
                    "cancel","OK",None)

    def _actualizar_columna(self,columna,datos):
        """Actualiza una fila de la tabla"""
        self.tabla_inscripciones.item(columna,values=(
            datos["id_inscripcion"],
            datos["id_alumno"],
            datos["id_curso"],
            datos["alumno"],
            datos["curso"],
            datos["fecha_inscripcion"]
        ))

    def actualizar_inscripcion(self):
        """Actualiza la inscripción seleccionada"""
        seleccion = self.tabla_inscripciones.selection()
        if not seleccion:
            return Mensaje(self,"ERROR",
                           "NO SE HA SELECCIONADO NINGUNA ASIGNACION EN LA TABLA!",
                           "cancel","OK",None)

        datos = self._obtener_datos()
        id_inscripcion = self._obtener_id_inscripciones(seleccion[0])

        try:
            pedido = requests.put(
                f"http://127.0.0.1:8000/inscripciones/{id_inscripcion}",
                json=datos,timeout=5)

            if pedido.status_code == 200:
                self.tabla_inscripciones.selection_remove(seleccion[0])
                self._actualizar_columna(seleccion[0],pedido.json())
                self._vaciar_campos()

        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ACTUALIZAR LA INSCRIPCION CORRECTAMENTE",
                    "cancel","OK",None)

    def listar_inscripciones(self):
        """Obtiene todas las inscripciones del backend"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/inscripciones",timeout=5)
            if pedido.status_code == 200:
                self._cargar_arbol(pedido.json())
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO TRAER LAS INSCRIPCIONES CORRECTAMENTE",
                    "cancel","OK",None)