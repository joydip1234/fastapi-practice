from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    marks: int


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    marks: Optional[int] = None
