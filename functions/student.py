from models.school import School
from models.student import Student
from models.teachers import Teacher
from utils.check_ident import check_ident, check_school_id, check_science


def add_student(form, db):
    check_school_id(form.school_id, db)
    check_science(form.science, db)
    student = Student(
        name=form.name,
        grade=form.grade,
        school_id=form.school_id,
        science=form.science
    )
    db.add(student)
    db.commit()
    return {"message": "Student muvofaqiytli saqlandi"}


def updade_student(ident, form, db):
    check_ident(ident, Student, db)
    db.query(Student).filter(Student.id == ident).update({
        Student.name: form.name,
        Student.grade: form.grade,
        Student.school_id: form.school_id,
        Student.science: form.science
    })
    db.commit()
    return {"message": "Student tahrirlandi"}


def delete_student(ident, db):
    check_ident(ident, Student, db)
    school = db.query(School).filter(School.id == Student.school_id).first()
    teacher = db.query(Teacher).filter(Teacher.science == Student.science).first()
    school.student_count -= 1
    teacher.student_count -= 1
    db.query(Student).filter(Student.id == ident)
    db.commit()
    return {"message": "Student o'chrildi"}