from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)


sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()
