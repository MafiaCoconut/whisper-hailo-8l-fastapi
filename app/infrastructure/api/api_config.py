from fastapi import FastAPI

from infrastructure.api import cors
from infrastructure.api.endpoints import default_api, whisper_api
from infrastructure.api.responces.exceptions import rewrite_http_exception_response


def configure_endpoints(app: FastAPI):
    default_api.config(app=app)
    whisper_api.config(app=app)


def config_exceptions(app: FastAPI):
    rewrite_http_exception_response(app=app)

def config_cors(app: FastAPI):
    cors.config(app=app)

def config(app: FastAPI):
    config_exceptions(app=app)
    configure_endpoints(app=app)
