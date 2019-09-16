# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/admin/v1_7/hashtree/hashtree.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from python_pachyderm.client.admin.v1_7.pfs import pfs_pb2 as client_dot_admin_dot_v1__7_dot_pfs_dot_pfs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/admin/v1_7/hashtree/hashtree.proto',
  package='hashtree_1_7',
  syntax='proto3',
  serialized_options=_b('Z=github.com/pachyderm/pachyderm/src/client/admin/v1_7/hashtree'),
  serialized_pb=_b('\n)client/admin/v1_7/hashtree/hashtree.proto\x12\x0chashtree_1_7\x1a\x1f\x63lient/admin/v1_7/pfs/pfs.proto\"1\n\rFileNodeProto\x12 \n\x07objects\x18\x04 \x03(\x0b\x32\x0f.pfs_1_7.Object\"h\n\x12\x44irectoryNodeProto\x12\x10\n\x08\x63hildren\x18\x03 \x03(\t\x12\x1f\n\x06header\x18\x04 \x01(\x0b\x32\x0f.pfs_1_7.Object\x12\x1f\n\x06\x66ooter\x18\x05 \x01(\x0b\x32\x0f.pfs_1_7.Object\"\xa1\x01\n\tNodeProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x14\n\x0csubtree_size\x18\x03 \x01(\x03\x12.\n\tfile_node\x18\x04 \x01(\x0b\x32\x1b.hashtree_1_7.FileNodeProto\x12\x32\n\x08\x64ir_node\x18\x05 \x01(\x0b\x32 .hashtree_1_7.DirectoryNodeProto\"\x95\x01\n\rHashTreeProto\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12/\n\x02\x66s\x18\x02 \x03(\x0b\x32#.hashtree_1_7.HashTreeProto.FsEntry\x1a\x42\n\x07\x46sEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.hashtree_1_7.NodeProto:\x02\x38\x01\x42?Z=github.com/pachyderm/pachyderm/src/client/admin/v1_7/hashtreeb\x06proto3')
  ,
  dependencies=[client_dot_admin_dot_v1__7_dot_pfs_dot_pfs__pb2.DESCRIPTOR,])




_FILENODEPROTO = _descriptor.Descriptor(
  name='FileNodeProto',
  full_name='hashtree_1_7.FileNodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objects', full_name='hashtree_1_7.FileNodeProto.objects', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=92,
  serialized_end=141,
)


_DIRECTORYNODEPROTO = _descriptor.Descriptor(
  name='DirectoryNodeProto',
  full_name='hashtree_1_7.DirectoryNodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='children', full_name='hashtree_1_7.DirectoryNodeProto.children', index=0,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='hashtree_1_7.DirectoryNodeProto.header', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='footer', full_name='hashtree_1_7.DirectoryNodeProto.footer', index=2,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=143,
  serialized_end=247,
)


_NODEPROTO = _descriptor.Descriptor(
  name='NodeProto',
  full_name='hashtree_1_7.NodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hashtree_1_7.NodeProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='hashtree_1_7.NodeProto.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtree_size', full_name='hashtree_1_7.NodeProto.subtree_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_node', full_name='hashtree_1_7.NodeProto.file_node', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dir_node', full_name='hashtree_1_7.NodeProto.dir_node', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=250,
  serialized_end=411,
)


_HASHTREEPROTO_FSENTRY = _descriptor.Descriptor(
  name='FsEntry',
  full_name='hashtree_1_7.HashTreeProto.FsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hashtree_1_7.HashTreeProto.FsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='hashtree_1_7.HashTreeProto.FsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=563,
)

_HASHTREEPROTO = _descriptor.Descriptor(
  name='HashTreeProto',
  full_name='hashtree_1_7.HashTreeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='hashtree_1_7.HashTreeProto.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fs', full_name='hashtree_1_7.HashTreeProto.fs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HASHTREEPROTO_FSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=563,
)

_FILENODEPROTO.fields_by_name['objects'].message_type = client_dot_admin_dot_v1__7_dot_pfs_dot_pfs__pb2._OBJECT
_DIRECTORYNODEPROTO.fields_by_name['header'].message_type = client_dot_admin_dot_v1__7_dot_pfs_dot_pfs__pb2._OBJECT
_DIRECTORYNODEPROTO.fields_by_name['footer'].message_type = client_dot_admin_dot_v1__7_dot_pfs_dot_pfs__pb2._OBJECT
_NODEPROTO.fields_by_name['file_node'].message_type = _FILENODEPROTO
_NODEPROTO.fields_by_name['dir_node'].message_type = _DIRECTORYNODEPROTO
_HASHTREEPROTO_FSENTRY.fields_by_name['value'].message_type = _NODEPROTO
_HASHTREEPROTO_FSENTRY.containing_type = _HASHTREEPROTO
_HASHTREEPROTO.fields_by_name['fs'].message_type = _HASHTREEPROTO_FSENTRY
DESCRIPTOR.message_types_by_name['FileNodeProto'] = _FILENODEPROTO
DESCRIPTOR.message_types_by_name['DirectoryNodeProto'] = _DIRECTORYNODEPROTO
DESCRIPTOR.message_types_by_name['NodeProto'] = _NODEPROTO
DESCRIPTOR.message_types_by_name['HashTreeProto'] = _HASHTREEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileNodeProto = _reflection.GeneratedProtocolMessageType('FileNodeProto', (_message.Message,), {
  'DESCRIPTOR' : _FILENODEPROTO,
  '__module__' : 'client.admin.v1_7.hashtree.hashtree_pb2'
  # @@protoc_insertion_point(class_scope:hashtree_1_7.FileNodeProto)
  })
_sym_db.RegisterMessage(FileNodeProto)

DirectoryNodeProto = _reflection.GeneratedProtocolMessageType('DirectoryNodeProto', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTORYNODEPROTO,
  '__module__' : 'client.admin.v1_7.hashtree.hashtree_pb2'
  # @@protoc_insertion_point(class_scope:hashtree_1_7.DirectoryNodeProto)
  })
_sym_db.RegisterMessage(DirectoryNodeProto)

NodeProto = _reflection.GeneratedProtocolMessageType('NodeProto', (_message.Message,), {
  'DESCRIPTOR' : _NODEPROTO,
  '__module__' : 'client.admin.v1_7.hashtree.hashtree_pb2'
  # @@protoc_insertion_point(class_scope:hashtree_1_7.NodeProto)
  })
_sym_db.RegisterMessage(NodeProto)

HashTreeProto = _reflection.GeneratedProtocolMessageType('HashTreeProto', (_message.Message,), {

  'FsEntry' : _reflection.GeneratedProtocolMessageType('FsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HASHTREEPROTO_FSENTRY,
    '__module__' : 'client.admin.v1_7.hashtree.hashtree_pb2'
    # @@protoc_insertion_point(class_scope:hashtree_1_7.HashTreeProto.FsEntry)
    })
  ,
  'DESCRIPTOR' : _HASHTREEPROTO,
  '__module__' : 'client.admin.v1_7.hashtree.hashtree_pb2'
  # @@protoc_insertion_point(class_scope:hashtree_1_7.HashTreeProto)
  })
_sym_db.RegisterMessage(HashTreeProto)
_sym_db.RegisterMessage(HashTreeProto.FsEntry)


DESCRIPTOR._options = None
_HASHTREEPROTO_FSENTRY._options = None
# @@protoc_insertion_point(module_scope)
