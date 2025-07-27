from typing import Any
from fastapi.routing import APIRouter
from src.resumes.schemas import ResumeResponse
from src.users.models import User
from src.users.schemas import LoginResponse, RegisterResponse, UserPatchResponse
from src.users.service import UserCRUD
from fastapi import Form, HTTPException, status
from src.users.utils import hash_password, verify_password, create_access_token
from src.utils import permission_required


router = APIRouter(prefix='/users')


@router.post('/register', response_model=RegisterResponse)
async def register_user(
    name: str,
    surname: str,
    email: str,
    password: str,
    repeat_password: str
) -> Any:

    if password != repeat_password:
        raise ValueError('Пароли не совпадают')
    result = await UserCRUD.get_user_by_email(email)

    if result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Пользователь с таким email уже существует'
        )

    user = User(
        name=name,
        surname=surname,
        email=email,
        password=hash_password(password),
        is_active=True
    )

    return await UserCRUD.create(user)


@router.post('/login', response_model=LoginResponse)
async def login_user(
    username: str = Form(...),
    password: str = Form(...)
) -> LoginResponse:
    print("login")
    user = await UserCRUD.get_user_by_email(username)
    print(user)
    if not user or user.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден'
        )

    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Неверный пароль'
        )

    access_token = create_access_token(data={"sub": user.email})

    return LoginResponse(access_token=access_token, token_type='bearer')


@router.patch('/editprofile', response_model=UserPatchResponse)
async def edit_user_profile(
    name: str,
    surname: str,
    email: str,
    new_password: str,
    current_user: User = permission_required(router.prefix)
) -> Any:

    if new_password == current_user.password:
        raise ValueError('Пароль должен отличаться от старого!')

    updated_user = UserPatchResponse(
        name=name,
        surname=surname,
        email=email,
        password=hash_password(new_password),
        is_active=True
    )

    return await UserCRUD.update_by_id(current_user.id, updated_user)


@router.patch('/delete', response_model=UserPatchResponse)
async def delete_user_profile(
    current_user: User = permission_required(router.prefix)
) -> Any:
    deleted_user = UserPatchResponse(
        name=current_user.name,
        surname=current_user.surname,
        email=current_user.email,
        password=current_user.password,
        is_active=False
    )

    return await UserCRUD.update_by_id(current_user.id, deleted_user)


@router.get('/resumes')
async def get_user_resumes(
    current_user: User = permission_required(router.prefix)
) -> list[ResumeResponse]:
    return await UserCRUD.get_resumes_by_user_id(current_user.id)
