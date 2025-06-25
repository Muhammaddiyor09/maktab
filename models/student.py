from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    grade = Column(Integer, nullable=False)
    school_id = Column(Integer, ForeignKey("school.id"), nullable=False)
    science = Column(String(40), nullable=False)

    school = relationship("School", back_populates="student")
