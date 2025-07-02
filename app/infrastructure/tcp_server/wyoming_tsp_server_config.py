import asyncio
import logging
from functools import partial

from wyoming.server import AsyncServer
from infrastructure.tcp_server.whisper_hailo_event_handler import WhisperHailoEventHandler
from infrastructure.wyoming.responses import wyoming_info

system_logger = logging.getLogger(__name__)


async def start_tcp_server():
    server = AsyncServer.from_uri("tcp://0.0.0.0:10300")
    await server.start(partial(WhisperHailoEventHandler, wyoming_info))
