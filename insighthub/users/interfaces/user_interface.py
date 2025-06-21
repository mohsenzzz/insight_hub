
from pydantic import BaseModel

class UserInterface(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str
    email: str
    password: str

class UserPutInterface(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str
    email: str

class UserPatchInterface(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str | None
    email: str | None

