from CTkMessagebox import CTkMessagebox


class Mensaje(CTkMessagebox):
    """Clase para mostrar mensajes personalizados en la aplicación"""

    def __init__(self,master,titulo,mensaje,icono,opcion_1,opcion_2):
        """Inicializa el mensaje con los parámetros recibidos"""
        super().__init__(master,
                         width=350,
                         title=titulo,
                         message=mensaje,
                         icon=icono,
                         option_1=opcion_1,
                         option_2=opcion_2)