from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./deployment.db"

# Important for FastAPI: allows access from multiple threads
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()


# Dependency (you will use this in your routes/services)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
