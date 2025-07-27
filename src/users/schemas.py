from pydantic import BaseModel
from src.resumes.schemas import ResumeResponse


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class RegisterResponse(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    is_active: bool


class UserDelete(BaseModel):
    id: int


class EditProfileRequest(BaseModel):
    name: str
    surname: str
    email: str
    new_password: str


class UserPatchResponse(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    is_active: bool


class UserRel(BaseModel):
    resumes: list[ResumeResponse] #type: ignore # noqa
