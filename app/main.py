from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import configure_logging
from api import status
from views import home
from core.config import STATIC_DIR


configure_logging()
app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(status.router)
app.include_router(home.router)
  
