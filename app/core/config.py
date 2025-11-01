
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
import logging
import os


load_dotenv()

RPI_IP = os.getenv("RPI_IP")

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


def configure_templates():
    return Jinja2Templates(directory=TEMPLATES_DIR)