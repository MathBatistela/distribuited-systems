import sys
from database.db import Enrollment, Student, Subject, session

sys.path.append("..")


def create_student(context: dict) -> dict:
    student = Student()

    for attr in context.keys():
        setattr(student, attr, context[attr])

    student.save()
    return student.asdict()


def get_students() -> list:
    return list(map(lambda o: o.asdict(), session.query(Student).all()))

def get_students_by_enrollment(search: dict) -> list:
    query = session.query(Enrollment)
    for attr,value in search.items():
        query = query.filter( getattr(Enrollment,attr)==value )
    return list(map(lambda o: o.student.asdict(), query.all()))


def get_student(ra: int) -> dict:
    return (session.query(Student).get(ra)).asdict()


def update_student(context: dict) -> dict:
    student = session.query(Student).get(context["ra"])

    if student:
        for attr in context.keys():
            setattr(student, attr, context[attr])

        student.save()

        return student.asdict()


def remove_student(ra: int) -> dict:
    student = session.query(Student).get(ra)

    if student:
        session.delete(student)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
