from ui.views.mensajes import Mensaje
import customtkinter as ctk
from tkinter import ttk
import requests


class FrameMateria(ctk.CTkFrame):
    """Frame para gestionar materias"""

    def __init__(self,master):
        """Inicializa la interfaz y carga las materias"""
        super().__init__(master,width=1400,height=800,fg_color="#2A2A2A")

        self.columnas = ["id","nombre","carga_horaria"]
        self.arbol_materia(self.columnas)

        self.etiqueta_titulo = ctk.CTkLabel(self,
                                            text="MATERIAS",
                                            font=("Consolas",50))
        self.etiqueta_titulo.place(x=400,y=50)

        self.plantilla = ctk.CTkLabel(self,width=500,height=400,
                                      corner_radius=40,text="",
                                      fg_color="#404040",
                                      bg_color="#2A2A2A")
        self.plantilla.place(x=250,y=170)

        self.etiqueta_nombre = ctk.CTkLabel(self,text="NOMBRE",
                                            font=("Consolas",20))
        self.etiqueta_nombre.place(x=300,y=250)

        self.etiqueta_carga_horaria = ctk.CTkLabel(self,
                                            text="CARGA\nHORARIA",
                                            font=("Consolas",20))
        self.etiqueta_carga_horaria.place(x=300,y=300)

        self.entrada_nombre = ctk.CTkEntry(self,width=300,
                                           placeholder_text="Ingrese nombre de la materia...",
                                           placeholder_text_color="#3aaaff")
        self.entrada_nombre.place(x=400,y=250)

        self.entrada_carga_horaria = ctk.CTkEntry(self,width=300,
                                             placeholder_text="Ingrese carga horaria de la materia...",
                                             placeholder_text_color="#3aaaff")
        self.entrada_carga_horaria.place(x=400,y=300)

        self.listas_entrada = [self.entrada_nombre,self.entrada_carga_horaria]

        self.boton_guardar = ctk.CTkButton(self,text="GUARDAR",
                                           corner_radius=30,
                                           fg_color="#50c735",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#4be628",
                                           command=self.guardar_materia)
        self.boton_guardar.place(x=500,y=400)

        self.boton_eliminar = ctk.CTkButton(self,text="ELIMINAR",
                                           corner_radius=30,
                                           fg_color="#c73535",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#e62828",
                                           command=self.eliminar_materia)
        self.boton_eliminar.place(x=500,y=450)

        self.boton_actualizar = ctk.CTkButton(self,text="ACTUALIZAR",
                                           corner_radius=30,
                                           fg_color="#c78a35",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#e68d28",
                                           command=self.actualizar_materia)
        self.boton_actualizar.place(x=350,y=450)

        self.boton_nuevo = ctk.CTkButton(self,text="NUEVO",
                                           corner_radius=30,
                                           fg_color="#3574c7",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#287ee6",
                                           command=self.nueva_materia)
        self.boton_nuevo.place(x=350,y=400)

        self._cargar_materias()
        self.tabla_materias.bind("<<TreeviewSelect>>",self._llenar_entradas)




    def _vaciar_entradas(self):
        """Limpia los campos de entrada"""
        for entrada in self.listas_entrada:
            entrada.delete(0,"end")

    def _llenar_entradas(self,event):
        """Llena los campos con la materia seleccionada"""
        datos = self._obtener_datos_arbol()
        if not datos:
            return
        self._vaciar_entradas()
        self.entrada_nombre.insert(0,datos[1])
        self.entrada_carga_horaria.insert(0,datos[2])

    def _obtener_datos_arbol(self):
        """Obtiene los datos de la fila seleccionada"""
        seleccion = self.tabla_materias.selection()
        if not seleccion:
            return
        return self.tabla_materias.item(seleccion[0],"values")

    def arbol_materia(self,columnas):
        """Crea la tabla de materias"""
        self.tabla_materias = ttk.Treeview(self,
                                          columns=columnas,
                                          show="headings",
                                          height=30)

        for i in columnas:
            self.tabla_materias.heading(i, text=i.upper())
            if i == "id":
                self.tabla_materias.column(i,width=0,minwidth=0,stretch=False)
            else:
                self.tabla_materias.column(i,width=250,minwidth=200,
                                           stretch=False,anchor="center")

        self.tabla_materias.column("#0",width=0,minwidth=0,stretch=False)
        self.tabla_materias.place(x=1050,y=200)

    def _obtener_datos(self):
        """Obtiene los datos ingresados en los campos"""
        return {
            "nombre": self.entrada_nombre.get(),
            "carga_horaria": self.entrada_carga_horaria.get()
        }

    def _llenar_arbol(self,materia):
        """Agrega una materia a la tabla"""
        self.tabla_materias.insert("","end",
            values=(materia["id_materia"],
                    materia["nombre"],
                    materia["carga_horaria"]))

    def _obtener_id(self,id_columna):
        """Obtiene el id de la materia seleccionada"""
        datos = self.tabla_materias.item(id_columna[0],"values")
        return datos[0]

    def _cargar_materias(self):
        """Carga las materias desde el backend"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/materias",timeout=5)
            self._cargar_arbol(pedido.json())
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO TRAER LAS MATERIAS CORRECTAMENTE",
                    "cancel","OK",None)

    def _cargar_arbol(self,materias):
        """Carga todas las materias en la tabla"""
        for materia in materias:
            self.tabla_materias.insert("","end",
                values=(materia["id_materia"],
                        materia["nombre"],
                        materia["carga_horaria"]))

    def guardar_materia(self):
        """Guarda una nueva materia"""
        datos = self._obtener_datos()

        for dato in datos.values():
            if dato == "":
                return Mensaje(self,"ERROR",
                               "COMPLETE LOS CAMPOS!","cancel","OK",None)
        try:
            pedido = requests.post("http://127.0.0.1:8000/materias",
                                   json=datos,timeout=5)
            if pedido.status_code == 200:
                self._llenar_arbol(pedido.json())
                self._vaciar_entradas()
                Mensaje(self,"GUARDADO",
                        "SE HA GUARDADO CORRECTAMENTE LA MATERIA",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO GUARDAR LA MATERIA CORRECTAMENTE",
                    "cancel","OK",None)

    def nueva_materia(self):
        """Prepara el formulario para una nueva materia"""
        seleccion = self.tabla_materias.selection()
        if seleccion:
            self.tabla_materias.selection_remove(seleccion[0])
        self._vaciar_entradas()

    def eliminar_materia(self):
        """Elimina la materia seleccionada"""
        seleccion = self.tabla_materias.selection()
        if not seleccion:
            return Mensaje(self,"ERROR",
                           "NO SE HA SELECCIONADO NINGUNA COLUMNA",
                           "warning","OK",None)

        id_materia = self._obtener_id(seleccion)

        try:
            pedido = requests.delete(
                f"http://127.0.0.1:8000/materias/{id_materia}",
                timeout=5)
            if pedido.status_code == 200:
                self.tabla_materias.selection_remove(seleccion[0])
                self.tabla_materias.delete(seleccion[0])
                self._vaciar_entradas()
                Mensaje(self,"ELIMINADO",
                        "SE HA ELIMINADO CORRECTAMENTE LA MATERIA",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ELIMINAR LA MATERIA",
                    "cancel","OK",None)

    def _actualizar_materia_tabla(self,id_columna,datos):
        """Actualiza la materia en la tabla"""
        self.tabla_materias.item(id_columna,
            values=(datos["id_materia"],
                    datos["nombre"],
                    datos["carga_horaria"]))

    def actualizar_materia(self):
        """Actualiza la materia seleccionada"""
        seleccion = self.tabla_materias.selection()
        if not seleccion:
            return Mensaje(self,"ERROR",
                           "NO SE HA SELECCIONADO NINGUNA COLUMNA",
                           "warning","OK",None)

        id_materia = self._obtener_id(seleccion)
        datos = self._obtener_datos()

        try:
            pedido = requests.put(
                f"http://127.0.0.1:8000/materias/{id_materia}",
                json=datos,timeout=5)

            if pedido.status_code == 200:
                self.tabla_materias.selection_remove(seleccion[0])
                self._actualizar_materia_tabla(seleccion,pedido.json())
                self._vaciar_entradas()

        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ACTUALIZAR LA MATERIA CORRECTAMENTE",
                    "cancel","OK",None)