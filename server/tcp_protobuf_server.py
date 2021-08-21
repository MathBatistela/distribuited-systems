"""
TCP/IP server that communicates by protocol buffers to handle
a grades manager service

Authors:
    @MathBatistela
    @MarcosGolom

Created at: 20/08/2021
Updated at: 20/08/2021
"""

import socket
import sys
import _thread
import logging
from pb_files import server_pb2, student_pb2
from google.protobuf import json_format, message
from services import enrollment_service, student_service
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)

METHODS = {0: "update_grade", 1: "get_students_by_enrollment"}

RESPONSES = {"server_response": 0, "students_response": 1}

HEADER = {"JOB": 2, "PB_SIZE": 4}


def get_students_by_enrollment(request):
    request_msg = student_pb2.StudentQueryByEnrollmentRequest()
    request_msg.ParseFromString(request)
    request_dict = json_format.MessageToDict(
        request_msg, preserving_proto_field_name=True
    )
    logging.info(f"Getting students for subject: {request_msg.subject_code}")
    try:
        students = student_service.get_students_by_enrollment(request_dict)
    except SQLAlchemyError as e:
        logging.error(f"Error in updating grade: {e}")
        err_response = server_pb2.Response(status=200, message=str(e))
        return RESPONSES["server_response"], err_response

    student_msg_list = list(
        map(
            lambda student: student_pb2.Student(
                ra=student["ra"],
                name=student["name"],
                period=student["period"],
                course_code=student["course_code"],
            ),
            students,
        )
    )
    response = student_pb2.StudentsResponse(students=student_msg_list)

    return RESPONSES["students_response"], response


def update_grade(request):
    request_msg = student_pb2.UpdateGradeRequest()
    request_msg.ParseFromString(request)
    request_dict = json_format.MessageToDict(
        request_msg, preserving_proto_field_name=True
    )
    logging.info(f"Updating grade for student: {request_msg.student_ra}")
    try:
        enrollment_service.update_enrollment(request_dict)
    except SQLAlchemyError as e:
        logging.error(f"Error in updating grade: {e}")
        err_response = server_pb2.Response(status=200, message=str(e))
        return RESPONSES["server_response"], err_response

    response = server_pb2.Response(status=200, message="Grade updated successfully!")

    return RESPONSES["server_response"], response


def generate_header(response_type, response_data):
    response_type = response_type.to_bytes(2, byteorder="little", signed=False)
    response_size = (response_data.ByteSize()).to_bytes(
        4, byteorder="little", signed=False
    )
    header = response_type + response_size
    return header

def raise_error(socket, message, status):
    logging.error(message)
    err_response = server_pb2.Response(status=status, message=message)
    header = generate_header(RESPONSES["server_response"], err_response)
    socket.send(header), socket.send(
        err_response.SerializeToString()
    )


def handle_client(clientsocket, addr):

    logging.info(f"Connection established with {addr}")

    header = clientsocket.recv(sum(HEADER.values()))
    method = int.from_bytes(
        header[: HEADER["JOB"]], byteorder="little", signed=False
    )
    pb_size = int.from_bytes(
        header[-HEADER["PB_SIZE"] :], byteorder="little", signed=False
    )
    pb_message = clientsocket.recv(pb_size)

    if method in METHODS.keys():
        try:
            response_type, response_data = eval(METHODS[method])(pb_message)
            header = generate_header(response_type, response_data)
            clientsocket.send(header), clientsocket.send(
                response_data.SerializeToString()
            )
        except:
            raise_error(clientsocket, "Internal server error", 500)

    else:
      raise_error(clientsocket, f"Method with code {method} does not exist", 404)

    clientsocket.close()
    sys.exit()


if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 2020)
    logging.info(f"Starting up on {server_address[0]} port {server_address[1]}")
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    logging.info("Waiting for a connection")

    sock.listen(5)

    while True:
        try:
            connection, client_address = sock.accept()
            _thread.start_new_thread(handle_client, (connection, client_address))
        except (KeyboardInterrupt,Exception):
            logging.info("Server closed")
            sock.close()
            sys.exit()
