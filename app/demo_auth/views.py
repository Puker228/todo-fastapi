import secrets

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

router = APIRouter(prefix="/demo-auth", tags=["Demo auth"])

security = HTTPBasic()


@router.get("/basic-auth/")
async def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {
        "message": "hi",
        "username": credentials.username,
        "password": credentials.password,
    }


username_to_passwords = {"admin": "admin", "john": "password"}


def get_auth_user_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_password = username_to_passwords.get(credentials.username)
    if correct_password is None:
        raise unauthed_exc

    if credentials.username not in username_to_passwords:
        raise unauthed_exc

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"), correct_password.encode("utf-8")
    ):
        raise unauthed_exc

    return credentials.username


@router.get("/basic-auth-username/")
async def demo_basic_auth_username(auth_username: str = Depends(get_auth_user_username)):
    return {
        "message": f"hi, {auth_username}",
        "username": auth_username,
    }
