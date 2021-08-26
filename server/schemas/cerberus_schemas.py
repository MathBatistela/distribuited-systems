"""
Schemas used by Cerberus module to validate requested data dictionaries

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

# schemas for students

student_create_schema = {
    "ra": {"type": "integer", "required": True},
    "name": {"type": "string", "required": True},
    "period": {"type": "integer", "required": True},
    "course_code": {"type": "integer", "required": True},
}

student_pk_schema = {"ra": {"type": "integer", "required": True}}

student_update_schema = {
    "ra": {"type": "integer", "required": True},
    "name": {"type": "string"},
    "period": {"type": "integer"},
    "course_code": {"type": "integer"},
}

# schemas for courses

course_create_schema = {
    "code": {"type": "integer", "required": True},
    "name": {"type": "string", "required": True},
}

course_pk_schema = {"code": {"type": "integer", "required": True}}

course_update_schema = {
    "code": {"type": "integer", "required": True},
    "name": {"type": "string"},
}

# schemas for subjects

subject_create_schema = {
    "code": {"type": "string", "required": True},
    "name": {"type": "string", "required": True},
    "professor": {"type": "string", "required": True},
    "course_code": {"type": "integer", "required": True},
}

subject_pk_schema = {"code": {"type": "string", "required": True}}

subject_update_schema = {
    "code": {"type": "string", "required": True},
    "name": {"type": "string"},
    "professor": {"type": "string"},
    "course_code": {"type": "integer"},
}

# schemas for enrollments

enrollment_create_schema = {
    "subject_code": {"type": "string", "required": True},
    "student_ra": {"type": "integer", "required": True},
    "year": {"type": "integer", "required": True},
    "semester": {"type": "integer", "required": True},
    "grade": {"type": "float", "required": True},
    "abscenses": {"type": "integer", "required": True},
}

enrollment_pk_schema = {
    "subject_code": {"type": "string", "required": True},
    "student_ra": {"type": "integer", "required": True},
    "year": {"type": "integer", "required": True},
    "semester": {"type": "integer", "required": True},
}

enrollment_update_schema = {
    "subject_code": {"type": "string", "required": True},
    "student_ra": {"type": "integer", "required": True},
    "year": {"type": "integer", "required": True},
    "semester": {"type": "integer", "required": True},
    "abscenses": {"type": "integer"},
    "grade": {"type": "float"},
}

# schemas for queries

enrolled_students_query_schema = {
    "subject_code": {"type": "string", "required": True},
    "year": {"type": "integer"},
    "semester": {"type": "integer"},
}
