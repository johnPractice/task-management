from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from .base_model import PyObjectId


class TaskBase(BaseModel):
    name: str
    description: str
    status: str
    custom_fields: Optional[
        Dict[str, Any]
    ] = None  # Custom fields represented as a dictionary


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

    class Config:
        orm_mode = True
