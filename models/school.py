from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db import Base


class School(Base):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    student_count = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="school")

