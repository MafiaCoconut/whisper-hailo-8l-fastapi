import logging
from fastapi import APIRouter, Response, FastAPI, Request, BackgroundTasks
from fastapi.params import Depends

from aiogram.types import Update
from icecream import ic

from application.services.telegram_service import TelegramService
from infrastructure.config.bot_config import bot
from infrastructure.config.dispatcher_config import dp
from infrastructure.config.services_config import get_telegram_service

router = APIRouter()

system_logger = logging.getLogger(__name__)
def config(app: FastAPI):
    app.include_router(router)


@router.post("/send_notification_from_device")
async def send_notification_from_device(
        message: str, device: str,
        response: Response, background_tasks: BackgroundTasks,
        telegram_service: TelegramService = Depends(get_telegram_service)):
    await telegram_service.send_notification_from_device(message=message, device=device)
    return {"message": "OK"}


