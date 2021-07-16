from asset_manager.models.auth import LoginUser, TokenData
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

# openssl rand -hex 32
# TODO: secret and algorithm should live in settings object
SECRET_KEY = "a80a56336b41867acd724f0804de2a65d106f9b64aacd03fb7a7d657786e97d0"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def verify_password(plain_password, hashed_password):
    # return pwd_context.verify(plain_password, hashed_password)
    # TODO: should verify if a plain password
    # is the same as hashed => hash(plain) == hashed
    return plain_password == hashed_password


def get_password_hash(password):
    # return pwd_context.hash(password)
    # TODO: should return a hashed password
    return password


def get_user(db, username) -> LoginUser:
    # TODO: should return a user from DB
    return LoginUser(username="admin", password="secure")


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user


def create_access_token(data):
    to_encode = data.copy()
    # to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise JWTError
        return TokenData(username=username)
    except JWTError:
        raise
    except Exception:
        raise
