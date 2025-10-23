from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from core.templates import setup_templates
from core.config import setup_logging
from services.system_metrics import get_system_metrics
from models.metrics import SystemMetrics


setup_logging()
app = FastAPI()
templates = setup_templates(app)

    
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/status", response_model=SystemMetrics)
async def get_stats():
    return get_system_metrics()