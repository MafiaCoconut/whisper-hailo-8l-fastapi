from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
import asyncio
from infrastructure.api import api_config, cors
from infrastructure.config import whisper_hailo
from infrastructure.tcp_server.wyoming_tsp_server_config import start_tcp_server
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

    system_logger.info(f"HAILO_VERSION: {os.getenv('HAILO_VERSION')}")
    system_logger.info(f"IS_HAILO_ON_DEVICE: {os.getenv('IS_HAILO_ON_DEVICE')}")

    system_logger.info("Starting Whyoming TCP server")
    system_logger.info(f"response exist: {os.path.isfile('common/wyoming_describe_response.json')}")

    asyncio.create_task(start_tcp_server())

    system_logger.info("Program is started")
    yield
    system_logger.info("Program is stopping")
    # if os.getenv("IS_HAILO_ON_DEVICE") == "TRUE":
    #     whisper_hailo.whisper_hailo_stop()
    system_logger.info("Program is stopped")


app.router.lifespan_context = lifespan
