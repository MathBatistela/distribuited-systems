"""
HTTP server that communicates by JSON to handle
a grades manager service

Authors:
    @MathBatistela
    @mvgolom

Created at: 14/08/2021
Updated at: 21/08/2021
"""

import json
import schemas.cerberus_schemas as schemas
from flask import Flask, request, jsonify
from services import (
    student_service,
    course_service,
    subject_service,
    enrollment_service,
)
from cerberus import Validator
from sqlalchemy.exc import SQLAlchemyError

# instantiates the HTTP server and schema validator
app = Flask(__name__)
app.config["DEBUG"] = True
v = Validator()


class APIError(Exception):
    """Auxiliar class for raising errors during the execution

    Args:
        Exception: An exception
    """

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        rv["status"] = self.status_code
        return rv


# defining above class as an error handler
@app.errorhandler(APIError)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code


# student crud route
@app.route("/student", methods=["GET", "POST", "PUT", "DELETE"])
def student():

    # loads the JSON request to a dict
    try:
        request_data = json.loads(request.data)
    except:
        raise APIError("Bad JSON!", status_code=400)

    # validates requested data and calls a student service according to the requested method
    try:
        if request.method == "GET" and v.validate(
            request_data, schemas.student_pk_schema
        ):
            response = student_service.get_student(request_data["ra"])

        elif request.method == "POST" and v.validate(
            request_data, schemas.student_create_schema
        ):
            response = student_service.create_student(request_data)

        elif request.method == "PUT" and v.validate(
            request_data, schemas.student_update_schema
        ):
            response = student_service.update_student(request_data)

        elif request.method == "DELETE" and v.validate(
            request_data, schemas.student_pk_schema
        ):
            response = student_service.remove_student(request_data["ra"])

    except SQLAlchemyError as e:
        raise APIError(str(e), status_code=400)

    # if requested data isn't valid, raises an error
    if v.errors:
        raise APIError(str(v.errors).strip("{}"), status_code=400)

    # returns a response, if exists
    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


# students search route
@app.route("/students/enrolled", methods=["GET"])
def students():

    # loads search params
    search = request.args.to_dict()
    for key in search:
        try:
            search[key] = int(search[key])
        except:
            pass

    # validates the requested data
    try:
        if v.validate(search, schemas.enrolled_students_query_schema):
            response = student_service.get_students_by_enrollment(search)
    except SQLAlchemyError as e:
        raise APIError(str(e), status_code=400)

    # if requested data isn't valid, raises an error
    if v.errors:
        raise APIError(str(v.errors).strip("{}"), status_code=400)

    return jsonify(response), 200


# course crud route
@app.route("/course", methods=["GET", "POST", "PUT", "DELETE"])
def course():

    # loads the JSON request to a dict
    try:
        request_data = json.loads(request.data)
    except:
        return jsonify({"status": 400, "message": "Bad request"}), 400

    # validates requested data and calls a course service according to the requested method
    try:
        if request.method == "GET" and v.validate(
            request_data, schemas.course_pk_schema
        ):
            response = course_service.get_course(request_data["code"])

        elif request.method == "POST" and v.validate(
            request_data, schemas.course_create_schema
        ):
            response = course_service.create_course(request_data)

        elif request.method == "PUT" and v.validate(
            request_data, schemas.course_update_schema
        ):
            response = course_service.update_course(request_data)

        elif request.method == "DELETE" and v.validate(
            request_data, schemas.course_pk_schema
        ):
            response = course_service.remove_course(request_data["code"])

    except SQLAlchemyError as e:
        raise APIError(str(e), status_code=400)

    # if requested data isn't valid, raises an error
    if v.errors:
        raise APIError(str(v.errors).strip("{}"), status_code=400)

    # returns a response, if exists
    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


# subject crud route
@app.route("/subject", methods=["GET", "POST", "PUT", "DELETE"])
def subject():

    # loads the JSON request to a dict
    try:
        request_data = json.loads(request.data)
    except:
        return jsonify({"status": 400, "message": "Bad request"}), 400

    # validates requested data and calls a subject service according to the requested method
    try:
        if request.method == "GET" and v.validate(
            request_data, schemas.subject_pk_schema
        ):
            response = subject_service.get_subject(request_data["code"])

        elif request.method == "POST" and v.validate(
            request_data, schemas.subject_create_schema
        ):
            response = subject_service.create_subject(request_data)

        elif request.method == "PUT" and v.validate(
            request_data, schemas.subject_update_schema
        ):
            response = subject_service.update_subject(request_data)

        elif request.method == "DELETE" and v.validate(
            request_data, schemas.subject_pk_schema
        ):
            response = subject_service.remove_subject(request_data["code"])

    except SQLAlchemyError as e:
        raise APIError(str(e), status_code=400)

    # if requested data isn't valid, raises an error
    if v.errors:
        raise APIError(str(v.errors).strip("{}"), status_code=400)

    # returns a response, if exists
    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


# enrollment crud route
@app.route("/enrollment", methods=["GET", "POST", "PUT", "DELETE"])
def enrollment():

    # loads the JSON request to a dict
    try:
        request_data = json.loads(request.data)
    except:
        return jsonify({"status": 400, "message": "Bad request"}), 400

    # validates requested data and calls an enrollment service according to the requested method
    try:
        if request.method == "GET" and v.validate(
            request_data, schemas.enrollment_pk_schema
        ):
            response = enrollment_service.get_enrollment(
                request_data["subject_code"],
                request_data["student_ra"],
                request_data["year"],
                request_data["semester"],
            )

        elif request.method == "POST" and v.validate(
            request_data, schemas.enrollment_create_schema
        ):
            response = enrollment_service.create_enrollment(request_data)

        elif request.method == "PUT" and v.validate(
            request_data, schemas.enrollment_update_schema
        ):
            response = enrollment_service.update_enrollment(request_data)

        elif request.method == "DELETE" and v.validate(
            request_data, schemas.enrollment_pk_schema
        ):
            response = enrollment_service.remove_enrollment(
                request_data["subject_code"],
                request_data["student_ra"],
                request_data["year"],
                request_data["semester"],
            )

    except SQLAlchemyError as e:
        raise APIError(str(e), status_code=400)

    # if requested data isn't valid, raises an error
    if v.errors:
        raise APIError(str(v.errors).strip("{}"), status_code=400)

    # returns a response, if exists
    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


# runs the server
app.run()
