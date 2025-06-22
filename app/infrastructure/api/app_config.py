from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from infrastructure.api import api_config, cors
from infrastructure.config import logs_config
from infrastructure.config import whisper_hailo

# from infrastructure.config.services_config import get_scheduler_service
# from infrastructure.config import telegram_config
app = FastAPI()

cors.config(app=app)
system_logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    system_logger.info("Program is starting")
    # scheduler_service = get_scheduler_service()
    # await scheduler_service.set_all_jobs()

    # logs_config.config()
    api_config.config(app=app)
    whisper_hailo.config()

    # await telegram_config.config()
    # ic(await scheduler_service.get_all_jobs())
    yield
    system_logger.info("Program is stopping")
    whisper_hailo.whisper_hailo_stop()
    system_logger.info("Program is stopped")


app.router.lifespan_context = lifespan
