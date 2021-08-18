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
