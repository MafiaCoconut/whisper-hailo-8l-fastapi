import logging
from fastapi import APIRouter, Response, FastAPI, Request
from icecream import ic
from fastapi.responses import JSONResponse
router = APIRouter()

system_logger = logging.getLogger(__name__)
def config(app: FastAPI):
    app.include_router(router)


# @router.post("/webhook")
# async def webhook_handler(request: Request):
#     data = await request.json()
#     ic(data)
#     update = Update(**data)
#     # ic(update)
#     try:
#         await dp.feed_update(bot=bot, update=update)
#     except Exception as e:
#         system_logger.error(e)

@router.get("/")
async def default_handler():
    return {"response": "It is working"}




