from fastapi import HTTPException, FastAPI, Request
from icecream import ic
from starlette.exceptions import HTTPException as StarletteHTTPException
from infrastructure.api.responces.models import ResponseModel, Meta
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.exceptions import RequestValidationError


def rewrite_http_exception_response(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def custom_http_exception_handler(request: Request, exc: HTTPException):
        response = ResponseModel(
            meta=Meta(
                code=exc.status_code,
                message="ERROR",
                description=exc.detail
            ),
            result={}
        )
        return JSONResponse(content=response.model_dump(), status_code=exc.status_code)

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request, exc):
        print(f"OMG! An HTTP error!: {repr(exc)}")
        return await http_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        print(f"OMG! The client sent invalid data!: {exc}")
        return await request_validation_exception_handler(request, exc)
