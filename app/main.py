from api.start_api import iniciar_api_en_background
from ui.ui import App
from db.db import creacion_tablas



if __name__ == "__main__":
    creacion_tablas()
    iniciar_api_en_background()
    App().mainloop()

