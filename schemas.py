from pydantic import BaseModel

class DepartementBase(BaseModel):
    name: str

class DepartementCreate(DepartementBase):
    pass

class Departement(DepartementBase):
    id: int
    class Config:
        orm_mode = True

class FormationBase(BaseModel):
    theme: str

class FormationCreate(FormationBase):
    pass

class Formation(FormationBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    age: int
    departement_id: int
    formation_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    departement: Departement
    formation: Formation
    class Config:
        orm_mode = True
