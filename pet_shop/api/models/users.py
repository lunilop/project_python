__all__ = [
    "BaseUser",
    "LoginUser",
    "PublicStoredUser",
    "PrivateStoredUser",
    "CreationUser",
    "UpdationUser",
]

from enum import Enum
from pydantic import BaseModel, Field, AliasChoices, EmailStr, field_validator
from pydantic_mongo import PydanticObjectId


class CreationRole(str, Enum):
    customer = "customer"
    employee = "employee"

class Role(str, Enum):
    admin = "admin"
    customer = "customer"
    employee = "employee"


class BaseUser(BaseModel):
    username: str
    role: Role = Role.customer
    email: str = Field(default=None)
    image: str | None = Field(default=None)
    
    # @field_validator("email")
    # def validate_email(cls, email):
    #     if not email or "@" not in email:
    #         raise ValueError("A valid email address is required.")
    #     return email


class UpdationUser(BaseUser):
    username: str = Field(default=None)
    role: Role = Field(default=None)
    email: str = Field(default=None)
    image: str | None = Field(default=None)


class CreationUser(BaseUser):
    role: CreationRole = CreationRole.customer
    password: str

    # @field_validator("password")
    # def password_strength(cls, value):
    #     if len(value) < 8:
    #         raise ValueError("Password must be at least 8 characters long.")
    #     return value


class LoginUser(BaseModel):
    username: str
    password: str


class PublicStoredUser(BaseUser):
    id: PydanticObjectId = Field(validation_alias=AliasChoices("_id", "id"))


class PrivateStoredUser(BaseUser):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
