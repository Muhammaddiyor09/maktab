from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from functions.teachers import add_teacher, updade_teacher, delete_teacher
from models.teachers import Teacher
from schema.teachers import SchemaTeacher

teacher_router = APIRouter()


@teacher_router.get("/get_teachers")
def get_teacher(db: Session = Depends(database)):
    try:
        return db.query(Teacher).all()
    except Exception as e:
        raise e


@teacher_router.post("/add_teacher")
def add_teachers(form: SchemaTeacher, db: Session = Depends(database)):
    try:
        return add_teacher(form, db)
    except Exception as e:
        return e


@teacher_router.put("/update_teacher")
def updates_teachers(ident: int, form: SchemaTeacher, db: Session = Depends(database)):
    try:
        return updade_teacher(ident, form, db)
    except Exception as e:
        return e


@teacher_router.delete("/delate_teacher")
def delate_teachers(ident: int, db: Session = Depends(database)):
    try:
        return delete_teacher(ident, db)
    except Exception as e:
        return e
