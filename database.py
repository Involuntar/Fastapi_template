from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(f"sqlite:///./{settings.DB_NAME}.sqlite", 
                       connect_args={"check_same_thread": False}) # Отключение проверки того же потока для SQLite

SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False,
                            bind=engine)

Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()