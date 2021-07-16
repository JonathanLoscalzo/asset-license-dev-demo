from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginUser(BaseModel):
    username: str
    password: str  # in db this is hashed
    disabled: bool = False


class TokenData(BaseModel):
    username: str
