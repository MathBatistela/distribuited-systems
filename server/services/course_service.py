"""
Has all the services to manipulate Course data
in database

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

from database.db import Course, session

def create_course(context: dict) -> dict:
    """Creates a Course row in DB

    Args:
        context (dict): Course fields

    Returns:
        dict: Course object as dictionary
    """
    course = Course()

    for attr in context.keys():
        setattr(course, attr, context[attr])

    course.save()
    return course.asdict()


def get_courses() -> list:
    """Get all the Courses from DB

    Returns:
        list: List of Courses as dictionary
    """
    return list(map(lambda o: o.asdict(), session.query(Course).all()))


def get_course(code: int) -> dict:
    """Get a Course row by the code

    Args:
        code (int): Course code

    Returns:
        dict: Course as dictionary
    """
    return (session.query(Course).get(code)).asdict()


def update_course(context: dict) -> dict:
    """Update a Course row in DB

    Args:
        context (dict): Course fields to update

    Returns:
        dict: Updated course as dictionary
    """
    course = session.query(Course).get(context["code"])

    if course:
        for attr in context.keys():
            setattr(course, attr, context[attr])

        course.save()

        return course.asdict()


def remove_course(code: int) -> dict:
    """Remove a Course row by the code

    Args:
        code (int): Course code

    Returns:
        dict: Deleted message
    """
    course = session.query(Course).get(code)

    if course:
        session.delete(course)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
