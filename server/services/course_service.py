import sys
from database.db import Course, session

sys.path.append("..")


def create_course(context: dict) -> dict:
    course = Course()

    for attr in context.keys():
        setattr(course, attr, context[attr])

    course.save()
    return course.asdict()


def get_courses() -> list:
    return list(map(lambda o: o.asdict(), session.query(Course).all()))


def get_course(code: int) -> dict:
    return (session.query(Course).get(code)).asdict()


def update_course(context: dict) -> dict:
    course = session.query(Course).get(context["code"])

    if course:
        for attr in context.keys():
            setattr(course, attr, context[attr])

        course.save()

        return course.asdict()


def remove_course(code: int) -> dict:
    course = session.query(Course).get(code)

    if course:
        session.delete(course)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
