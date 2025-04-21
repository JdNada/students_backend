from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Departement(Base):
    __tablename__ = "departements"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    students = relationship("Student", back_populates="departement")

class Formation(Base):
    __tablename__ = "formations"
    id = Column(Integer, primary_key=True, index=True)
    theme = Column(String, unique=True, index=True)
    students = relationship("Student", back_populates="formation")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    departement_id = Column(Integer, ForeignKey("departements.id"))
    formation_id = Column(Integer, ForeignKey("formations.id"))

    departement = relationship("Departement", back_populates="students")
    formation = relationship("Formation", back_populates="students")
