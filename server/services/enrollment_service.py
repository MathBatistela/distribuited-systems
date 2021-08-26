"""
Has all the services to manipulate Enrollment data
in database

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

from database.db import Enrollment, session


def create_enrollment(context: dict) -> dict:
    """Creates an Enrollment row in DB

    Args:
        context (dict): Enrollment fields

    Returns:
        dict: Enrollment object as dictionary
    """
    enrollment = Enrollment()

    for attr in context.keys():
        setattr(enrollment, attr, context[attr])

    enrollment.save()
    return enrollment.asdict()


def get_enrollments(search: dict) -> list:
    """Get all the Enrollments from DB

    Args:
        search (dict): Filter param

    Returns:
        list: List of Enrollments as dictionary
    """
    query = session.query(Enrollment)
    for attr, value in search.items():
        query = query.filter(getattr(Enrollment, attr) == value)

    return list(map(lambda o: o.asdict(), query.all()))


def get_enrollment(
    subject_code: str, student_ra: int, year: int, semester: int
) -> dict:
    """Get an Enrollment row from DB

    Args:
        subject_code (str): Subject code of the enrollment
        student_ra (int): Enrolled student ra
        year (int): Year of the enrollment
        semester (int): Semester of the enrollment

    Returns:
        dict: Enrollment object as dictonary
    """

    enrollment = (
        session.query(Enrollment)
        .filter_by(
            subject_code=subject_code,
            student_ra=student_ra,
            year=year,
            semester=semester,
        )
        .first()
    )
    if enrollment:
        return enrollment.asdict()
    else:
        return {}


def update_enrollment(context: dict) -> dict:
    """Update an Enrollment row in DB

    Args:
        context (dict): Enrollment fields to update

    Returns:
        dict: Updated enrollment object as dictionary
    """
    enrollment = (
        session.query(Enrollment)
        .filter_by(
            subject_code=context["subject_code"],
            student_ra=context["student_ra"],
            year=context["year"],
            semester=context["semester"],
        )
        .first()
    )

    if enrollment:
        for attr in context.keys():
            setattr(enrollment, attr, context[attr])

        enrollment.save()

        return enrollment.asdict()


def remove_enrollment(
    subject_code: str, student_ra: int, year: int, semester: int
) -> dict:
    """Remove an Enrollment row from DB

    Args:
        subject_code (str): Subject code of the enrollment
        student_ra (int): Enrolled student ra
        year (int): Year of the enrollment
        semester (int): Semester of the enrollment

    Returns:
        dict: Enrollment object as dictonary
    """
    enrollment = (
        session.query(Enrollment)
        .filter_by(
            subject_code=subject_code,
            student_ra=student_ra,
            year=year,
            semester=semester,
        )
        .first()
    )

    if enrollment:
        session.delete(enrollment)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
