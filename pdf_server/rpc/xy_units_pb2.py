# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xy-units.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xy-units.proto',
  package='units',
  syntax='proto3',
  serialized_options=b'\n\020io.grpc.xy.unitsB\021XyUnitServerProtoP\001',
  serialized_pb=b'\n\x0exy-units.proto\x12\x05units\"\x1f\n\x0cHelloRequest\x12\x0f\n\x07Message\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07Message\x18\x01 \x01(\t\"]\n\rGenPdfRequest\x12\x10\n\x08template\x18\x01 \x01(\t\x12\x12\n\nparameters\x18\x02 \x01(\t\x12\x14\n\x0cresourcePath\x18\x03 \x01(\t\x12\x10\n\x08saveName\x18\x04 \x01(\t\"\x1e\n\x0bGenPdfReply\x12\x0f\n\x07pdfPath\x18\x01 \x01(\t\"\x9c\x01\n\x12\x42rainReportRequest\x12\x12\n\nseriesPath\x18\x01 \x01(\t\x12\x11\n\tpatientId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06gender\x18\x04 \x01(\t\x12\x0b\n\x03\x61ge\x18\x05 \x01(\x05\x12\x10\n\x08scanInfo\x18\x06 \x01(\t\x12\x10\n\x08scanDate\x18\x07 \x01(\t\x12\x10\n\x08hospital\x18\x08 \x01(\t\"E\n\x10\x42rainReportReply\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x11\n\terrorCode\x18\x02 \x01(\x05\x12\x10\n\x08\x65rrorMsg\x18\x03 \x01(\t*-\n\nStatusCode\x12\x0b\n\x07Unknown\x10\x00\x12\x06\n\x02Ok\x10\x01\x12\n\n\x06\x46\x61iled\x10\x02\x32\xc6\x01\n\x10ReportsGenerator\x12\x46\n\x0eGenBrainReport\x12\x19.units.BrainReportRequest\x1a\x17.units.BrainReportReply\"\x00\x12\x34\n\x08SayHello\x12\x13.units.HelloRequest\x1a\x11.units.HelloReply\"\x00\x12\x34\n\x06GenPdf\x12\x14.units.GenPdfRequest\x1a\x12.units.GenPdfReply\"\x00\x42\'\n\x10io.grpc.xy.unitsB\x11XyUnitServerProtoP\x01\x62\x06proto3'
)

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='units.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ok', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=446,
  serialized_end=491,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
Unknown = 0
Ok = 1
Failed = 2



_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='units.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='units.HelloRequest.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=25,
  serialized_end=56,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='units.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='units.HelloReply.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=58,
  serialized_end=87,
)


_GENPDFREQUEST = _descriptor.Descriptor(
  name='GenPdfRequest',
  full_name='units.GenPdfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template', full_name='units.GenPdfRequest.template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='units.GenPdfRequest.parameters', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourcePath', full_name='units.GenPdfRequest.resourcePath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saveName', full_name='units.GenPdfRequest.saveName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=89,
  serialized_end=182,
)


_GENPDFREPLY = _descriptor.Descriptor(
  name='GenPdfReply',
  full_name='units.GenPdfReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pdfPath', full_name='units.GenPdfReply.pdfPath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=184,
  serialized_end=214,
)


_BRAINREPORTREQUEST = _descriptor.Descriptor(
  name='BrainReportRequest',
  full_name='units.BrainReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seriesPath', full_name='units.BrainReportRequest.seriesPath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientId', full_name='units.BrainReportRequest.patientId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='units.BrainReportRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='units.BrainReportRequest.gender', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='units.BrainReportRequest.age', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scanInfo', full_name='units.BrainReportRequest.scanInfo', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scanDate', full_name='units.BrainReportRequest.scanDate', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hospital', full_name='units.BrainReportRequest.hospital', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=217,
  serialized_end=373,
)


_BRAINREPORTREPLY = _descriptor.Descriptor(
  name='BrainReportReply',
  full_name='units.BrainReportReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='units.BrainReportReply.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='units.BrainReportReply.errorCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorMsg', full_name='units.BrainReportReply.errorMsg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=375,
  serialized_end=444,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['GenPdfRequest'] = _GENPDFREQUEST
DESCRIPTOR.message_types_by_name['GenPdfReply'] = _GENPDFREPLY
DESCRIPTOR.message_types_by_name['BrainReportRequest'] = _BRAINREPORTREQUEST
DESCRIPTOR.message_types_by_name['BrainReportReply'] = _BRAINREPORTREPLY
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'xy_units_pb2'
  # @@protoc_insertion_point(class_scope:units.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'xy_units_pb2'
  # @@protoc_insertion_point(class_scope:units.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

GenPdfRequest = _reflection.GeneratedProtocolMessageType('GenPdfRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENPDFREQUEST,
  '__module__' : 'xy_units_pb2'
  # @@protoc_insertion_point(class_scope:units.GenPdfRequest)
  })
_sym_db.RegisterMessage(GenPdfRequest)

GenPdfReply = _reflection.GeneratedProtocolMessageType('GenPdfReply', (_message.Message,), {
  'DESCRIPTOR' : _GENPDFREPLY,
  '__module__' : 'xy_units_pb2'
  # @@protoc_insertion_point(class_scope:units.GenPdfReply)
  })
_sym_db.RegisterMessage(GenPdfReply)

BrainReportRequest = _reflection.GeneratedProtocolMessageType('BrainReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _BRAINREPORTREQUEST,
  '__module__' : 'xy_units_pb2'
  # @@protoc_insertion_point(class_scope:units.BrainReportRequest)
  })
_sym_db.RegisterMessage(BrainReportRequest)

BrainReportReply = _reflection.GeneratedProtocolMessageType('BrainReportReply', (_message.Message,), {
  'DESCRIPTOR' : _BRAINREPORTREPLY,
  '__module__' : 'xy_units_pb2'
  # @@protoc_insertion_point(class_scope:units.BrainReportReply)
  })
_sym_db.RegisterMessage(BrainReportReply)


DESCRIPTOR._options = None

_REPORTSGENERATOR = _descriptor.ServiceDescriptor(
  name='ReportsGenerator',
  full_name='units.ReportsGenerator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=494,
  serialized_end=692,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenBrainReport',
    full_name='units.ReportsGenerator.GenBrainReport',
    index=0,
    containing_service=None,
    input_type=_BRAINREPORTREQUEST,
    output_type=_BRAINREPORTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='units.ReportsGenerator.SayHello',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenPdf',
    full_name='units.ReportsGenerator.GenPdf',
    index=2,
    containing_service=None,
    input_type=_GENPDFREQUEST,
    output_type=_GENPDFREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPORTSGENERATOR)

DESCRIPTOR.services_by_name['ReportsGenerator'] = _REPORTSGENERATOR

# @@protoc_insertion_point(module_scope)
