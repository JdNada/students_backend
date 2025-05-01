from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Departement, Formation

# Exemple avec SQLite (modifie pour PostgreSQL si nécessaire)
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
departments_db = [
    Departement(id=1, name="Informatique"),
    Departement(id=2, name="Mathématiques"),
    Departement(id=3, name="Physique"),
]

formations_db = [
    Formation(id=1, title="Python Avancé"),
    Formation(id=2, title="Analyse de données"),
    Formation(id=3, title="Réseaux informatiques"),
]
