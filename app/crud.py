from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def enroll_student(db: Session, enrollment: schemas.EnrollmentCreate):
    student = db.query(models.Student).get(enrollment.student_id)
    course = db.query(models.Course).get(enrollment.course_id)
    if student and course:
        student.courses.append(course)
        db.commit()
        return True
    return False

def get_student(db: Session, student_id: int):
    return db.query(models.Student).get(student_id)

def get_course(db: Session, course_id: int):
    return db.query(models.Course).get(course_id)

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Course).offset(skip).limit(limit).all()
