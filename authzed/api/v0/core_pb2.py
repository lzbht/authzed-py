# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: authzed/api/v0/core.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'authzed/api/v0/core.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61uthzed/api/v0/core.proto\x12\x0e\x61uthzed.api.v0\x1a\x17validate/validate.proto\"\xa0\x01\n\rRelationTuple\x12[\n\x13object_and_relation\x18\x01 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x11objectAndRelation\x12\x32\n\x04user\x18\x02 \x01(\x0b\x32\x14.authzed.api.v0.UserB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x04user\"\x9d\x02\n\x11ObjectAndRelation\x12\x66\n\tnamespace\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)?[a-z][a-z0-9_]{1,62}[a-z0-9]$R\tnamespace\x12R\n\tobject_id\x18\x02 \x01(\tB5\xfa\x42\x32r0(\x80\x01\x32+^(([a-zA-Z0-9_][a-zA-Z0-9/_|-]{0,127})|\\*)$R\x08objectId\x12L\n\x08relation\x18\x03 \x01(\tB0\xfa\x42-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{1,62}[a-z0-9])$R\x08relation\"\xc9\x01\n\x11RelationReference\x12\x66\n\tnamespace\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)?[a-z][a-z0-9_]{1,62}[a-z0-9]$R\tnamespace\x12L\n\x08relation\x18\x03 \x01(\tB0\xfa\x42-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{1,62}[a-z0-9])$R\x08relation\"b\n\x04User\x12G\n\x07userset\x18\x02 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x07usersetB\x11\n\nuser_oneof\x12\x03\xf8\x42\x01\x42H\n\x12\x63om.authzed.api.v0Z2github.com/authzed/authzed-go/proto/authzed/api/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v0.core_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.authzed.api.v0Z2github.com/authzed/authzed-go/proto/authzed/api/v0'
  _globals['_RELATIONTUPLE'].fields_by_name['object_and_relation']._loaded_options = None
  _globals['_RELATIONTUPLE'].fields_by_name['object_and_relation']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_RELATIONTUPLE'].fields_by_name['user']._loaded_options = None
  _globals['_RELATIONTUPLE'].fields_by_name['user']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_OBJECTANDRELATION'].fields_by_name['namespace']._loaded_options = None
  _globals['_OBJECTANDRELATION'].fields_by_name['namespace']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)?[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_OBJECTANDRELATION'].fields_by_name['object_id']._loaded_options = None
  _globals['_OBJECTANDRELATION'].fields_by_name['object_id']._serialized_options = b'\372B2r0(\200\0012+^(([a-zA-Z0-9_][a-zA-Z0-9/_|-]{0,127})|\\*)$'
  _globals['_OBJECTANDRELATION'].fields_by_name['relation']._loaded_options = None
  _globals['_OBJECTANDRELATION'].fields_by_name['relation']._serialized_options = b'\372B-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{1,62}[a-z0-9])$'
  _globals['_RELATIONREFERENCE'].fields_by_name['namespace']._loaded_options = None
  _globals['_RELATIONREFERENCE'].fields_by_name['namespace']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)?[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_RELATIONREFERENCE'].fields_by_name['relation']._loaded_options = None
  _globals['_RELATIONREFERENCE'].fields_by_name['relation']._serialized_options = b'\372B-r+(@2\'^(\\.\\.\\.|[a-z][a-z0-9_]{1,62}[a-z0-9])$'
  _globals['_USER'].oneofs_by_name['user_oneof']._loaded_options = None
  _globals['_USER'].oneofs_by_name['user_oneof']._serialized_options = b'\370B\001'
  _globals['_USER'].fields_by_name['userset']._loaded_options = None
  _globals['_USER'].fields_by_name['userset']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_RELATIONTUPLE']._serialized_start=71
  _globals['_RELATIONTUPLE']._serialized_end=231
  _globals['_OBJECTANDRELATION']._serialized_start=234
  _globals['_OBJECTANDRELATION']._serialized_end=519
  _globals['_RELATIONREFERENCE']._serialized_start=522
  _globals['_RELATIONREFERENCE']._serialized_end=723
  _globals['_USER']._serialized_start=725
  _globals['_USER']._serialized_end=823
# @@protoc_insertion_point(module_scope)
