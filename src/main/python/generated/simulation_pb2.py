# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: simulation.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'simulation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10simulation.proto\x12\nsimulation\"(\n\x06SimReq\x12\x13\n\x06\x62odyID\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_bodyID\"\x1d\n\x05Vec2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"Z\n\x0e\x42odyAttributes\x12#\n\x08velocity\x18\x01 \x01(\x0b\x32\x11.simulation.Vec2D\x12#\n\x08position\x18\x02 \x01(\x0b\x32\x11.simulation.Vec2D\"9\n\x0bSimResponse\x12*\n\x06\x62odies\x18\x01 \x03(\x0b\x32\x1a.simulation.BodyAttributes2?\n\x03Sim\x12\x38\n\x07Replies\x12\x12.simulation.SimReq\x1a\x17.simulation.SimResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simulation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIMREQ']._serialized_start=32
  _globals['_SIMREQ']._serialized_end=72
  _globals['_VEC2D']._serialized_start=74
  _globals['_VEC2D']._serialized_end=103
  _globals['_BODYATTRIBUTES']._serialized_start=105
  _globals['_BODYATTRIBUTES']._serialized_end=195
  _globals['_SIMRESPONSE']._serialized_start=197
  _globals['_SIMRESPONSE']._serialized_end=254
  _globals['_SIM']._serialized_start=256
  _globals['_SIM']._serialized_end=319
# @@protoc_insertion_point(module_scope)
