import sys
from database.db import Enrollment, session

sys.path.append("..")


def create_enrollment(context: dict) -> dict:
    enrollment = Enrollment()

    for attr in context.keys():
        setattr(enrollment, attr, context[attr])

    enrollment.save()
    return enrollment.asdict()


def get_enrollments(search: dict) -> list:
    query = session.query(Enrollment)
    for attr,value in search.items():
        query = query.filter( getattr(Enrollment,attr)==value )

    return list(map(lambda o: o.asdict(), query.all()))


def get_enrollment(subject_code: str, student_ra: int) -> dict:
    return (session.query(Enrollment).filter_by(subject_code=subject_code, student_ra=student_ra).one()).asdict()


def update_enrollment(context: dict) -> dict:
    enrollment = session.query(Enrollment).filter_by(subject_code=context["subject_code"], student_ra=context["student_ra"]).one()

    if enrollment:
        for attr in context.keys():
            setattr(enrollment, attr, context[attr])

        enrollment.save()

        return enrollment.asdict()


def remove_enrollment(subject_code: str, student_ra: int) -> dict:
    enrollment = session.query(Enrollment).filter_by(subject_code=subject_code, student_ra=student_ra).one()

    if enrollment:
        session.delete(enrollment)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
