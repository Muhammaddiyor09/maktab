from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db import database
from functions.school import add_school, updade_school, delete_school
from models.school import School
from schema.school import SchemaSchool
from utils.pagination import pagination

school_router = APIRouter()


@school_router.get("/get_schools")
def get_school(page: int = Query(gt=0), limit: int = Query(gt=0, lt=25), db: Session = Depends(database)):
    try:
        return pagination(School, page, limit, db)
    except Exception as e:
        raise e


@school_router.post("/add_school")
def add_schools(form: SchemaSchool, db: Session = Depends(database)):
    try:
        return add_school(form, db)
    except Exception as e:
        return e


@school_router.put("/update_school")
def updates_schools(ident: int, form: SchemaSchool, db: Session = Depends(database)):
    try:
        return updade_school(ident, form, db)
    except Exception as e:
        return e


@school_router.delete("/delate_school")
def delete_schools(ident: int, db: Session = Depends(database)):
    try:
        return delete_school(ident, db)
    except Exception as e:
        return e
