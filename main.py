from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.system_metrics import get_cpu_temp, get_disk_usage
import platform
import distro

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

    
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/status")
async def get_stats():
    cpu_temp = get_cpu_temp()
    disk_usage = get_disk_usage()
    system = platform.system()
    release = platform.release()
    distro_name = distro.name(pretty=True)

    return {"cpu_temp": cpu_temp,
            "disk_usage": disk_usage,
            "system": system,
            "release": release,
            "distro_name": distro_name
            }