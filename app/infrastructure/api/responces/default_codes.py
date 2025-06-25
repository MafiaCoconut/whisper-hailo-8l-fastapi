from fastapi import HTTPException

from infrastructure.api.responces.models import ResponseModel

responses = {
    '200': {"model": ResponseModel, 'description': "OK"},
    '201': {"model": ResponseModel, 'description': "Created"},
    '204': {'description': "No content"},
    '400': {"model": ResponseModel, 'description': "Bad Request"},
    '401': {"model": ResponseModel, 'description': "Unauthorized"},
    '403': {"model": ResponseModel, 'description': "Forbidden"},
    '404': {"model": ResponseModel, 'description': "Not found"},
    '409': {"model": ResponseModel, 'description': "Conflict"},
    '422': {"model": ResponseModel, 'description': "Validation Error"},
    '500': {"model": ResponseModel, 'description': "Internal Server Error"},
}

async def raise_created() -> None:
    raise HTTPException(status_code=201, detail="Created")

async def raise_item_not_found() -> None:
    raise HTTPException(status_code=404, detail="Item not found")

async def raise_unauthorized() -> None:
    raise HTTPException(status_code=401, detail="Unauthorized")

async def raise_validation_error(detail: str = "") -> None:
    raise HTTPException(status_code=422, detail="Validation error" + ("" if detail == "" else f": {detail}"))

async def raise_internal_server_error() -> None:
    raise HTTPException(status_code=500, detail="Internal server error")

