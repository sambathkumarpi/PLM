# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL (SQLite in this case)
DATABASE_URL = "sqlite:///./plm_system.db"

# Create an engine that can talk to the SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal is the session factory that will provide us with sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
from models import Base
Base.metadata.create_all(bind=engine)
