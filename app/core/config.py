from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api import status
from views import home
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


def configure_logging():
    logging.basicConfig(filename="logs/app.log",
                    level=logging.INFO,
                    format="{asctime} [{levelname}] {name}: {message}",
                    style="{")

    logging.getLogger("watchfiles").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


def configure_routing(app):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    app.include_router(status.router)
    app.include_router(home.router)


def configure_templates():
    return Jinja2Templates(directory=TEMPLATES_DIR)