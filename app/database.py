
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Emplacement de la base de données SQLite
DATABASE_URL = "sqlite:///./gerbeble.db"

# Connexion à la base de données
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Création des sessions de travail
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe de base des modèles
class Base(DeclarativeBase):
    pass


# Fournit une session à chaque opération de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()