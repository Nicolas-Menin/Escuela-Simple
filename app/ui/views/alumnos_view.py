from tkinter import ttk
import requests
import customtkinter as ctk
from ui.views.mensajes import Mensaje


class FrameAlumnos(ctk.CTkFrame):
    """Frame para gestionar alumnos (crear, listar, actualizar y eliminar)"""

    def __init__(self,master):
        """Inicializa la interfaz y carga los alumnos en la tabla"""
        super().__init__(master,width=1400,height=800,fg_color="#2A2A2A")

        self.columnas = ["id","nombre","apellido","dni","correo"]
        self.arbol_alumnos(self.columnas)

        # TITULO
        self.etiqueta_titulo = ctk.CTkLabel(self,
                                            text="ALUMNOS",
                                            font=("Consolas",50))
        self.etiqueta_titulo.place(x=400,y=50)

        # PLANTILLA
        self.plantilla = ctk.CTkLabel(self,
                                      width=500,
                                      height=400,
                                      corner_radius=40,
                                      text="",
                                      fg_color="#404040",
                                      bg_color="#2A2A2A")
        self.plantilla.place(x=250,y=170)

        # ETIQUETAS
        self.etiqueta_nombre = ctk.CTkLabel(self,text="NOMBRE",font=("Consolas",20))
        self.etiqueta_nombre.place(x=300,y=200)

        self.etiqueta_apellido = ctk.CTkLabel(self,text="APELLIDO",font=("Consolas",20))
        self.etiqueta_apellido.place(x=300,y=250)

        self.etiqueta_dni = ctk.CTkLabel(self,text="DNI",font=("Consolas",20))
        self.etiqueta_dni.place(x=300,y=300)

        self.etiqueta_correo = ctk.CTkLabel(self,text="CORREO",font=("Consolas",20))
        self.etiqueta_correo.place(x=300,y=350)

        # ENTRADAS
        self.entrada_nombre = ctk.CTkEntry(self,width=300,
                                           placeholder_text="Ingrese nombre del alumno...",
                                           placeholder_text_color="#3aaaff")
        self.entrada_nombre.place(x=400,y=200)

        self.entrada_apellido = ctk.CTkEntry(self,width=300,
                                             placeholder_text="Ingrese apellido del alumno...",
                                             placeholder_text_color="#3aaaff")
        self.entrada_apellido.place(x=400,y=250)

        self.entrada_dni = ctk.CTkEntry(self,width=300,
                                        placeholder_text="Ingrese dni del alumno...",
                                        placeholder_text_color="#3aaaff")
        self.entrada_dni.place(x=400,y=300)

        self.entrada_correo = ctk.CTkEntry(self,width=300,
                                           placeholder_text="Ingrese correo del alumno...",
                                           placeholder_text_color="#3aaaff")
        self.entrada_correo.place(x=400,y=350)

        self.listas_entrada = [
            self.entrada_nombre,
            self.entrada_apellido,
            self.entrada_dni,
            self.entrada_correo
        ]

        # BOTONES
        self.boton_guardar = ctk.CTkButton(self,text="GUARDAR",
                                           corner_radius=30,
                                           fg_color="#50c735",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#4be628",
                                           command=self.guardar_alumno)
        self.boton_guardar.place(x=500,y=400)

        self.boton_eliminar = ctk.CTkButton(self,text="ELIMINAR",
                                           corner_radius=30,
                                           fg_color="#c73535",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#e62828",
                                           command=self.eliminar_alumno)
        self.boton_eliminar.place(x=500,y=450)

        self.boton_actualizar = ctk.CTkButton(self,text="ACTUALIZAR",
                                           corner_radius=30,
                                           fg_color="#c78a35",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#e68d28",
                                           command=self.actualizar_alumno)
        self.boton_actualizar.place(x=350,y=450)

        self.boton_nuevo = ctk.CTkButton(self,text="NUEVO",
                                           corner_radius=30,
                                           fg_color="#3574c7",
                                           bg_color="#404040",
                                           font=("Consolas",20),
                                           hover_color="#287ee6",
                                           command=self.nuevo_alumno)
        self.boton_nuevo.place(x=350,y=400)

        self._cargar_arbol_alumnos()
        self.tabla_alumnos.bind("<<TreeviewSelect>>",self.llenar_entradas)


    def arbol_alumnos(self,columnas):
        """Crea la tabla donde se muestran los alumnos"""
        self.tabla_alumnos = ttk.Treeview(self,
                                          columns=columnas,
                                          show="headings",
                                          height=30)

        for i in columnas:
            self.tabla_alumnos.heading(i, text=i.upper())

            if i == "id":
                self.tabla_alumnos.column(i,width=0,minwidth=0,stretch=False)
            else:
                self.tabla_alumnos.column(i,width=150,minwidth=150,stretch=False)

        self.tabla_alumnos.column("#0",width=0,minwidth=0,stretch=False)
        self.tabla_alumnos.place(x=1050,y=200)


    def _vaciar_entradas(self):
        """Vacía los campos de texto"""
        self.entrada_nombre.delete(0,"end")
        self.entrada_apellido.delete(0,"end")
        self.entrada_dni.delete(0,"end")
        self.entrada_correo.delete(0,"end")


    def llenar_entradas(self,event):
        """Llena los campos con los datos del alumno seleccionado"""
        seleccion = self.tabla_alumnos.selection()
        if not seleccion:
            return

        datos = self.tabla_alumnos.item(seleccion[0],"values")

        for i in self.listas_entrada:
            i.delete(0,"end")

        self.entrada_nombre.insert(0,datos[1])
        self.entrada_apellido.insert(0,datos[2])
        self.entrada_dni.insert(0,datos[3])
        self.entrada_correo.insert(0,datos[4])


    def _obtener_datos(self):
        """Obtiene los datos ingresados y los devuelve en un diccionario"""
        return {
            "nombre": self.entrada_nombre.get().strip(),
            "apellido": self.entrada_apellido.get().strip(),
            "dni": self.entrada_dni.get().strip(),
            "correo": self.entrada_correo.get().strip()
        }


    def _borrar_entradas(self):
        """Borra todos los campos de entrada"""
        for entrada in self.listas_entrada:
            entrada.delete(0,"end")


    def llenar_arbol(self,datos):
        """Inserta un alumno nuevo en la tabla"""
        self.tabla_alumnos.insert("","end",values=(
            datos["id_alumno"],
            datos["nombre"],
            datos["apellido"],
            datos["dni"],
            datos["correo"]
        ))


    def _cargar_arbol_alumnos(self):
        """Hace una petición GET para traer los alumnos"""
        try:
            alumnos = requests.get("http://127.0.0.1:8000/alumnos",timeout=5)
            if alumnos.status_code == 200:
                self._cargar_alumnos(alumnos.json())
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO TRAER LOS ALUMNOS CORRECTAMENTE",
                    "cancel","OK",None)


    def _cargar_alumnos(self,alumnos):
        """Recorre la lista y los carga en la tabla"""
        for alumno in alumnos:
            self.tabla_alumnos.insert("","end",values=(
                alumno["id_alumno"],
                alumno["nombre"],
                alumno["apellido"],
                alumno["dni"],
                alumno["correo"]
            ))


    def nuevo_alumno(self):
        """Limpia selección y campos para ingresar un nuevo alumno"""
        seleccion = self.tabla_alumnos.selection()
        if seleccion:
            self.tabla_alumnos.selection_remove(seleccion[0])
        self._vaciar_entradas()


    def guardar_alumno(self):
        """Envía los datos al backend para guardar un alumno"""
        datos = self._obtener_datos()
        for i in datos.values():
            if i == "":
                return Mensaje(self,"ERROR","COMPLETE LOS CAMPOS!","cancel","OK",None)

        try:
            pedido = requests.post("http://127.0.0.1:8000/alumnos",json=datos,timeout=5)
            if pedido.status_code == 200:
                alumno = pedido.json()
                self.llenar_arbol(alumno)
                self._vaciar_entradas()
                Mensaje(self,"GUARDADO","SE HA GUARDADO CORRECTAMENTE EL ALUMNO","check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO GUARDAR EL ALUMNO CORRECTAMENTE",
                    "cancel","OK",None)


    def _retornar_id(self,columna):
        """Devuelve el id del alumno seleccionado"""
        id_columna = columna[0]
        datos = self.tabla_alumnos.item(id_columna,"values")
        return datos[0]


    def _eliminar_columna(self,columna):
        """Elimina una fila de la tabla"""
        self.tabla_alumnos.delete(columna)


    def eliminar_alumno(self):
        """Elimina el alumno seleccionado"""
        seleccion = self.tabla_alumnos.selection()
        if not seleccion:
            return Mensaje(self,"ERROR","NO SE HA SELECCIONADO NINGUNA COLUMNA","warning","OK",None)

        id_alumno = int(self._retornar_id(seleccion))

        try:
            pedido = requests.delete(f"http://127.0.0.1:8000/alumnos/{id_alumno}",timeout=5)
            if pedido.status_code == 200:
                self.tabla_alumnos.selection_remove(seleccion[0])
                self._eliminar_columna(seleccion[0])
                self._vaciar_entradas()
                Mensaje(self,"ELIMINADO","SE HA ELIMINADO CORRECTAMENTE EL ALUMNO","check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO ELIMINAR EL ALUMNO","cancel","OK",None)


    def actualizar_alumno(self):
        """Actualiza los datos del alumno seleccionado"""
        seleccion = self.tabla_alumnos.selection()
        if not seleccion:
            return Mensaje(self,"ERROR","NO SE HA SELECCIONADO NINGUNA COLUMNA","warning","OK",None)

        id_alumno = int(self._retornar_id(seleccion))
        datos = self._obtener_datos()

        try:
            pedido  = requests.put(f"http://127.0.0.1:8000/alumnos/{id_alumno}",json=datos,timeout=5)
            if pedido.status_code == 200:
                self.tabla_alumnos.selection_remove(seleccion[0])
                alumno = pedido.json()
                self.actualizar_arbol(seleccion,alumno)
                self._vaciar_entradas()
                Mensaje(self,"ACTUALIZADO","SE HA ACTUALIZADO CORRECTAMENTE EL ALUMNO","check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO ACTUALIZAR EL ALUMNO CORRECTAMENTE",
                    "cancel","OK",None)


    def actualizar_arbol(self,id_tabla,alumno):
        """Actualiza los datos de una fila en la tabla"""
        self.tabla_alumnos.item(id_tabla,values=(
            alumno["id_alumno"],
            alumno["nombre"],
            alumno["apellido"],
            alumno["dni"],
            alumno["correo"]
        ))
