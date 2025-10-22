from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.system_metrics import get_cpu_info, get_disk_usage, get_system_info, get_memory_usage
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


@app.get("/status")
async def get_stats():
    cpu = get_cpu_info()
    disk_usage = get_disk_usage()
    system_info = get_system_info()
    memory_usage = get_memory_usage()
    
    return {"cpu": cpu,
            "disk_usage": disk_usage,
            "system_info": system_info,
            "memory_usage": memory_usage
            }