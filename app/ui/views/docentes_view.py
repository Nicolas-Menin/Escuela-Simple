from tkinter import ttk
import customtkinter as ctk
import requests
from ui.views.mensajes import Mensaje


class FrameDocente(ctk.CTkFrame):
    """Frame para gestionar docentes (crear, listar, actualizar y eliminar)"""

    def __init__(self,master):
        """Inicializa la interfaz de docentes y carga la tabla"""
        super().__init__(master,width=1400,height=800,fg_color="#2A2A2A")

        self.columnas = ["id","nombre","apellido","dni","profesion","correo"]
        self.arbol_docentes(self.columnas)

        self.etiqueta_titulo = ctk.CTkLabel(self,text="DOCENTES",font=("Consolas",50))
        self.etiqueta_titulo.place(x=400,y=50)

        self.plantilla = ctk.CTkLabel(self,width=500,height=400,corner_radius=40,
                                      text="",fg_color="#404040",bg_color="#2A2A2A")
        self.plantilla.place(x=250,y=170)

        self.etiqueta_nombre = ctk.CTkLabel(self,text="NOMBRE",font=("Consolas",20))
        self.etiqueta_nombre.place(x=300,y=200)

        self.etiqueta_apellido = ctk.CTkLabel(self,text="APELLIDO",font=("Consolas",20))
        self.etiqueta_apellido.place(x=300,y=250)

        self.etiqueta_dni = ctk.CTkLabel(self,text="DNI",font=("Consolas",20))
        self.etiqueta_dni.place(x=300,y=300)

        self.etiqueta_profesion = ctk.CTkLabel(self,text="PROFESION",font=("Consolas",20))
        self.etiqueta_profesion.place(x=280,y=350)

        self.etiqueta_correo = ctk.CTkLabel(self,text="CORREO",font=("Consolas",20))
        self.etiqueta_correo.place(x=300,y=400)

        self.entrada_nombre = ctk.CTkEntry(self,width=300,
                                           placeholder_text="Ingrese nombre del docente...",
                                           placeholder_text_color="#3aaaff")
        self.entrada_nombre.place(x=400,y=200)

        self.entrada_apellido = ctk.CTkEntry(self,width=300,
                                             placeholder_text="Ingrese apellido del docente...",
                                             placeholder_text_color="#3aaaff")
        self.entrada_apellido.place(x=400,y=250)

        self.entrada_dni = ctk.CTkEntry(self,width=300,
                                        placeholder_text="Ingrese dni del docente...",
                                        placeholder_text_color="#3aaaff")
        self.entrada_dni.place(x=400,y=300)

        self.entrada_profesion = ctk.CTkEntry(self,width=300,
                                              placeholder_text="Ingrese profesion del docente...",
                                              placeholder_text_color="#3aaaff")
        self.entrada_profesion.place(x=400,y=350)

        self.entrada_correo = ctk.CTkEntry(self,width=300,
                                           placeholder_text="Ingrese correo del docente...",
                                           placeholder_text_color="#3aaaff")
        self.entrada_correo.place(x=400,y=400)

        self.listas_entrada = [
            self.entrada_nombre,
            self.entrada_apellido,
            self.entrada_dni,
            self.entrada_profesion,
            self.entrada_correo
        ]

        self.boton_guardar = ctk.CTkButton(self,text="GUARDAR",corner_radius=30,
                                           fg_color="#50c735",bg_color="#404040",
                                           font=("Consolas",20),hover_color="#4be628",
                                           command=self.guardar_docente)
        self.boton_guardar.place(x=500,y=450)

        self.boton_eliminar = ctk.CTkButton(self,text="ELIMINAR",corner_radius=30,
                                            fg_color="#c73535",bg_color="#404040",
                                            font=("Consolas",20),hover_color="#e62828",
                                            command=self.eliminar_docente)
        self.boton_eliminar.place(x=500,y=500)

        self.boton_actualizar = ctk.CTkButton(self,text="ACTUALIZAR",corner_radius=30,
                                              fg_color="#c78a35",bg_color="#404040",
                                              font=("Consolas",20),hover_color="#e68d28",
                                              command=self.actualizar_docente)
        self.boton_actualizar.place(x=350,y=500)

        self.boton_nuevo = ctk.CTkButton(self,text="NUEVO",corner_radius=30,
                                         fg_color="#3574c7",bg_color="#404040",
                                         font=("Consolas",20),hover_color="#287ee6",
                                         command=self.nuevo_docente)
        self.boton_nuevo.place(x=350,y=450)

        self.tabla_docentes.bind("<<TreeviewSelect>>",self._llenar_entradas)
        self._cargar_arbol_docentes()



    def arbol_docentes(self,columnas):
        """Crea la tabla donde se muestran los docentes"""
        self.tabla_docentes = ttk.Treeview(self,columns=columnas,
                                           show="headings",height=30)

        for i in columnas:
            self.tabla_docentes.heading(i,text=i.upper())

        for i in columnas:
            if i == "id":
                self.tabla_docentes.column(i,width=0,minwidth=0,stretch=False)
            else:
                self.tabla_docentes.column(i,minwidth=140,width=140,stretch=False)

        self.tabla_docentes.column("#0",minwidth=0,width=0,stretch=False)
        self.tabla_docentes.place(x=1030,y=200)

    def _vaciar_entradas(self):
        """Limpia todos los campos de entrada"""
        for entrada in self.listas_entrada:
            entrada.delete(0,"end")

    def _llenar_entradas(self,event):
        """Llena los campos con los datos del docente seleccionado"""
        seleccion = self.tabla_docentes.selection()
        if not seleccion:
            return

        datos = self.tabla_docentes.item(seleccion[0],"values")
        self._vaciar_entradas()

        self.entrada_nombre.insert(0,datos[1])
        self.entrada_apellido.insert(0,datos[2])
        self.entrada_dni.insert(0,datos[3])
        self.entrada_profesion.insert(0,datos[4])
        self.entrada_correo.insert(0,datos[5])

    def _obtener_datos(self):
        """Obtiene los datos ingresados y los devuelve en un diccionario"""
        return {
            "nombre": self.entrada_nombre.get(),
            "apellido": self.entrada_apellido.get(),
            "dni": self.entrada_dni.get(),
            "profesion": self.entrada_profesion.get(),
            "correo": self.entrada_correo.get()
        }

    def _obtener_id(self,columna):
        """Devuelve el id del docente seleccionado"""
        datos = self.tabla_docentes.item(columna,"values")
        return datos[0]

    def _llenar_arbol(self,datos):
        """Inserta un nuevo docente en la tabla"""
        self.tabla_docentes.insert("","end",values=(
            datos["id_docente"],
            datos["nombre"],
            datos["apellido"],
            datos["dni"],
            datos["profesion"],
            datos["correo"]
        ))

    def _actualizar_docente_tabla(self,id_tabla,docente):
        """Actualiza una fila de la tabla con nuevos datos"""
        self.tabla_docentes.item(id_tabla,values=(
            docente["id_docente"],
            docente["nombre"],
            docente["apellido"],
            docente["dni"],
            docente["profesion"],
            docente["correo"]
        ))

    def _cargar_arbol_docentes(self):
        """Hace una petición GET para traer todos los docentes"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/docentes",timeout=5)
            if pedido.status_code == 200:
                self._cargar_docentes(pedido.json())
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO TRAER LOS DOCENTES CORRECTAMENTE",
                    "cancel","OK",None)

    def _cargar_docentes(self,docentes):
        """Carga todos los docentes en la tabla"""
        for docente in docentes:
            self.tabla_docentes.insert("","end",values=(
                docente["id_docente"],
                docente["nombre"],
                docente["apellido"],
                docente["dni"],
                docente["profesion"],
                docente["correo"]
            ))

    def guardar_docente(self):
        """Envía los datos al backend para guardar un docente"""
        datos = self._obtener_datos()

        for i in datos.values():
            if i == "":
                return Mensaje(self,"ERROR","COMPLETE LOS CAMPOS!","cancel","OK",None)

        try:
            pedido = requests.post("http://127.0.0.1:8000/docentes",
                                   json=datos,timeout=5)
            if pedido.status_code == 200:
                self._llenar_arbol(pedido.json())
                self._vaciar_entradas()
                Mensaje(self,"GUARDADO",
                        "SE HA GUARDADO CORRECTAMENTE EL DOCENTE",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO GUARDAR EL DOCENTE CORRECTAMENTE",
                    "cancel","OK",None)

    def eliminar_docente(self):
        """Elimina el docente seleccionado del backend y de la tabla"""
        seleccion = self.tabla_docentes.selection()
        if not seleccion:
            return Mensaje(self,"ERROR",
                           "NO SE HA SELECCIONADO NINGUNA COLUMNA",
                           "warning","OK",None)

        id_docente = self._obtener_id(seleccion[0])

        try:
            pedido = requests.delete(
                f"http://127.0.0.1:8000/docentes/{id_docente}",timeout=5)
            if pedido.status_code == 200:
                self.tabla_docentes.selection_remove(seleccion[0])
                self.tabla_docentes.delete(seleccion[0])
                self._vaciar_entradas()
                Mensaje(self,"ELIMINADO",
                        "SE HA ELIMINADO CORRECTAMENTE EL DOCENTE",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ELIMINAR EL DOCENTE",
                    "cancel","OK",None)

    def nuevo_docente(self):
        """Limpia la selección y los campos para crear un nuevo docente"""
        seleccion = self.tabla_docentes.selection()
        if seleccion:
            self.tabla_docentes.selection_remove(seleccion[0])
        self._vaciar_entradas()

    def actualizar_docente(self):
        """Actualiza los datos del docente seleccionado"""
        seleccion = self.tabla_docentes.selection()
        if not seleccion:
            return Mensaje(self,"ERROR",
                           "NO SE HA SELECCIONADO NINGUNA COLUMNA",
                           "warning","OK",None)

        datos = self._obtener_datos()
        id_docente = self._obtener_id(seleccion[0])

        try:
            pedido = requests.put(
                f"http://127.0.0.1:8000/docentes/{id_docente}",
                json=datos,timeout=5)

            if pedido.status_code == 200:
                self.tabla_docentes.selection_remove(seleccion[0])
                self._actualizar_docente_tabla(seleccion[0],pedido.json())
                self._vaciar_entradas()
                Mensaje(self,"ACTUALIZADO",
                        "SE HA ACTUALIZADO CORRECTAMENTE EL DOCENTE",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ACTUALIZAR EL DOCENTE CORRECTAMENTE",
                    "cancel","OK",None)