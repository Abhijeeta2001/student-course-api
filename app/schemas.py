from pydantic import BaseModel, EmailStr
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase): pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase): pass

class Course(CourseBase):
    id: int
    class Config:
        orm_mode = True

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class StudentWithCourses(Student):
    courses: List[Course] = []

class CourseWithStudents(Course):
    students: List[Student] = []
