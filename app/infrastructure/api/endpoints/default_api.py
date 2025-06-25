import logging
from fastapi import APIRouter, Response, FastAPI, Request
from icecream import ic
from fastapi.responses import JSONResponse
router = APIRouter()

system_logger = logging.getLogger(__name__)
def config(app: FastAPI):
    app.include_router(router)

@router.get("/")
async def default_handler():
    return {"response": "It is working"}




