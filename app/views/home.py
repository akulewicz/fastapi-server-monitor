from fastapi import APIRouter
from fastapi import Request
from core.config import configure_templates
from fastapi.responses import HTMLResponse


router = APIRouter()

templates = configure_templates()

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="home/index.html")
