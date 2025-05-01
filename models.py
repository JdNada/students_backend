# models.py
from pydantic import BaseModel
from typing import List

class Departement(BaseModel):
    id: int
    name: str

class Formation(BaseModel):
    id: int
    title: str


class Student(BaseModel):
    id: int
    name: str
    lastName: str
    age: int
    departement_id: int
    formation_ids: List[int]

