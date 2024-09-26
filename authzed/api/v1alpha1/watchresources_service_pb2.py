# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: authzed/api/v1alpha1/watchresources_service.proto
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
    'authzed/api/v1alpha1/watchresources_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1authzed/api/v1alpha1/watchresources_service.proto\x12\x14\x61uthzed.api.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x19\x61uthzed/api/v1/core.proto\"\x96\x03\n\x15WatchResourcesRequest\x12z\n\x14resource_object_type\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x12resourceObjectType\x12G\n\npermission\x18\x02 \x01(\tB\'\xfa\x42$r\"(@2\x1e^[a-z][a-z0-9_]{1,62}[a-z0-9]$R\npermission\x12.\n\x13subject_object_type\x18\x03 \x01(\tR\x11subjectObjectType\x12:\n\x19optional_subject_relation\x18\x04 \x01(\tR\x17optionalSubjectRelation\x12L\n\x15optional_start_cursor\x18\x05 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x13optionalStartCursor\"\x84\x03\n\x10PermissionUpdate\x12:\n\x07subject\x18\x01 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceR\x07subject\x12;\n\x08resource\x18\x02 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceR\x08resource\x12\x1a\n\x08relation\x18\x03 \x01(\tR\x08relation\x12\x64\n\x12updated_permission\x18\x04 \x01(\x0e\x32\x35.authzed.api.v1alpha1.PermissionUpdate.PermissionshipR\x11updatedPermission\"u\n\x0ePermissionship\x12\x1e\n\x1aPERMISSIONSHIP_UNSPECIFIED\x10\x00\x12 \n\x1cPERMISSIONSHIP_NO_PERMISSION\x10\x01\x12!\n\x1dPERMISSIONSHIP_HAS_PERMISSION\x10\x02\"\x9d\x01\n\x16WatchResourcesResponse\x12@\n\x07updates\x18\x01 \x03(\x0b\x32&.authzed.api.v1alpha1.PermissionUpdateR\x07updates\x12\x41\n\x0f\x63hanges_through\x18\x02 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x0e\x63hangesThrough2\xa9\x01\n\x15WatchResourcesService\x12\x8f\x01\n\x0eWatchResources\x12+.authzed.api.v1alpha1.WatchResourcesRequest\x1a,.authzed.api.v1alpha1.WatchResourcesResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1alpha1/lookupwatch:\x01*0\x01\x42T\n\x18\x63om.authzed.api.v1alpha1Z8github.com/authzed/authzed-go/proto/authzed/api/v1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1alpha1.watchresources_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.authzed.api.v1alpha1Z8github.com/authzed/authzed-go/proto/authzed/api/v1alpha1'
  _globals['_WATCHRESOURCESREQUEST'].fields_by_name['resource_object_type']._loaded_options = None
  _globals['_WATCHRESOURCESREQUEST'].fields_by_name['resource_object_type']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_WATCHRESOURCESREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_WATCHRESOURCESREQUEST'].fields_by_name['permission']._serialized_options = b'\372B$r\"(@2\036^[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_WATCHRESOURCESSERVICE'].methods_by_name['WatchResources']._loaded_options = None
  _globals['_WATCHRESOURCESSERVICE'].methods_by_name['WatchResources']._serialized_options = b'\202\323\344\223\002\032\"\025/v1alpha1/lookupwatch:\001*'
  _globals['_WATCHRESOURCESREQUEST']._serialized_start=158
  _globals['_WATCHRESOURCESREQUEST']._serialized_end=564
  _globals['_PERMISSIONUPDATE']._serialized_start=567
  _globals['_PERMISSIONUPDATE']._serialized_end=955
  _globals['_PERMISSIONUPDATE_PERMISSIONSHIP']._serialized_start=838
  _globals['_PERMISSIONUPDATE_PERMISSIONSHIP']._serialized_end=955
  _globals['_WATCHRESOURCESRESPONSE']._serialized_start=958
  _globals['_WATCHRESOURCESRESPONSE']._serialized_end=1115
  _globals['_WATCHRESOURCESSERVICE']._serialized_start=1118
  _globals['_WATCHRESOURCESSERVICE']._serialized_end=1287
# @@protoc_insertion_point(module_scope)
