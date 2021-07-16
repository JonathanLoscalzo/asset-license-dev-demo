from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pymongo.database import Database
from asset_manager.models.auth import LoginUser, Token
from asset_manager.utils.security import (
    authenticate_user,
    create_access_token,
)

from asset_manager.deps import get_current_user, get_db

router = APIRouter(
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/token", response_model=Token)
async def login_for_access_token(
    db: Database = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = authenticate_user(None, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})

    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def read_users_me(current_user: LoginUser = Depends(get_current_user)):
    return current_user
