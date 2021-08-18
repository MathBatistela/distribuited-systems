import json
import schemas
from flask import Flask, request, jsonify
from services import student_service, course_service, subject_service
from cerberus import Validator
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["DEBUG"] = True
v = Validator()


class APIError(Exception):
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


@app.errorhandler(APIError)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code


@app.route("/student", methods=["GET", "POST", "PUT", "DELETE"])
def student():
    try:
        request_data = json.loads(request.data)
    except:
        raise APIError("Bad JSON!", status_code=400)

    try:
        if request.method == "GET":
            if v.validate(request_data, schemas.student_pk_schema):
                response = student_service.get_student(request_data["ra"])

        elif request.method == "POST":
            if v.validate(request_data, schemas.student_create_schema):
                response = student_service.create_student(request_data)

        elif request.method == "PUT":
            if v.validate(request_data, schemas.student_update_schema):
                response = student_service.update_student(request_data)

        elif request.method == "DELETE":
            if v.validate(request_data, schemas.student_pk_schema):
                response = student_service.remove_student(request_data["ra"])

    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise APIError(error, status_code=500)

    validate_errors = v.errors
    if validate_errors:
        raise APIError(json.dumps(validate_errors), status_code=400)

    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


@app.route("/course", methods=["GET", "POST", "PUT", "DELETE"])
def course():

    try:
        request_data = json.loads(request.data)
    except:
        return jsonify({"status": 400, "message": "Bad request"}), 400
    try:
        if request.method == "GET":
            if v.validate(request_data, schemas.course_pk_schema):
                response = course_service.get_course(request_data["code"])

        elif request.method == "POST":
            if v.validate(request_data, schemas.course_create_schema):
                response = course_service.create_course(request_data)

        elif request.method == "PUT":
            if v.validate(request_data, schemas.course_update_schema):
                response = course_service.update_course(request_data)

        elif request.method == "DELETE":
            if v.validate(request_data, schemas.course_pk_schema):
                response = course_service.remove_course(request_data["code"])

    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise APIError(error, status_code=400)

    validate_errors = v.errors
    if validate_errors:
        raise APIError(json.dumps(validate_errors), status_code=400)

    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


@app.route("/subject", methods=["GET", "POST", "PUT", "DELETE"])
def subject():
    try:
        request_data = json.loads(request.data)
    except:
        return jsonify({"status": 400, "message": "Bad request"}), 400
    try:
        if request.method == "GET":
            if v.validate(request_data, schemas.subject_pk_schema):
                response = subject_service.get_subject(request_data["code"])

        elif request.method == "POST":
            if v.validate(request_data, schemas.subject_create_schema):
                response = subject_service.create_subject(request_data)

        elif request.method == "PUT":
            if v.validate(request_data, schemas.subject_update_schema):
                response = subject_service.update_subject(request_data)

        elif request.method == "DELETE":
            if v.validate(request_data, schemas.subject_pk_schema):
                response = subject_service.remove_subject(request_data["code"])

    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise APIError(error, status_code=400)

    validate_errors = v.errors
    if validate_errors:
        raise APIError(json.dumps(validate_errors), status_code=400)

    if response:
        return jsonify(response), 200
    else:
        raise APIError("Not Found", status_code=404)


app.run()
