from fastapi import HTTPException

from models.school import School
from models.teachers import Teacher


def check_ident(ident, model, db):
    item = db.query(model).filter(model.id == ident).first()
    if not item:
        raise HTTPException(404, "item topilmadi")


def check_school_id(ident, db):
    school = db.query(School).filter(School.id == ident).first()
    if not school:
        raise HTTPException(404, "Bunday iddagi school topilmadi")
    school.student_count += 1


def check_science(science, db):
    science = db.query(Teacher).filter(Teacher.science == science).first()
    if not science:
        raise HTTPException(404, "Bunday science topilmadi")
    science.student_count += 1