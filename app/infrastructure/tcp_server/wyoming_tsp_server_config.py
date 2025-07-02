import asyncio
import logging

from wyoming.server import AsyncServer
from infrastructure.tcp_server.tcp_handler import handle_wyoming

system_logger = logging.getLogger(__name__)


async def start_tcp_server():
    server = AsyncServer()
    server = await asyncio.start_server(
        handle_wyoming, host="0.0.0.0", port=10300
    )
    system_logger.info(f"Wyoming TCP running on 0.0.0.0:10300")
    async with server:
        await server.serve_forever()