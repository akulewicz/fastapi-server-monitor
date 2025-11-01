from fastapi import FastAPI
from app.core.config import configure_logging, configure_routing


configure_logging()
app = FastAPI()
configure_routing(app)
  
