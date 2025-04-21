# main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()

# Autoriser les requêtes du frontend Angular (localhost:4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # origine Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Modèle de données d'un étudiant
class Student(BaseModel):
    id: int
    name: str
    age: int

# Base de données simulée (liste d'étudiants)
students_db: List[Student] = [
    Student(id=1, name="Alice", age=21),
    Student(id=2, name="Bob", age=22),
    Student(id=3, name="Charlie", age=23),
]

@app.get("/students", response_model=List[Student])
def get_students():
    """Retourne tous les étudiants"""
    return students_db

@app.post("/students", response_model=Student)
def add_student(student: Student):
    """Ajoute un étudiant à la base"""
    students_db.append(student)
    return student

