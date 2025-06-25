import logging
import inspect
from dotenv import load_dotenv
import os
from functools import wraps

from icecream import ic
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import coloredlogs

load_dotenv()
system_logger = logging.getLogger(__file__)
error_logger = logging.getLogger("error_logger")
apscheduler_logger = logging.getLogger("apscheduler")


fmt =  "%(asctime)s | %(levelname)-8s | %(name)-40s | %(message)s"
datefmt = "%d.%m.%Y-%H:%M"

formatter = logging.Formatter( fmt=fmt, datefmt=datefmt )

system_handler = logging.FileHandler("logs/system_data.log")
system_handler.setFormatter(formatter)

error_handler = logging.FileHandler("logs/error_data.log")
error_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)

def log_decorator(log_level=logging.DEBUG, print_args: bool = False, print_kwargs: bool = False):
    """
    A decorator that outputs information about the called function
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            file_path = inspect.getfile(func)
            file_name = file_path[file_path.rfind("/")+1:]
            msg = f"Called function: {file_name}[{func.__name__}]"
            if print_args:
                msg += f" Args: {args}."
            if print_kwargs:
                msg += f" Kwargs: {kwargs}"

            system_logger.log(level=log_level, msg=msg)
            result = await func(*args, **kwargs)

            return result

        return wrapper
    return decorator

def log_api_decorator(log_level=logging.INFO):
    """
    A decorator that outputs information about the called API function
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            system_logger.log(level=log_level, msg=f"API Called function: {func.__name__}")

            result = await func(*args, **kwargs)

            system_logger.log(level=log_level, msg=f"Result: {result.body}")

            return result

        return wrapper
    return decorator
