from sqlalchemy import String, Integer, Column
from .database import Base


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
