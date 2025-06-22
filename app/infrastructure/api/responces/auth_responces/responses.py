from pydantic import BaseModel

from domain.user import UserBaseInfo
from infrastructure.api.responces.models import ResponseModel, Meta

class JwtTokensModel(BaseModel):
    access_token: str
    refresh_token: str

class UsersTokensModel(BaseModel):
    access_token: str
    refresh_token: str
    user: UserBaseInfo

class LoginModel(BaseModel):
    access_token: str
    user: UserBaseInfo

class RegistrationResponse(ResponseModel):
    meta: Meta
    result: UsersTokensModel

class LoginResponse(ResponseModel):
    meta: Meta
    result: LoginModel

class RefreshResponse(ResponseModel):
    meta: Meta
    result: JwtTokensModel

class StatusResponse(ResponseModel):
    meta: Meta
    result: bool