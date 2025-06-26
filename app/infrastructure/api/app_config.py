from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from infrastructure.api import api_config, cors
from infrastructure.config import whisper_hailo
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

cors.config(app=app)
system_logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    system_logger.info("Program is starting")

    system_logger.info("API configuration is started")
    api_config.config(app=app)
    whisper_hailo.config(app=app, _model=os.getenv("HAILO_VERSION"))

    print('os.getenv("HAILO_VERSION"): ', os.getenv("HAILO_VERSION"))
    # match os.getenv("HAILO_VERSION"):
    #     case "HAILO-8":
    #     case "HAILO-8L":
    #         whisper_hailo.config(app=app, _model="hailo8l")

    system_logger.info("Program is started")
    yield
    system_logger.info("Program is stopping")
    # if os.getenv("IS_HAILO_ON_DEVICE") == "TRUE":
    #     whisper_hailo.whisper_hailo_stop()
    system_logger.info("Program is stopped")


app.router.lifespan_context = lifespan
