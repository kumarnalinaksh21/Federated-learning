# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/execution/v1/protocol.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2
from syft_proto.execution.v1 import role_pb2 as syft__proto_dot_execution_dot_v1_dot_role__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/execution/v1/protocol.proto',
  package='syft_proto.execution.v1',
  syntax='proto3',
  serialized_options=b'\n$org.openmined.syftproto.execution.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&syft_proto/execution/v1/protocol.proto\x12\x17syft_proto.execution.v1\x1a!syft_proto/types/syft/v1/id.proto\x1a\"syft_proto/execution/v1/role.proto\"\x9f\x02\n\x08Protocol\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x42\n\x05roles\x18\x03 \x03(\x0b\x32,.syft_proto.execution.v1.Protocol.RolesEntryR\x05roles\x12\x12\n\x04tags\x18\x04 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x1aW\n\nRolesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.syft_proto.execution.v1.RoleR\x05value:\x02\x38\x01\x42&\n$org.openmined.syftproto.execution.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,syft__proto_dot_execution_dot_v1_dot_role__pb2.DESCRIPTOR,])




_PROTOCOL_ROLESENTRY = _descriptor.Descriptor(
  name='RolesEntry',
  full_name='syft_proto.execution.v1.Protocol.RolesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='syft_proto.execution.v1.Protocol.RolesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='syft_proto.execution.v1.Protocol.RolesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=426,
)

_PROTOCOL = _descriptor.Descriptor(
  name='Protocol',
  full_name='syft_proto.execution.v1.Protocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.execution.v1.Protocol.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='syft_proto.execution.v1.Protocol.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roles', full_name='syft_proto.execution.v1.Protocol.roles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='roles', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='syft_proto.execution.v1.Protocol.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='syft_proto.execution.v1.Protocol.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PROTOCOL_ROLESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=426,
)

_PROTOCOL_ROLESENTRY.fields_by_name['value'].message_type = syft__proto_dot_execution_dot_v1_dot_role__pb2._ROLE
_PROTOCOL_ROLESENTRY.containing_type = _PROTOCOL
_PROTOCOL.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_PROTOCOL.fields_by_name['roles'].message_type = _PROTOCOL_ROLESENTRY
DESCRIPTOR.message_types_by_name['Protocol'] = _PROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Protocol = _reflection.GeneratedProtocolMessageType('Protocol', (_message.Message,), {

  'RolesEntry' : _reflection.GeneratedProtocolMessageType('RolesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROTOCOL_ROLESENTRY,
    '__module__' : 'syft_proto.execution.v1.protocol_pb2'
    # @@protoc_insertion_point(class_scope:syft_proto.execution.v1.Protocol.RolesEntry)
    })
  ,
  'DESCRIPTOR' : _PROTOCOL,
  '__module__' : 'syft_proto.execution.v1.protocol_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.execution.v1.Protocol)
  })
_sym_db.RegisterMessage(Protocol)
_sym_db.RegisterMessage(Protocol.RolesEntry)


DESCRIPTOR._options = None
_PROTOCOL_ROLESENTRY._options = None
# @@protoc_insertion_point(module_scope)