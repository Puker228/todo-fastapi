import secrets

from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

router = APIRouter(prefix="/demo-auth", tags=["Demo auth"])

security = HTTPBasic()


username_to_passwords = {"admin": "admin", "john": "password"}


static_auth_token_to_username = {
    "78632760c617484597e55174781e8b11": "admin",
    "054096a23303a96cd662911f4f11f0ae": "password",
}


def get_auth_user_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> str:
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


def get_username_by_static_auth_token(
    static_token: str = Header(alias="x-auth-token"),
) -> str:
    if static_token not in static_auth_token_to_username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token invalid"
        )
    return static_auth_token_to_username[static_token]


@router.get("/basic-auth/")
async def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {
        "message": "hi",
        "username": credentials.username,
        "password": credentials.password,
    }


@router.get("/basic-auth-username/")
async def demo_basic_auth_username(
    auth_username: str = Depends(get_auth_user_username),
):
    return {
        "message": f"hi, {auth_username}",
        "username": auth_username,
    }


@router.get("/some-http-header-auth/")
async def demo_auth_some_http_header(
    username: str = Depends(get_username_by_static_auth_token),
):
    return {
        "message": f"hi, {username}",
        "username": username,
    }
