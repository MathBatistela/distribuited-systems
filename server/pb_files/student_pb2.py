# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: student.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='student.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstudent.proto\"H\n\x07Student\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06period\x18\x03 \x01(\x05\x12\x13\n\x0b\x63ourse_code\x18\x04 \x01(\x05\".\n\x10StudentsResponse\x12\x1a\n\x08students\x18\x01 \x03(\x0b\x32\x08.Student\"m\n\x12UpdateGradeRequest\x12\x14\n\x0csubject_code\x18\x01 \x01(\t\x12\x12\n\nstudent_ra\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\x10\n\x08semester\x18\x04 \x01(\x05\x12\r\n\x05grade\x18\x05 \x01(\x02\"t\n\x1cStudentQueryBySubjectRequest\x12\x14\n\x0csubject_code\x18\x01 \x01(\t\x12\x11\n\x04year\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08semester\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\x07\n\x05_yearB\x0b\n\t_semesterb\x06proto3'
)




_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ra', full_name='Student.ra', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Student.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='Student.period', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='course_code', full_name='Student.course_code', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=89,
)


_STUDENTSRESPONSE = _descriptor.Descriptor(
  name='StudentsResponse',
  full_name='StudentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='students', full_name='StudentsResponse.students', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=137,
)


_UPDATEGRADEREQUEST = _descriptor.Descriptor(
  name='UpdateGradeRequest',
  full_name='UpdateGradeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_code', full_name='UpdateGradeRequest.subject_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_ra', full_name='UpdateGradeRequest.student_ra', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='UpdateGradeRequest.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='UpdateGradeRequest.semester', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grade', full_name='UpdateGradeRequest.grade', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=248,
)


_STUDENTQUERYBYSUBJECTREQUEST = _descriptor.Descriptor(
  name='StudentQueryBySubjectRequest',
  full_name='StudentQueryBySubjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_code', full_name='StudentQueryBySubjectRequest.subject_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='StudentQueryBySubjectRequest.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='StudentQueryBySubjectRequest.semester', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_year', full_name='StudentQueryBySubjectRequest._year',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_semester', full_name='StudentQueryBySubjectRequest._semester',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=250,
  serialized_end=366,
)

_STUDENTSRESPONSE.fields_by_name['students'].message_type = _STUDENT
_STUDENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_year'].fields.append(
  _STUDENTQUERYBYSUBJECTREQUEST.fields_by_name['year'])
_STUDENTQUERYBYSUBJECTREQUEST.fields_by_name['year'].containing_oneof = _STUDENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_year']
_STUDENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_semester'].fields.append(
  _STUDENTQUERYBYSUBJECTREQUEST.fields_by_name['semester'])
_STUDENTQUERYBYSUBJECTREQUEST.fields_by_name['semester'].containing_oneof = _STUDENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_semester']
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['StudentsResponse'] = _STUDENTSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateGradeRequest'] = _UPDATEGRADEREQUEST
DESCRIPTOR.message_types_by_name['StudentQueryBySubjectRequest'] = _STUDENTQUERYBYSUBJECTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:Student)
  })
_sym_db.RegisterMessage(Student)

StudentsResponse = _reflection.GeneratedProtocolMessageType('StudentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STUDENTSRESPONSE,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:StudentsResponse)
  })
_sym_db.RegisterMessage(StudentsResponse)

UpdateGradeRequest = _reflection.GeneratedProtocolMessageType('UpdateGradeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGRADEREQUEST,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:UpdateGradeRequest)
  })
_sym_db.RegisterMessage(UpdateGradeRequest)

StudentQueryBySubjectRequest = _reflection.GeneratedProtocolMessageType('StudentQueryBySubjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _STUDENTQUERYBYSUBJECTREQUEST,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:StudentQueryBySubjectRequest)
  })
_sym_db.RegisterMessage(StudentQueryBySubjectRequest)


# @@protoc_insertion_point(module_scope)
