from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@app.post("/enroll/")
def enroll(enroll_data: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    if crud.enroll_student(db, enroll_data):
        return {"message": "Enrolled successfully"}
    raise HTTPException(404, "Student or course not found")

@app.get("/students/{id}", response_model=schemas.StudentWithCourses)
def get_student(id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, id)
    if not student:
        raise HTTPException(404, "Student not found")
    return student

@app.get("/courses/{id}", response_model=schemas.CourseWithStudents)
def get_course(id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, id)
    if not course:
        raise HTTPException(404, "Course not found")
    return course

@app.get("/students/", response_model=List[schemas.Student])
def list_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_students(db, skip, limit)

@app.get("/courses/", response_model=List[schemas.Course])
def list_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_courses(db, skip, limit)
