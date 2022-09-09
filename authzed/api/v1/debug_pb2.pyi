"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v1.core_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DebugInformation(google.protobuf.message.Message):
    """DebugInformation defines debug information returned by an API call in a footer when
    requested with a specific debugging header.

    The specific debug information returned will depend on the type of the API call made.

    See the github.com/authzed/authzed-go project for the specific header and footer names.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECK_FIELD_NUMBER: builtins.int
    SCHEMA_USED_FIELD_NUMBER: builtins.int
    @property
    def check(self) -> global___CheckDebugTrace:
        """check holds debug information about a check request."""
    schema_used: builtins.str
    """schema_used holds the schema used for the request."""
    def __init__(
        self,
        *,
        check: global___CheckDebugTrace | None = ...,
        schema_used: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["check", b"check"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["check", b"check", "schema_used", b"schema_used"]) -> None: ...

global___DebugInformation = DebugInformation

class CheckDebugTrace(google.protobuf.message.Message):
    """CheckDebugTrace is a recursive trace of the requests made for resolving a CheckPermission
    API call.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _PermissionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PermissionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CheckDebugTrace._PermissionType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PERMISSION_TYPE_UNSPECIFIED: CheckDebugTrace._PermissionType.ValueType  # 0
        PERMISSION_TYPE_RELATION: CheckDebugTrace._PermissionType.ValueType  # 1
        PERMISSION_TYPE_PERMISSION: CheckDebugTrace._PermissionType.ValueType  # 2

    class PermissionType(_PermissionType, metaclass=_PermissionTypeEnumTypeWrapper): ...
    PERMISSION_TYPE_UNSPECIFIED: CheckDebugTrace.PermissionType.ValueType  # 0
    PERMISSION_TYPE_RELATION: CheckDebugTrace.PermissionType.ValueType  # 1
    PERMISSION_TYPE_PERMISSION: CheckDebugTrace.PermissionType.ValueType  # 2

    class _Permissionship:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PermissionshipEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CheckDebugTrace._Permissionship.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PERMISSIONSHIP_UNSPECIFIED: CheckDebugTrace._Permissionship.ValueType  # 0
        PERMISSIONSHIP_NO_PERMISSION: CheckDebugTrace._Permissionship.ValueType  # 1
        PERMISSIONSHIP_HAS_PERMISSION: CheckDebugTrace._Permissionship.ValueType  # 2

    class Permissionship(_Permissionship, metaclass=_PermissionshipEnumTypeWrapper): ...
    PERMISSIONSHIP_UNSPECIFIED: CheckDebugTrace.Permissionship.ValueType  # 0
    PERMISSIONSHIP_NO_PERMISSION: CheckDebugTrace.Permissionship.ValueType  # 1
    PERMISSIONSHIP_HAS_PERMISSION: CheckDebugTrace.Permissionship.ValueType  # 2

    class SubProblems(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRACES_FIELD_NUMBER: builtins.int
        @property
        def traces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CheckDebugTrace]: ...
        def __init__(
            self,
            *,
            traces: collections.abc.Iterable[global___CheckDebugTrace] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["traces", b"traces"]) -> None: ...

    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    PERMISSION_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    WAS_CACHED_RESULT_FIELD_NUMBER: builtins.int
    SUB_PROBLEMS_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference:
        """resource holds the resource on which the Check was performed."""
    permission: builtins.str
    """permission holds the name of the permission or relation on which the Check was performed."""
    permission_type: global___CheckDebugTrace.PermissionType.ValueType
    """permission_type holds information indicating whether it was a permission or relation."""
    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference:
        """subject holds the subject on which the Check was performed. This will be static across all calls within
        the same Check tree.
        """
    result: global___CheckDebugTrace.Permissionship.ValueType
    """result holds the result of the Check call."""
    was_cached_result: builtins.bool
    """was_cached_result, if true, indicates that the result was found in the cache and returned directly."""
    @property
    def sub_problems(self) -> global___CheckDebugTrace.SubProblems:
        """sub_problems holds the sub problems that were executed to resolve the answer to this Check. An empty list
        and a permissionship of PERMISSIONSHIP_HAS_PERMISSION indicates the subject was found within this relation.
        """
    def __init__(
        self,
        *,
        resource: authzed.api.v1.core_pb2.ObjectReference | None = ...,
        permission: builtins.str = ...,
        permission_type: global___CheckDebugTrace.PermissionType.ValueType = ...,
        subject: authzed.api.v1.core_pb2.SubjectReference | None = ...,
        result: global___CheckDebugTrace.Permissionship.ValueType = ...,
        was_cached_result: builtins.bool = ...,
        sub_problems: global___CheckDebugTrace.SubProblems | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resolution", b"resolution", "resource", b"resource", "sub_problems", b"sub_problems", "subject", b"subject", "was_cached_result", b"was_cached_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["permission", b"permission", "permission_type", b"permission_type", "resolution", b"resolution", "resource", b"resource", "result", b"result", "sub_problems", b"sub_problems", "subject", b"subject", "was_cached_result", b"was_cached_result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["resolution", b"resolution"]) -> typing_extensions.Literal["was_cached_result", "sub_problems"] | None: ...

global___CheckDebugTrace = CheckDebugTrace