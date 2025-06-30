import math
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload
from db import database
from functions.student import add_student, updade_student, delete_student
from models.student import Student
from schema.student import SchemaStudent

student_router = APIRouter()


@student_router.get("/get_students")
def get_student(page: int = Query(gt=0), limit: int = Query(gt=0, lt=25), db: Session = Depends(database)):
    try:
        offset = (page - 1) * limit
        page_count = db.query(Student).count()
        result = db.query(Student).limit(limit).offset(offset).options(joinedload(Student.school)).all()
        return {
            "page": page,
            "limit": limit,
            "page_count": math.ceil(page_count / limit),
            "data": result
        }
    except Exception as e:
        raise e


@student_router.post("/add_student")
def add_students(form: SchemaStudent, db: Session = Depends(database)):
    try:
        return add_student(form, db)
    except Exception as e:
        return e


@student_router.put("/update_student")
def updates_students(ident: int, form: SchemaStudent, db: Session = Depends(database)):
    try:
        return updade_student(ident, form, db)
    except Exception as e:
        return e


@student_router.delete("/delate_student")
def delete_students(ident: int, db: Session = Depends(database)):
    try:
        return delete_student(ident, db)
    except Exception as e:
        return e
