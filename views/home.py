from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="home/index.html")
