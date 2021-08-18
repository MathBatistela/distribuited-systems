import sys
from database.db import Subject, session

sys.path.append("..")


def create_subject(context: dict) -> dict:
    subject = Subject()

    for attr in context.keys():
        setattr(subject, attr, context[attr])

    subject.save()
    return subject.asdict()


def get_subjects() -> list:
    return list(map(lambda o: o.asdict(), session.query(Subject).all()))


def get_subject(code: str) -> dict:
    return (session.query(Subject).get(code)).asdict()


def update_subject(context: dict) -> dict:
    subject = session.query(Subject).get(context["code"])

    if subject:
        for attr in context.keys():
            setattr(subject, attr, context[attr])

        subject.save()

        return subject.asdict()


def remove_subject(code: str) -> dict:
    subject = session.query(Subject).get(code)

    if subject:
        session.delete(subject)
        session.commit()

        return {"status": 200, "message": "Deleted successfully!"}
