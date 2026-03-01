from ui.views.mensajes import Mensaje
from tkinter import ttk
import customtkinter as ctk
import requests


class FrameCursoMateria(ctk.CTkFrame):
    """Frame para asignar materias y docentes a cursos"""

    def __init__(self,master):
        """Inicializa la interfaz y carga las asignaciones y los combobox"""
        super().__init__(master,width=1400,height=800,fg_color="#2A2A2A")

        self.docentes = None
        self.materias = None
        self.cursos = None
        self.columnas = ["id_curso_materia","id_materia","id_docente",
                         "id_curso","curso","materia","docente"]
        self.arbol_cursos_materias(self.columnas)

        self.etiqueta_titulo = ctk.CTkLabel(self,
                                            text="Asignación de Materias a Cursos",
                                            font=("Consolas",50))
        self.etiqueta_titulo.place(x=400,y=50)

        self.plantilla = ctk.CTkLabel(self,
                                      width=500,
                                      height=400,
                                      corner_radius=40,
                                      text="",
                                      fg_color="#404040",
                                      bg_color="#2A2A2A")
        self.plantilla.place(x=250,y=170)

        self.registrar_materia = ctk.CTkLabel(self,text="REGISTRAR\nMATERIA",font=("Consolas",20))
        self.registrar_materia.place(x=300,y=200)

        self.registar_docente = ctk.CTkLabel(self,text="REGISTRAR\nDOCENTE",font=("Consolas",20))
        self.registar_docente.place(x=300,y=275)

        self.registrar_curso = ctk.CTkLabel(self,text="REGISTRAR\nCURSO",font=("Consolas",20))
        self.registrar_curso.place(x=300,y=350)

        self.cbox_materia = ctk.CTkComboBox(self,state="readonly",width=250,justify="center",
                                            variable=ctk.StringVar(value="Seleccione una materia"))
        self.cbox_materia.place(x=420,y=210)

        self.cbox_docente = ctk.CTkComboBox(self,state="readonly",width=250,justify="center",
                                            variable=ctk.StringVar(value="Seleccione un docente"))
        self.cbox_docente.place(x=420,y=285)

        self.cbox_curso = ctk.CTkComboBox(self,state="readonly",width=250,justify="center",
                                          variable=ctk.StringVar(value="Seleccione un curso"))
        self.cbox_curso.place(x=420,y=360)

        self.lista_cbox = [self.cbox_materia,self.cbox_docente,self.cbox_curso]

        self.boton_guardar = ctk.CTkButton(self,text="GUARDAR",corner_radius=30,
                                           fg_color="#50c735",bg_color="#404040",
                                           font=("Consolas",20),hover_color="#4be628",
                                           command=self.guardar_curso_materia)
        self.boton_guardar.place(x=500,y=450)

        self.boton_eliminar = ctk.CTkButton(self,text="ELIMINAR",corner_radius=30,
                                           fg_color="#c73535",bg_color="#404040",
                                           font=("Consolas",20),hover_color="#e62828",
                                           command=self.eliminar_curso_materia)
        self.boton_eliminar.place(x=500,y=500)

        self.boton_actualizar = ctk.CTkButton(self,text="ACTUALIZAR",corner_radius=30,
                                           fg_color="#c78a35",bg_color="#404040",
                                           font=("Consolas",20),hover_color="#e68d28",
                                           command=self.actualizar_curso_materia)
        self.boton_actualizar.place(x=350,y=500)

        self.boton_nuevo = ctk.CTkButton(self,text="NUEVO",corner_radius=30,
                                           fg_color="#3574c7",bg_color="#404040",
                                           font=("Consolas",20),hover_color="#287ee6",
                                           command=self.nuevo_curso_materia)
        self.boton_nuevo.place(x=350,y=450)

        self._cargar_cursos_materias()
        self.cargar_materias()
        self.cargar_docentes()
        self.cargar_cursos()

        self.tabla_curso_materias.bind("<<TreeviewSelect>>",self._llenar_cbox)

    def vaciar_tabla(self):

        for i in self.tabla_curso_materias.get_children():

            self.tabla_curso_materias.delete(i)

    def cargar_datos(self):
        self.vaciar_tabla()
        self._cargar_cursos_materias()
        self.cargar_materias()
        self.cargar_docentes()
        self.cargar_cursos()


    def _llenar_cbox(self,evento):
        """Llena los combobox con los datos de la fila seleccionada"""
        seleccion = self.tabla_curso_materias.selection()
        if not seleccion:
            return
        datos = self.tabla_curso_materias.item(seleccion[0],"values")
        self._limpiar_cbox()
        self.cbox_materia.set(value=datos[5])
        self.cbox_docente.set(value=datos[6])
        self.cbox_curso.set(value=datos[4])


    def _limpiar_cbox(self):
        """Limpia todos los combobox"""
        for cbox in self.lista_cbox:
            cbox.set(value="")


    def _obtener_id_curso_materia(self,columna):
        """Devuelve el id de la asignación seleccionada"""
        datos = self.tabla_curso_materias.item(columna,"values")
        return datos[0]


    def _obtener_id_materia(self):
        """Devuelve el id de la materia seleccionada"""
        if not self.materias:
            return None
        for materia in self.materias:
            if materia["nombre"] == self.cbox_materia.get():
                return materia["id_materia"]
        return None


    def _obtener_id_docente(self):
        """Devuelve el id del docente seleccionado"""
        if not self.docentes:
            return None
        for docente in self.docentes:
            if docente["nombre"] == self.cbox_docente.get():
                return docente["id_docente"]
        return None


    def _obtener_id_curso(self):
        """Devuelve el id del curso seleccionado"""
        if not self.cursos:
            return None
        for curso in self.cursos:
            if curso["nombre"] == self.cbox_curso.get():
                return curso["id_curso"]
        return None


    def _obtener_datos(self):
        """Obtiene los ids seleccionados y los devuelve en un diccionario"""
        if self.cbox_materia.get() == "" or self.cbox_docente.get() == "" or self.cbox_curso.get() == "":
            return
        return {
            "id_materia": self._obtener_id_materia(),
            "id_docente": self._obtener_id_docente(),
            "id_curso": self._obtener_id_curso()
        }


    def _obtener_informacion_cbox(self):
        """Devuelve los nombres seleccionados en los combobox"""
        return {
            "nombre_materia": self.cbox_materia.get(),
            "nombre_docente": self.cbox_docente.get(),
            "nombre_curso": self.cbox_curso.get()
        }


    def _llenar_arbol(self,id_curso_materia,datos):
        """Inserta una nueva asignación en la tabla"""
        nombres = self._obtener_informacion_cbox()
        self.tabla_curso_materias.insert("","end",values=(
            id_curso_materia["id_curso_materia"],
            datos["id_materia"],
            datos["id_docente"],
            datos["id_curso"],
            nombres["nombre_curso"],
            nombres["nombre_materia"],
            nombres["nombre_docente"]
        ))


    def _cargar_arbol(self,asiganciones):
        """Carga todas las asignaciones en la tabla"""
        for asignacion in asiganciones:
            self.tabla_curso_materias.insert("","end",values=(
                asignacion["id_curso_materia"],
                asignacion["id_materia"],
                asignacion["id_docente"],
                asignacion["id_curso"],
                asignacion["nombre_curso"],
                asignacion["nombre_materia"],
                asignacion["nombre_docente"]
            ))


    def _actualizar_columna(self,columna,datos):
        """Actualiza una fila de la tabla"""
        self.tabla_curso_materias.item(columna,values=(
            datos["id_curso_materia"],
            datos["id_materia"],
            datos["id_docente"],
            datos["id_curso"],
            datos["nombre_curso"],
            datos["nombre_materia"],
            datos["nombre_docente"]
        ))


    def _borrar_columna(self,columna):
        """Elimina una fila de la tabla"""
        self.tabla_curso_materias.delete(columna)


    def nuevo_curso_materia(self):
        """Limpia selección y combobox para nueva asignación"""
        seleccion = self.tabla_curso_materias.selection()
        if seleccion:
            self.tabla_curso_materias.selection_remove(seleccion[0])
        self._limpiar_cbox()


    def guardar_curso_materia(self):
        """Guarda una nueva asignación en el backend"""
        datos = self._obtener_datos()
        if not datos:
            return Mensaje(self,"ERROR","COMPLETE LOS CAMPOS!","cancel","OK",None)

        try:
            pedido = requests.post("http://127.0.0.1:8000/curso_materia",json=datos,timeout=5)
            if pedido.status_code == 200:
                self._llenar_arbol(pedido.json(),datos)
                self._limpiar_cbox()
                Mensaje(self,"GUARDADO","SE HA GUARDADO CORRECTAMENTE LA ASIGNACION","check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO GUARDAR LA ASIGNACION CORRECTAMENTE",
                    "cancel","OK",None)


    def eliminar_curso_materia(self):
        """Elimina la asignación seleccionada"""
        seleccion = self.tabla_curso_materias.selection()
        if not seleccion:
            return Mensaje(self,"ERROR","NO SE HA SELECCIONADO NINGUNA ASIGNACION EN LA TABLA!","cancel","OK",None)

        id_curso_materia = self._obtener_id_curso_materia(seleccion[0])

        try:
            pedido = requests.delete(f"http://127.0.0.1:8000/curso_materia/{id_curso_materia}",timeout=5)
            if pedido.status_code == 200:
                self.tabla_curso_materias.selection_remove(seleccion[0])
                self._borrar_columna(seleccion[0])
                self._limpiar_cbox()
                Mensaje(self,"ELIMINADO","SE HA ELIMINADO CORRECTAMENTE LA ASIGNACION","check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO ELIMINAR LA ASIGNACION CORRECTAMENTE",
                    "cancel","OK",None)


    def actualizar_curso_materia(self):
        """Actualiza la asignación seleccionada"""
        seleccion = self.tabla_curso_materias.selection()
        if not seleccion:
            return Mensaje(self,"ERROR","NO SE HA SELECCIONADO NINGUNA ASIGNACION EN LA TABLA!","cancel","OK",None)

        datos = self._obtener_datos()
        id_curso_materia = self._obtener_id_curso_materia(seleccion[0])

        try:
            pedido = requests.put(f"http://127.0.0.1:8000/curso_materia/{id_curso_materia}",json=datos,timeout=5)
            if pedido.status_code == 200:
                self.tabla_curso_materias.selection_remove(seleccion[0])
                self._actualizar_columna(seleccion[0],pedido.json())
                self._limpiar_cbox()
                Mensaje(self,"ACTUALIZADO","SE HA ACTUALIZADO LA ASIGNACION CORRECTAMENTE","check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO ACTUALIZAR LA ASIGNACION CORRECTAMENTE",
                    "cancel","OK",None)


    def arbol_cursos_materias(self,columnas):
        """Crea la tabla donde se muestran las asignaciones"""
        self.tabla_curso_materias = ttk.Treeview(self,columns=columnas,show="headings",height=30)

        for i in columnas:
            self.tabla_curso_materias.heading(i,text=i.upper())

        for i in columnas:
            if i in ["id_curso_materia","id_materia","id_docente","id_curso"]:
                self.tabla_curso_materias.column(i,width=0,minwidth=0,stretch=False)
            else:
                self.tabla_curso_materias.column(i,minwidth=140,width=140,stretch=False,anchor="center")

        self.tabla_curso_materias.column("#0",minwidth=0,width=0,stretch=False)
        self.tabla_curso_materias.place(x=1030,y=200)


    def _cargar_cursos_materias(self):
        """Carga todas las asignaciones desde el backend"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/curso_materia",timeout=5)
            if pedido.status_code == 200:
                self._cargar_arbol(pedido.json())
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO CARGAR LAS ASIGNACIONES CORRECTAMENTE",
                    "cancel","OK",None)


    def cargar_docentes(self):
        """Carga los docentes en el combobox"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/docentes/combo",timeout=5)
            if pedido.status_code ==200:
                self.docentes = pedido.json()
                nombres = [i["nombre"] for i in self.docentes]
                self.cbox_docente.configure(values=nombres)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO TRAER LOS DOCENTES CORRECTAMENTE",
                    "cancel","OK",None)


    def cargar_cursos(self):
        """Carga los cursos en el combobox"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/cursos/combo",timeout=5)
            if pedido.status_code ==200:
                self.cursos = pedido.json()
                nombres = [i["nombre"] for i in self.cursos]
                self.cbox_curso.configure(values=nombres)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO TRAER LOS CURSOS CORRECTAMENTE",
                    "cancel","OK",None)


    def cargar_materias(self):
        """Carga las materias en el combobox"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/materias/combo",timeout=5)
            if pedido.status_code == 200:
                self.materias = pedido.json()
                nombres = [i["nombre"] for i in self.materias]
                self.cbox_materia.configure(values=nombres)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO TRAER LAS MATERIAS CORRECTAMENTE",
                    "cancel","OK",None)