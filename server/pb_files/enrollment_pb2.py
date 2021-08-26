# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enrollment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enrollment.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x65nrollment.proto\"x\n\nEnrollment\x12\x14\n\x0csubject_code\x18\x01 \x01(\t\x12\x12\n\nstudent_ra\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\x10\n\x08semester\x18\x04 \x01(\x05\x12\r\n\x05grade\x18\x05 \x01(\x02\x12\x11\n\tabscenses\x18\x06 \x01(\x05\"7\n\x13\x45nrollmentsResponse\x12 \n\x0b\x65nrollments\x18\x01 \x03(\x0b\x32\x0b.Enrollment\"_\n\x13\x45nrollmentPkRequest\x12\x14\n\x0csubject_code\x18\x01 \x01(\t\x12\x12\n\nstudent_ra\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\x10\n\x08semester\x18\x04 \x01(\x05\"w\n\x1f\x45nrollmentQueryBySubjectRequest\x12\x14\n\x0csubject_code\x18\x01 \x01(\t\x12\x11\n\x04year\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08semester\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\x07\n\x05_yearB\x0b\n\t_semester\"\xa7\x01\n\x17UpdateEnrollmentRequest\x12\x14\n\x0csubject_code\x18\x01 \x01(\t\x12\x12\n\nstudent_ra\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\x10\n\x08semester\x18\x04 \x01(\x05\x12\x12\n\x05grade\x18\x05 \x01(\x02H\x00\x88\x01\x01\x12\x16\n\tabscenses\x18\x06 \x01(\x05H\x01\x88\x01\x01\x42\x08\n\x06_gradeB\x0c\n\n_abscensesb\x06proto3'
)




_ENROLLMENT = _descriptor.Descriptor(
  name='Enrollment',
  full_name='Enrollment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_code', full_name='Enrollment.subject_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_ra', full_name='Enrollment.student_ra', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='Enrollment.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='Enrollment.semester', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grade', full_name='Enrollment.grade', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abscenses', full_name='Enrollment.abscenses', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=20,
  serialized_end=140,
)


_ENROLLMENTSRESPONSE = _descriptor.Descriptor(
  name='EnrollmentsResponse',
  full_name='EnrollmentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enrollments', full_name='EnrollmentsResponse.enrollments', index=0,
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
  serialized_start=142,
  serialized_end=197,
)


_ENROLLMENTPKREQUEST = _descriptor.Descriptor(
  name='EnrollmentPkRequest',
  full_name='EnrollmentPkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_code', full_name='EnrollmentPkRequest.subject_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_ra', full_name='EnrollmentPkRequest.student_ra', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='EnrollmentPkRequest.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='EnrollmentPkRequest.semester', index=3,
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
  serialized_start=199,
  serialized_end=294,
)


_ENROLLMENTQUERYBYSUBJECTREQUEST = _descriptor.Descriptor(
  name='EnrollmentQueryBySubjectRequest',
  full_name='EnrollmentQueryBySubjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_code', full_name='EnrollmentQueryBySubjectRequest.subject_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='EnrollmentQueryBySubjectRequest.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='EnrollmentQueryBySubjectRequest.semester', index=2,
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
      name='_year', full_name='EnrollmentQueryBySubjectRequest._year',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_semester', full_name='EnrollmentQueryBySubjectRequest._semester',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=296,
  serialized_end=415,
)


_UPDATEENROLLMENTREQUEST = _descriptor.Descriptor(
  name='UpdateEnrollmentRequest',
  full_name='UpdateEnrollmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_code', full_name='UpdateEnrollmentRequest.subject_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_ra', full_name='UpdateEnrollmentRequest.student_ra', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='UpdateEnrollmentRequest.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='UpdateEnrollmentRequest.semester', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grade', full_name='UpdateEnrollmentRequest.grade', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abscenses', full_name='UpdateEnrollmentRequest.abscenses', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
      name='_grade', full_name='UpdateEnrollmentRequest._grade',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_abscenses', full_name='UpdateEnrollmentRequest._abscenses',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=418,
  serialized_end=585,
)

