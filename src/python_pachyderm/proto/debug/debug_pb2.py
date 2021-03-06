# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/debug/debug.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from python_pachyderm.proto.pps import pps_pb2 as client_dot_pps_dot_pps__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/debug/debug.proto',
  package='debug',
  syntax='proto3',
  serialized_options=b'Z/github.com/pachyderm/pachyderm/src/client/debug',
  serialized_pb=b'\n\x18\x63lient/debug/debug.proto\x12\x05\x64\x65\x62ug\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x14\x63lient/pps/pps.proto\"P\n\x0eProfileRequest\x12\x1f\n\x07profile\x18\x01 \x01(\x0b\x32\x0e.debug.Profile\x12\x1d\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\r.debug.Filter\"D\n\x07Profile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"g\n\x06\x46ilter\x12\x0f\n\x05pachd\x18\x01 \x01(\x08H\x00\x12!\n\x08pipeline\x18\x02 \x01(\x0b\x32\r.pps.PipelineH\x00\x12\x1f\n\x06worker\x18\x03 \x01(\x0b\x32\r.debug.WorkerH\x00\x42\x08\n\x06\x66ilter\")\n\x06Worker\x12\x0b\n\x03pod\x18\x01 \x01(\t\x12\x12\n\nredirected\x18\x02 \x01(\x08\".\n\rBinaryRequest\x12\x1d\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\r.debug.Filter\",\n\x0b\x44umpRequest\x12\x1d\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\r.debug.Filter2\xc8\x01\n\x05\x44\x65\x62ug\x12\x41\n\x07Profile\x12\x15.debug.ProfileRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x30\x01\x12?\n\x06\x42inary\x12\x14.debug.BinaryRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x30\x01\x12;\n\x04\x44ump\x12\x12.debug.DumpRequest\x1a\x1b.google.protobuf.BytesValue\"\x00\x30\x01\x42\x31Z/github.com/pachyderm/pachyderm/src/client/debugb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,client_dot_pps_dot_pps__pb2.DESCRIPTOR,])




_PROFILEREQUEST = _descriptor.Descriptor(
  name='ProfileRequest',
  full_name='debug.ProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile', full_name='debug.ProfileRequest.profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='debug.ProfileRequest.filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=121,
  serialized_end=201,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='debug.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='debug.Profile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='debug.Profile.duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=203,
  serialized_end=271,
)


_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='debug.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pachd', full_name='debug.Filter.pachd', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='debug.Filter.pipeline', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker', full_name='debug.Filter.worker', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='filter', full_name='debug.Filter.filter',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=273,
  serialized_end=376,
)


_WORKER = _descriptor.Descriptor(
  name='Worker',
  full_name='debug.Worker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pod', full_name='debug.Worker.pod', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redirected', full_name='debug.Worker.redirected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=378,
  serialized_end=419,
)


_BINARYREQUEST = _descriptor.Descriptor(
  name='BinaryRequest',
  full_name='debug.BinaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='debug.BinaryRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=421,
  serialized_end=467,
)


_DUMPREQUEST = _descriptor.Descriptor(
  name='DumpRequest',
  full_name='debug.DumpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='debug.DumpRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=469,
  serialized_end=513,
)

_PROFILEREQUEST.fields_by_name['profile'].message_type = _PROFILE
_PROFILEREQUEST.fields_by_name['filter'].message_type = _FILTER
_PROFILE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_FILTER.fields_by_name['pipeline'].message_type = client_dot_pps_dot_pps__pb2._PIPELINE
_FILTER.fields_by_name['worker'].message_type = _WORKER
_FILTER.oneofs_by_name['filter'].fields.append(
  _FILTER.fields_by_name['pachd'])
_FILTER.fields_by_name['pachd'].containing_oneof = _FILTER.oneofs_by_name['filter']
_FILTER.oneofs_by_name['filter'].fields.append(
  _FILTER.fields_by_name['pipeline'])
_FILTER.fields_by_name['pipeline'].containing_oneof = _FILTER.oneofs_by_name['filter']
_FILTER.oneofs_by_name['filter'].fields.append(
  _FILTER.fields_by_name['worker'])
_FILTER.fields_by_name['worker'].containing_oneof = _FILTER.oneofs_by_name['filter']
_BINARYREQUEST.fields_by_name['filter'].message_type = _FILTER
_DUMPREQUEST.fields_by_name['filter'].message_type = _FILTER
DESCRIPTOR.message_types_by_name['ProfileRequest'] = _PROFILEREQUEST
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['Worker'] = _WORKER
DESCRIPTOR.message_types_by_name['BinaryRequest'] = _BINARYREQUEST
DESCRIPTOR.message_types_by_name['DumpRequest'] = _DUMPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfileRequest = _reflection.GeneratedProtocolMessageType('ProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEREQUEST,
  '__module__' : 'client.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.ProfileRequest)
  })
_sym_db.RegisterMessage(ProfileRequest)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'client.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.Profile)
  })
_sym_db.RegisterMessage(Profile)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'client.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.Filter)
  })
_sym_db.RegisterMessage(Filter)

Worker = _reflection.GeneratedProtocolMessageType('Worker', (_message.Message,), {
  'DESCRIPTOR' : _WORKER,
  '__module__' : 'client.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.Worker)
  })
_sym_db.RegisterMessage(Worker)

BinaryRequest = _reflection.GeneratedProtocolMessageType('BinaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINARYREQUEST,
  '__module__' : 'client.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.BinaryRequest)
  })
_sym_db.RegisterMessage(BinaryRequest)

DumpRequest = _reflection.GeneratedProtocolMessageType('DumpRequest', (_message.Message,), {
  'DESCRIPTOR' : _DUMPREQUEST,
  '__module__' : 'client.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.DumpRequest)
  })
_sym_db.RegisterMessage(DumpRequest)


DESCRIPTOR._options = None

_DEBUG = _descriptor.ServiceDescriptor(
  name='Debug',
  full_name='debug.Debug',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=516,
  serialized_end=716,
  methods=[
  _descriptor.MethodDescriptor(
    name='Profile',
    full_name='debug.Debug.Profile',
    index=0,
    containing_service=None,
    input_type=_PROFILEREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Binary',
    full_name='debug.Debug.Binary',
    index=1,
    containing_service=None,
    input_type=_BINARYREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Dump',
    full_name='debug.Debug.Dump',
    index=2,
    containing_service=None,
    input_type=_DUMPREQUEST,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEBUG)

DESCRIPTOR.services_by_name['Debug'] = _DEBUG

# @@protoc_insertion_point(module_scope)
