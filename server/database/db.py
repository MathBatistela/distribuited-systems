"""
Object-relational mapping for all tables in grades_manager DB 

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

import sys

sys.path.append("..")

from sqlalchemy import Column, String, Integer, ForeignKey, Float, inspect
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.sqltypes import Float

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

# opens DB and creates a session
engine = create_engine("sqlite:///database/grades_manager.db")
Session = sessionmaker(bind=engine)
session = Session()


# base class with base methods 
@as_declarative()
class Base:
    def asdict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self):
        session.add(self)
        session.commit()


# Course table ORM
class Course(Base):
    __tablename__ = "course"
    code = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship("Subject")
    students = relationship("Student")


# Enrollment table ORM
class Enrollment(Base):
    __tablename__ = "enrollment"
    year = Column(Integer)
    semester = Column(Integer)
    subject_code = Column(String, ForeignKey("subject.code"), primary_key=True)
    student_ra = Column(Integer, ForeignKey("student.ra"), primary_key=True)
    grade = Column(Float)
    abscenses = Column(Integer)
    student = relationship("Student")
    subject = relationship("Subject")


# Subject table ORM
class Subject(Base):
    __tablename__ = "subject"
    code = Column(String, primary_key=True)
    name = Column(String)
    professor = Column(String)
    course_code = Column(Integer, ForeignKey("course.code"))
    enrolled_students = relationship("Enrollment", back_populates="subject")


# Student table ORM
class Student(Base):
    __tablename__ = "student"
    ra = Column(Integer, primary_key=True)
    name = Column(String)
    period = Column(Integer)
    course_code = Column(Integer, ForeignKey("course.code"))
    subjects = relationship("Enrollment", back_populates="student")


Base.metadata.create_all(engine)
