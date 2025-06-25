from models.teachers import Teacher
from utils.check_ident import check_ident


def add_teacher(form, db):
    teacher = Teacher(
        name=form.name,
        science=form.science,
        student_count=0
    )
    db.add(teacher)
    db.commit()
    return {"message": "Teacher muvofaqiytli saqlandi"}


def updade_teacher(ident, form, db):
    db.query(Teacher).filter(Teacher.id == ident).update({
        Teacher.name: form.name,
        Teacher.science: form.science,
    })
    db.commit()
    return {"message": "Teacher tahrirlandi"}


def delete_teacher(ident, db):
    check_ident(ident, Teacher, db)
    db.query(Teacher).filter(Teacher.id == ident)
    db.commit()
    return {"message": "Teacher o'chrildi"}