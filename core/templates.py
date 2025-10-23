from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


def setup_templates(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return Jinja2Templates(directory="templates")