"""
gRPC server that comunicates by protocol buffers to handle
a grades manager service

Authors:
    @MathBatistela
    @mvgolom

Created at: 22/08/2021
Updated at: 23/08/2021
"""

from concurrent import futures
import logging
from services import enrollment_service, student_service
from google.protobuf import json_format


import grpc
from pb_files import enrollment_pb2, student_pb2, server_pb2, server_pb2_grpc

IP = "127.0.0.1"
PORT = 50051

# logger config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)

# grades manager service for gRPC functions
class GradesManager(server_pb2_grpc.GradesManagerServicer):

    # remote procedure for creating an enrollment in DB
    def createEnrollment(self, request, context):
        logging.info(
            f"Creating enrollment for subject: {request.subject_code} and student: {request.student_ra}"
        )

        # mapping requested message to a dictionary
        request_dict = json_format.MessageToDict(
            request, preserving_proto_field_name=True
        )
        enrollment = enrollment_service.create_enrollment(request_dict)
        return enrollment_pb2.Enrollment(**enrollment)

    # remote procedure for getting an enrollment in DB
    def getEnrollment(self, request, context):
        logging.info(
            f"Getting enrollment for subject: {request.subject_code} and student: {request.student_ra}"
        )

        # mapping requested message to a dictionary
        request_dict = json_format.MessageToDict(
            request, preserving_proto_field_name=True
        )
        enrollment = enrollment_service.get_enrollment(**request_dict)
        return enrollment_pb2.Enrollment(**enrollment)

    # remote procedure for updating an enrollment in DB
    def updateEnrollment(self, request, context):
        logging.info(
            f"Updating enrollment for subject: {request.subject_code} and student: {request.student_ra}"
        )

        # mapping requested message to a dictionary
        request_dict = json_format.MessageToDict(
            request, preserving_proto_field_name=True
        )
        enrollment = enrollment_service.update_enrollment(request_dict)
        return enrollment_pb2.Enrollment(**enrollment)

    # remote procedure for deleting an enrollment in DB
    def deleteEnrollment(self, request, context):
        logging.info(
            f"Deleting enrollment for subject: {request.subject_code} and student: {request.student_ra}"
        )

        # mapping requested message to a dictionary
        request_dict = json_format.MessageToDict(
            request, preserving_proto_field_name=True
        )
        enrollment_service.remove_enrollment(**request_dict)
        return server_pb2.Response(
            status=200, message="Enrollment deleted successfully!"
        )

    # remote procedure for getting abscenses and grades for a subject in DB
    def getAbscensesAndGradesBySubject(self, request, context):
        logging.info(
            f"Getting abscenses and grades for subject: {request.subject_code}"
        )

        # mapping requested message to a dictionary
        request_dict = json_format.MessageToDict(
            request, preserving_proto_field_name=True
        )
        enrollments = enrollment_service.get_enrollments(request_dict)

        # sum all the abscenses
        abscenses = sum([enrollment["abscenses"] for enrollment in enrollments])

        # generate a grades list
        grades = [enrollment["grade"] for enrollment in enrollments]

        return server_pb2.AbscencesAndGradesBySubjectResponse(
            abscenses=abscenses, grades=grades
        )

    # remote procedure for getting students by subject from DB
    def getStudentsBySubject(self, request, context):
        logging.info(f"Getting students for subject: {request.subject_code}")

        # mapping requested message to a dictionary
        request_dict = json_format.MessageToDict(
            request, preserving_proto_field_name=True
        )
        students = student_service.get_students_by_enrollment(request_dict)

        # mapping obtained students from dict list to Student list
        student_msg_list = list(
            map(lambda student: student_pb2.Student(**student), students)
        )

        return student_pb2.StudentsResponse(students=student_msg_list)


if __name__ == "__main__":

    # instantiates the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_GradesManagerServicer_to_server(GradesManager(), server)
    server.add_insecure_port(f"{IP}:{PORT}")
    server.start()
    logging.info(f"Starting up on {IP} port {PORT}")
    server.wait_for_termination()
