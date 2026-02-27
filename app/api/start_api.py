import threading
import uvicorn
from api.app_api import app as fst_api


def levantar_api():
    """Levanta el servidor FastAPI con uvicorn"""

    uvicorn.run(
        fst_api,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )


def iniciar_api_en_background():
    """Inicia la API en un hilo en segundo plano"""

    thread = threading.Thread(
        target=levantar_api,
        daemon=True
    )
    thread.start()