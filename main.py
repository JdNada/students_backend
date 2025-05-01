from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from database import departments_db, formations_db
from models import Student, Departement, Formation

app = FastAPI()

# Pour autoriser les requêtes Angular (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ En prod : restreindre l'origine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèle Pydantic
class Student(BaseModel):
    id :int
    name: str
    lastName: str
    age: int

# Simulation d'une "base de données" (en mémoire pour l'exemple)
students_db: List[Student] = []

# Route pour ajouter un étudiant
@app.post("/students/", response_model=Student)
def add_student(student: Student):
    students_db.append(student)
    return student
# Route pour supprimer un étudiant par son id
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    # Recherche l'étudiant avec l'ID spécifié
    student = next((s for s in students_db if s.id == student_id), None)

    if student is None:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")

    # Suppression de l'étudiant de la liste
    students_db.remove(student)
    return {"message": f"Étudiant avec l'id {student_id} supprimé"}

# Route pour obtenir la liste des étudiants
@app.get("/students/", response_model=List[Student])
def get_students():
    return students_db

@app.get("/departments", response_model=List[Departement])
def get_departments():
    return departments_db

# === ROUTES FORMATIONS ===
@app.get("/formations", response_model=List[Formation])
def get_formations():
    return formations_db
