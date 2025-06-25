from models.school import School
from utils.check_ident import check_ident


def add_school(form, db):
    school = School(
        name=form.name,
        student_count=0

    )
    db.add(school)
    db.commit()
    return {"message": "School muvofaqiytli saqlandi"}


def updade_school(ident, form, db):
    check_ident(ident, School, db)
    db.query(School).filter(School.id == ident).update({
        School.name: form.name,
    })
    db.commit()
    return {"message": "School tahrirlandi"}


def delete_school(ident, db):
    check_ident(ident, School, db)
    db.query(School).filter(School.id == ident)
    db.commit()
    return {"message": "School o'chrildi"}
