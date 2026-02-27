from tkinter import ttk
from ui.views.mensajes import Mensaje
from CTkCalendar import CTkCalendar
import customtkinter as ctk
import requests


class FrameCurso(ctk.CTkFrame):
    """Frame para gestionar cursos (crear, listar, actualizar y eliminar)"""

    def __init__(self,master):
        """Inicializa la interfaz de cursos y carga los datos en la tabla"""
        super().__init__(master,width=1400,height=800,fg_color="#2A2A2A")

        self.estado_calendario = False
        self.columnas = ["id","grado","division","turno","ciclo_lectivo"]
        self.arbol_cursos(self.columnas)
        self.listar_cursos()

        self.etiqueta_titulo = ctk.CTkLabel(self,text="CURSOS",font=("Consolas",50))
        self.etiqueta_titulo.place(x=400,y=50)

        self.plantilla = ctk.CTkLabel(self,width=500,height=400,corner_radius=40,
                                      text="",fg_color="#404040",bg_color="#2A2A2A")
        self.plantilla.place(x=250,y=170)

        self.etiqueta_grado = ctk.CTkLabel(self,text="GRADO",font=("Consolas",20))
        self.etiqueta_grado.place(x=300,y=200)

        self.etiqueta_division = ctk.CTkLabel(self,text="DIVISION",font=("Consolas",20))
        self.etiqueta_division.place(x=300,y=250)

        self.etiqueta_turno = ctk.CTkLabel(self,text="TURNO",font=("Consolas",20))
        self.etiqueta_turno.place(x=300,y=300)

        self.etiqueta_ciclo_lectivo = ctk.CTkLabel(self,text="CICLO\nLECTIVO",font=("Consolas",20))
        self.etiqueta_ciclo_lectivo.place(x=300,y=350)

        self.cbox_grado = ctk.CTkComboBox(self,width=210,
                                          values=["1°","2°","3°","4°","5°","6°"],
                                          justify="center",
                                          variable=ctk.StringVar(value="Seleccione uno de los grados"),
                                          state="readonly")
        self.cbox_grado.place(x=400,y=200)

        self.cbox_division = ctk.CTkComboBox(self,width=250,
                                             values=["A","B","C","D"],
                                             justify="center",
                                             variable=ctk.StringVar(value="Seleccione una de las divisiones"),
                                             state="readonly")
        self.cbox_division.place(x=400,y=250)

        self.cbox_turno = ctk.CTkComboBox(self,width=210,
                                          values=["Mañana","Tarde","Noche"],
                                          justify="center",
                                          state="readonly",
                                          variable=ctk.StringVar(value="Seleccione uno de los turnos"))
        self.cbox_turno.place(x=400,y=300)

        self.entrada_ciclo_lectivo = ctk.CTkEntry(self,width=200,
                                                  placeholder_text="Ciclo lectivo XX/XX/XXXX...",
                                                  placeholder_text_color="#3aaaff")
        self.entrada_ciclo_lectivo.place(x=400,y=350)

        self.lista_cbox= [self.cbox_grado,self.cbox_division,self.cbox_turno]

        self.calendario = CTkCalendar(self)

        self.boton_calendario = ctk.CTkButton(self,text="📅",width=30,
                                              command=self.mostrar_calendario)
        self.boton_calendario.place(x=600,y=350)

        self.boton_guardar = ctk.CTkButton(self,text="GUARDAR",corner_radius=30,
                                           fg_color="#50c735",bg_color="#404040",
                                           font=("Consolas",20),hover_color="#4be628",
                                           command=self.guardar_curso)
        self.boton_guardar.place(x=500,y=450)

        self.boton_eliminar = ctk.CTkButton(self,text="ELIMINAR",corner_radius=30,
                                            fg_color="#c73535",bg_color="#404040",
                                            font=("Consolas",20),hover_color="#e62828",
                                            command=self.eliminar_curso)
        self.boton_eliminar.place(x=500,y=500)

        self.boton_actualizar = ctk.CTkButton(self,text="ACTUALIZAR",corner_radius=30,
                                              fg_color="#c78a35",bg_color="#404040",
                                              font=("Consolas",20),hover_color="#e68d28",
                                              command=self.actualizar_curso)
        self.boton_actualizar.place(x=350,y=500)

        self.boton_nuevo = ctk.CTkButton(self,text="NUEVO",corner_radius=30,
                                         fg_color="#3574c7",bg_color="#404040",
                                         font=("Consolas",20),hover_color="#287ee6",
                                         command=self.nuevo_curso)
        self.boton_nuevo.place(x=350,y=450)

        self.mostrar_calendario()
        self.tabla_cursos.bind("<<TreeviewSelect>>",self._llenar_entradas)
        self.bind("<Button-1>",lambda e: self.calendario.place_forget())

    def arbol_cursos(self,columnas):
        """Crea la tabla donde se muestran los cursos"""
        self.tabla_cursos = ttk.Treeview(self,columns=columnas,
                                         show="headings",height=30)

        for i in columnas:
            self.tabla_cursos.heading(i,text=i.upper())

        for i in columnas:
            if i == "id":
                self.tabla_cursos.column(i,width=0,minwidth=0,stretch=False)
            else:
                self.tabla_cursos.column(i,minwidth=140,width=140,stretch=False)

        self.tabla_cursos.column("#0",minwidth=0,width=0,stretch=False)
        self.tabla_cursos.place(x=1030,y=200)

    def _llenar_entradas(self,event):
        """Llena los campos con los datos del curso seleccionado"""
        seleccion = self.tabla_cursos.selection()
        if not seleccion:
            return

        self._vaciar_entradas()
        datos = self.tabla_cursos.item(seleccion[0],"values")

        self.cbox_grado.set(value=datos[1])
        self.cbox_division.set(value=datos[2])
        self.cbox_turno.set(value=datos[3])
        self.entrada_ciclo_lectivo.insert(0,datos[4])

    def mostrar_calendario(self):
        """Muestra u oculta el calendario"""
        if self.estado_calendario:
            self.calendario = CTkCalendar(self,command=self.insertar_fecha)
            self.calendario.place(x=610,y=350)
        else:
            self.calendario.place_forget()

        self.estado_calendario = not self.estado_calendario

    def insertar_fecha(self,fecha):
        """Inserta la fecha seleccionada en el campo ciclo lectivo"""
        self.entrada_ciclo_lectivo.delete(0,"end")
        self.entrada_ciclo_lectivo.insert(0,fecha)

    def _vaciar_entradas(self):
        """Limpia todos los campos de entrada"""
        self.cbox_grado.set("")
        self.cbox_turno.set("")
        self.cbox_division.set("")
        self.entrada_ciclo_lectivo.delete(0,"end")

    def _obtener_datos(self):
        """Obtiene los datos ingresados y los devuelve en un diccionario"""
        if self.cbox_grado.get() in ["Seleccione uno de los grados",""]:
            return
        if self.cbox_division.get() in ["Seleccione una de las divisiones",""]:
            return
        if self.cbox_turno.get() in ["Seleccione uno de los turnos",""]:
            return
        if self.entrada_ciclo_lectivo.get().strip() == "":
            return

        return {
            "grado": self.cbox_grado.get(),
            "division": self.cbox_division.get(),
            "turno": self.cbox_turno.get(),
            "ciclo_lectivo": self.entrada_ciclo_lectivo.get().strip()
        }

    def _actualizar_curso_arbol(self,columna,curso):
        """Actualiza una fila de la tabla con nuevos datos"""
        self.tabla_cursos.item(columna,values=(curso["id_curso"],
                                               curso["grado"],
                                               curso["division"],
                                               curso["turno"],
                                               curso["ciclo_lectivo"]))

    def _llenar_arbol(self,curso):
        """Inserta un nuevo curso en la tabla"""
        self.tabla_cursos.insert("","end",values=(curso["id_curso"],
                                                 curso["grado"],
                                                 curso["division"],
                                                 curso["turno"],
                                                 curso["ciclo_lectivo"]))

    def guardar_curso(self):
        """Envía los datos al backend para guardar un curso"""
        datos = self._obtener_datos()
        if not datos:
            return Mensaje(self,"ERROR","COMPLETE LOS CAMPOS!","cancel","OK",None)

        try:
            pedido = requests.post("http://127.0.0.1:8000/cursos",json=datos,timeout=5)
            if pedido.status_code == 200:
                self._llenar_arbol(pedido.json())
                self._vaciar_entradas()
                Mensaje(self,"GUARDADO","SE HA GUARDADO CORRECTAMENTE EL CURSO",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO GUARDAR EL CURSO CORRECTAMENTE",
                    "cancel","OK",None)

    def _obtener_id(self,columna):
        """Devuelve el id del curso seleccionado"""
        datos = self.tabla_cursos.item(columna,"values")
        return datos[0]

    def _eliminar_columna(self,columna):
        """Elimina una fila de la tabla"""
        self.tabla_cursos.delete(columna)

    def eliminar_curso(self):
        """Elimina el curso seleccionado del backend y de la tabla"""
        seleccion = self.tabla_cursos.selection()
        if not seleccion:
            return Mensaje(self,"ERROR","NO SE HA SELECCIONADO NINGUNA COLUMNA",
                           "warning","OK",None)

        id_curso = self._obtener_id(seleccion[0])

        try:
            pedido = requests.delete(f"http://127.0.0.1:8000/cursos/{id_curso}",timeout=5)
            if pedido.status_code == 200:
                self.tabla_cursos.selection_remove(seleccion[0])
                self._eliminar_columna(seleccion[0])
                self._vaciar_entradas()
                Mensaje(self,"ELIMINADO","SE HA ELIMINADO CORRECTAMENTE EL CURSO",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO ELIMINAR EL CURSO",
                    "cancel","OK",None)

    def nuevo_curso(self):
        """Limpia la selección y los campos para crear un nuevo curso"""
        seleccion = self.tabla_cursos.selection()
        if seleccion:
            self.tabla_cursos.selection_remove(seleccion[0])
        self._vaciar_entradas()

    def _cargar_cursos_tabla(self,cursos):
        """Carga todos los cursos obtenidos del backend en la tabla"""
        for curso in cursos:
            self.tabla_cursos.insert("","end",values=(curso["id_curso"],
                                                     curso["grado"],
                                                     curso["division"],
                                                     curso["turno"],
                                                     curso["ciclo_lectivo"]))

    def listar_cursos(self):
        """Hace una petición GET para traer todos los cursos"""
        try:
            pedido = requests.get("http://127.0.0.1:8000/cursos",timeout=5)
            if pedido.status_code == 200:
                self._cargar_cursos_tabla(pedido.json())
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR","NO SE HA PODIDO TRAER LOS CURSOS",
                    "cancel","OK",None)

    def actualizar_curso(self):
        """Actualiza los datos del curso seleccionado"""
        seleccion = self.tabla_cursos.selection()
        if not seleccion:
            return Mensaje(self,"ERROR","NO SE HA SELECCIONADO NINGUNA COLUMNA",
                           "warning","OK",None)

        datos = self._obtener_datos()
        id_curso = self._obtener_id(seleccion[0])

        try:
            pedido = requests.put(f"http://127.0.0.1:8000/cursos/{id_curso}",
                                  json=datos,timeout=5)
            if pedido.status_code == 200:
                self._actualizar_curso_arbol(seleccion[0],pedido.json())
                self.tabla_cursos.selection_remove(seleccion[0])
                self._vaciar_entradas()
                Mensaje(self,"ACTUALIZADO",
                        "SE HA ACTUALIZADO CORRECTAMENTE EL CURSO",
                        "check","OK",None)
        except requests.exceptions.RequestException:
            Mensaje(self,"ERROR",
                    "NO SE HA PODIDO ACTUALIZAR EL CURSO CORRECTAMENTE",
                    "cancel","OK",None)