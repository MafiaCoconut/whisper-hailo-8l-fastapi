from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from infrastructure.api import api_config, cors
from infrastructure.config import whisper_hailo
app = FastAPI()

cors.config(app=app)
system_logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    system_logger.info("Program is starting")

    system_logger.info("API configuration is started")
    api_config.config(app=app)

    system_logger.info("Program is started")
    yield
    system_logger.info("Program is stopping")
    if os.getenv("IS_HAILO_ON_DEVICE") == "TRUE":
        whisper_hailo.whisper_hailo_stop()
    system_logger.info("Program is stopped")


app.router.lifespan_context = lifespan
