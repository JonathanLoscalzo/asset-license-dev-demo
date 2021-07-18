from asset_manager.models.auth import LoginUser
from asset_manager.utils.security import oauth2_scheme, decode_token, get_user
from fastapi import Depends, HTTPException, status
from asset_manager.utils import settings as config
from asset_manager.data.init_db import connect_db, initialize
from functools import lru_cache


@lru_cache()
def get_settings() -> config.Settings:
    return config.Settings()


def get_db(settings: config.Settings = Depends(get_settings)):
    database = connect_db(settings.CONNECTION_STRING, settings.DATABASE_NAME)

    initialize(database)

    return database


async def get_current_user(
    db=Depends(get_db), token: str = Depends(oauth2_scheme)
) -> LoginUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data = decode_token(token)
    except Exception as e:
        raise credentials_exception from e

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is disabled"
        )
    return user

