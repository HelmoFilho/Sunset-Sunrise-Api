## -- Importing External Modules -- ##
from fastapi import APIRouter

## -- Importing Internal Modules -- ##
from src.app.server import app

# Routes

from src.app.resources import sunset_sunrise

# Routing

## V1
app.include_router(sunset_sunrise.router, prefix = "/api/v1")