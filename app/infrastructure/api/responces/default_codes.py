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


"""
200 OK – Запрос успешно выполнен, и сервер возвращает запрашиваемые данные.

201 Created – Запрос успешно выполнен, и в результате был создан новый ресурс.

204 No Content – Запрос успешно выполнен, но в ответе нет содержимого (например, при удалении ресурса).

400 Bad Request – Сервер не может обработать запрос из-за ошибки клиента (неверный синтаксис, неправильные параметры запроса).

401 Unauthorized – Для доступа к ресурсу требуется аутентификация, либо предоставленные учётные данные неверны или отсутствуют.

403 Forbidden – Доступ к ресурсу запрещён, даже если аутентификация пройдена; у клиента нет достаточных прав.

404 Not Found – Запрашиваемый ресурс не найден на сервере.

405 Method Not Allowed – Используемый HTTP-метод не поддерживается для данного ресурса.

409 Conflict – Возникает конфликт с текущим состоянием ресурса; например, при попытке создать ресурс, который уже существует.

500 Internal Server Error – Общая ошибка сервера, которая не позволяет корректно обработать запрос.

503 Service Unavailable – Сервер временно недоступен (например, из-за технического обслуживания или перегрузки).
"""