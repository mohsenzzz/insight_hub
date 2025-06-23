from pydantic import BaseModel


class TaskInputInterface(BaseModel):
    name: str
    type:str

class TaskCreatePutInterface(BaseModel):
    name: str
    description: str|None
    taskInput: list[TaskInputInterface]