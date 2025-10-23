from fastapi.staticfiles import StaticFiles
from api import status
from views import home
import logging


def configure_logging():
    logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="{asctime} [{levelname}] {name}: {message}",
                    style="{")

    logging.getLogger("watchfiles").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


def configure_routing(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(status.router)
    app.include_router(home.router)