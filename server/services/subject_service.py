"""
Has all the services to manipulate Subject data
in database

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

import sys
from database.db import Subject, session

sys.path.append("..")


def create_subject(context: dict) -> dict:
    """Creates a Subject row in DB

    Args:
        context (dict): Subjet fileds

    Returns:
        dict: Subject object as dictionary
    """
    subject = Subject()

    for attr in context.keys():
        setattr(subject, attr, context[attr])

    subject.save()
    return subject.asdict()


def get_subjects() -> list:
    """Get all the Subjects rows in DB

    Returns:
        list: List of Subjects as dictionary
    """
    return list(map(lambda o: o.asdict(), session.query(Subject).all()))


def get_subject(code: str) -> dict:
    """Get a Subject row in DB

    Args:
        code (str): Subject code

    Returns:
        dict: Subject object as dictionary
    """
    return (session.query(Subject).get(code)).asdict()


def update_subject(context: dict) -> dict:
    """Update a Subject row in DB

    Args:
        context (dict): Subject fields to update

    Returns:
        dict: Subject objects as dictionary
    """
    subject = session.query(Subject).get(context["code"])

    if subject:
        for attr in context.keys():
            setattr(subject, attr, context[attr])

        subject.save()

        return subject.asdict()


def remove_subject(code: str) -> dict:
    """Remove a Subject row in DB

    Args:
        code (str): Subject code

    Returns:
        dict: Subject object as dictionary
    """
    subject = session.query(Subject).get(code)

    if subject:
        session.delete(subject)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
