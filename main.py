from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.system_metrics import get_system_metrics
from models.metrics import SystemMetrics
import logging

logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="{asctime} [{levelname}] {name}: {message}",
                    style="{")

logging.getLogger("watchfiles").setLevel(logging.WARNING)
logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

    
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/status", response_model=SystemMetrics)
async def get_stats():
    return get_system_metrics()