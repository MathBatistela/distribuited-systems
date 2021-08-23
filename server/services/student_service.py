"""
Has all the services to manipulate Student data
in database

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

from database.db import Enrollment, Student, Subject, session



def create_student(context: dict) -> dict:
    """Create a Student row in DB

    Args:
        context (dict): Student fields

    Returns:
        dict: Student object as dictionary
    """
    student = Student()

    for attr in context.keys():
        setattr(student, attr, context[attr])

    student.save()
    return student.asdict()


def get_students() -> list:
    """Get all the Students from DB

    Returns:
        list: List of Student objects as dictionary
    """
    return list(map(lambda o: o.asdict(), session.query(Student).all()))


def get_students_by_enrollment(search: dict) -> list:
    """Get all the Students enrolled in a Subject

    Args:
        search (dict): Filter params

    Returns:
        list: List of Student objects as dictionary
    """
    query = session.query(Enrollment)
    for attr, value in search.items():
        query = query.filter(getattr(Enrollment, attr) == value)
    return list(map(lambda o: o.student.asdict(), query.all()))


def get_student(ra: int) -> dict:
    """Get a Student row in DB

    Args:
        ra (int): Student ra

    Returns:
        dict: Student object as dictionary
    """
    return (session.query(Student).get(ra)).asdict()


def update_student(context: dict) -> dict:
    """Update a Student row in DB

    Args:
        context (dict): Student fields to update

    Returns:
        dict: Updated Student objects as dictionary
    """
    student = session.query(Student).get(context["ra"])

    if student:
        for attr in context.keys():
            setattr(student, attr, context[attr])

        student.save()

        return student.asdict()


def remove_student(ra: int) -> dict:
    """Remove a Student row in DB

    Args:
        ra (int): Student ra

    Returns:
        dict: Deleted message
    """
    student = session.query(Student).get(ra)

    if student:
        session.delete(student)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
