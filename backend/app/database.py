from sqlalchemy.ext.declarative import session_maker, declarative_base
from sqlalchemy import create_engine

USERNAME = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
PORT = "5432"
DATABASE = "recipes"

Base = declarative_base() # all ORM models inherit from this

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    ) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()