from sqlalchemy import Column, String, Integer
from db import Base


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    science = Column(String(40), nullable=False)
    student_count = Column(Integer, nullable=False)