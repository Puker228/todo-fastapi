from fastapi import APIRouter, HTTPException, Depends

from users.schema import SUserRegister
from users.crud import UsersCRUD
from auth.utils import get_password_hash


router = APIRouter(prefix="/auth", tags=["Auth and users"])


@router.post("/register")
async def register_user(user_data: SUserRegister = Depends()):
    existing_user = await UsersCRUD.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersCRUD.add_one(email=user_data.email, password=hashed_password)
