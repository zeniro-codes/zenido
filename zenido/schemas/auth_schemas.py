from pydantic import BaseModel, EmailStr, SecretStr


class UserRegister(BaseModel):
    username: EmailStr
    password: SecretStr