_ENROLLMENTSRESPONSE.fields_by_name['enrollments'].message_type = _ENROLLMENT
_ENROLLMENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_year'].fields.append(
  _ENROLLMENTQUERYBYSUBJECTREQUEST.fields_by_name['year'])
_ENROLLMENTQUERYBYSUBJECTREQUEST.fields_by_name['year'].containing_oneof = _ENROLLMENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_year']
_ENROLLMENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_semester'].fields.append(
  _ENROLLMENTQUERYBYSUBJECTREQUEST.fields_by_name['semester'])
_ENROLLMENTQUERYBYSUBJECTREQUEST.fields_by_name['semester'].containing_oneof = _ENROLLMENTQUERYBYSUBJECTREQUEST.oneofs_by_name['_semester']
_UPDATEENROLLMENTREQUEST.oneofs_by_name['_grade'].fields.append(
  _UPDATEENROLLMENTREQUEST.fields_by_name['grade'])
_UPDATEENROLLMENTREQUEST.fields_by_name['grade'].containing_oneof = _UPDATEENROLLMENTREQUEST.oneofs_by_name['_grade']
_UPDATEENROLLMENTREQUEST.oneofs_by_name['_abscenses'].fields.append(
  _UPDATEENROLLMENTREQUEST.fields_by_name['abscenses'])
_UPDATEENROLLMENTREQUEST.fields_by_name['abscenses'].containing_oneof = _UPDATEENROLLMENTREQUEST.oneofs_by_name['_abscenses']
DESCRIPTOR.message_types_by_name['Enrollment'] = _ENROLLMENT
DESCRIPTOR.message_types_by_name['EnrollmentsResponse'] = _ENROLLMENTSRESPONSE
DESCRIPTOR.message_types_by_name['EnrollmentPkRequest'] = _ENROLLMENTPKREQUEST
DESCRIPTOR.message_types_by_name['EnrollmentQueryBySubjectRequest'] = _ENROLLMENTQUERYBYSUBJECTREQUEST
DESCRIPTOR.message_types_by_name['UpdateEnrollmentRequest'] = _UPDATEENROLLMENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Enrollment = _reflection.GeneratedProtocolMessageType('Enrollment', (_message.Message,), {
  'DESCRIPTOR' : _ENROLLMENT,
  '__module__' : 'enrollment_pb2'
  # @@protoc_insertion_point(class_scope:Enrollment)
  })
_sym_db.RegisterMessage(Enrollment)

EnrollmentsResponse = _reflection.GeneratedProtocolMessageType('EnrollmentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENROLLMENTSRESPONSE,
  '__module__' : 'enrollment_pb2'
  # @@protoc_insertion_point(class_scope:EnrollmentsResponse)
  })
_sym_db.RegisterMessage(EnrollmentsResponse)

EnrollmentPkRequest = _reflection.GeneratedProtocolMessageType('EnrollmentPkRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENROLLMENTPKREQUEST,
  '__module__' : 'enrollment_pb2'
  # @@protoc_insertion_point(class_scope:EnrollmentPkRequest)
  })
_sym_db.RegisterMessage(EnrollmentPkRequest)

EnrollmentQueryBySubjectRequest = _reflection.GeneratedProtocolMessageType('EnrollmentQueryBySubjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENROLLMENTQUERYBYSUBJECTREQUEST,
  '__module__' : 'enrollment_pb2'
  # @@protoc_insertion_point(class_scope:EnrollmentQueryBySubjectRequest)
  })
_sym_db.RegisterMessage(EnrollmentQueryBySubjectRequest)

UpdateEnrollmentRequest = _reflection.GeneratedProtocolMessageType('UpdateEnrollmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENROLLMENTREQUEST,
  '__module__' : 'enrollment_pb2'
  # @@protoc_insertion_point(class_scope:UpdateEnrollmentRequest)
  })
_sym_db.RegisterMessage(UpdateEnrollmentRequest)


# @@protoc_insertion_point(module_scope)
