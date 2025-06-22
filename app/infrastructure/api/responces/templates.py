from icecream import ic

from infrastructure.api.responces.models import ResponseModel, Meta
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response

response_router = APIRouter()

async def get_success_json_response(data: dict, cookies: list[dict] | None = None):
    body = ResponseModel(
        meta=Meta(
            code=200,
            message="OK",
            description="Item fetched successfully"
        ),
        result=data
    )
    response = JSONResponse(content=body.model_dump(), status_code=200, )
    if cookies:
        await set_cookies(response=response, cookies=cookies)
    return response



async def set_cookies(response: JSONResponse, cookies: list[dict]):
        _httponly = True
        _secure = False
        _samesite = "lax"
        _path = "/"

        for cookie in cookies:

            response.set_cookie(
                key=cookie.get("key"),
                value=cookie.get("value"),
                httponly=_httponly, secure=_secure, samesite=_samesite, path=_path
            )

