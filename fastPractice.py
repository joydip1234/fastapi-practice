from fastapi import FastAPI, Path

from data import students
from typing import Optional

from student import Student, UpdateStudent

app = FastAPI()


@app.get("/")
def hello():
    return "Hello World!"


# example for path parameters
@app.get("/get-students")
def get_student_by_id():
    return students


# example for path parameters
@app.get("/get-by-id/{student_id}")
def get_student_by_id(student_id: int = Path(default=1, description="Enter here the student Id", gt=0, lt=3)):
    return students[student_id]


# example for query parameters
@app.get("/get-by-name")
def get_student_by_name(test: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return test


# example for query parameters
@app.get("/get-by-name-again")
def get_student_by_name(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return test


# combining path parameters and query parameters

@app.get("/get-student/{student_id}")
def get_student(student_id: int, test: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return test


# request body and post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return "Student Exists"
    students[student_id] = student
    return students[student_id]


# put method/method example
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return "Student does not exist"
    if student.name is not None:
        students[student_id].name = student.name

    if student.age is not None:
        students[student_id].age = student.age

    if student.marks is not None:
        students[student_id].marks = student.marks

    return students[student_id]


# delete method example
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return "Student does not exist"
    # students.pop(student_id)
    del students[student_id]
    return "Student deleted successfully"


