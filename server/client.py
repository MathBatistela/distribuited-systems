import socket
from pb_files import server_pb2, student_pb2
from google.protobuf import json_format

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 2020))

# student = student_pb2.Student()
# student.ra = 237892
# student.name = "Marcos Golom"
# print(student.ByteSize())
# student.period = 45
# student.course_code = 30

# x = student_pb2.UpdateGradeRequest(
#     subject_code="BCC32B",
#     student_ra=2046423,
#     year=2021,
#     semester=2,
#     grade=3
# )

# # marshalling
# msg = x.SerializeToString()
# size = len(msg)
# print(size)
# print(msg)

# func = (4).to_bytes(2, byteorder='little', signed=False)
# size = size.to_bytes(4, byteorder='little', signed=False)


y = student_pb2.StudentQueryByEnrollmentRequest(subject_code="BCC37D", semester=2)

# marshalling
msg = y.SerializeToString()
size = len(msg)
print(size)
print(msg)

func = (1).to_bytes(2, byteorder="little", signed=False)
size = size.to_bytes(4, byteorder="little", signed=False)


client_socket.send(func + size)

client_socket.send(msg)

header = client_socket.recv(6)

res = int.from_bytes(header[:2], byteorder="little", signed=False)
pb_size = int.from_bytes(header[-4:], byteorder="little", signed=False)

print(res)
pb = client_socket.recv(pb_size)

response = student_pb2.StudentsResponse()
response.ParseFromString(pb)

print(response.students)


client_socket.close()

# print(json_format.MessageToDict(student, preserving_proto_field_name=True))
