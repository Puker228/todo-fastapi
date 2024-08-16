from fastapi import APIRouter

from app.schemas.user_schemas import SUserRegister


router = APIRouter(prefix="/auth", tags=["Auth and users"])


@router.post("/register")
async def register_user(user_data: SUserRegister):
    pass
