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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10simulation.proto\x12\nsimulation\"4\n\x12SimCurrentStateReq\x12\x13\n\x06\x62odyID\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_bodyID\"\x1d\n\x05Vec2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\" \n\x0b\x43onfigValid\x12\x11\n\tsucceeded\x18\x01 \x01(\x08\"x\n\x0e\x42odyAttributes\x12#\n\x08velocity\x18\x01 \x01(\x0b\x32\x11.simulation.Vec2D\x12#\n\x08position\x18\x02 \x01(\x0b\x32\x11.simulation.Vec2D\x12\x0c\n\x04mass\x18\x03 \x01(\x02\x12\x0e\n\x06\x62odyID\x18\x04 \x01(\r\"6\n\x08SimState\x12*\n\x06\x62odies\x18\x01 \x03(\x0b\x32\x1a.simulation.BodyAttributes2\x90\x01\n\x03Sim\x12\x44\n\nStateReply\x12\x1e.simulation.SimCurrentStateReq\x1a\x14.simulation.SimState\"\x00\x12\x43\n\x10SetConfiguration\x12\x14.simulation.SimState\x1a\x17.simulation.ConfigValid\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simulation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIMCURRENTSTATEREQ']._serialized_start=32
  _globals['_SIMCURRENTSTATEREQ']._serialized_end=84
  _globals['_VEC2D']._serialized_start=86
  _globals['_VEC2D']._serialized_end=115
  _globals['_CONFIGVALID']._serialized_start=117
  _globals['_CONFIGVALID']._serialized_end=149
  _globals['_BODYATTRIBUTES']._serialized_start=151
  _globals['_BODYATTRIBUTES']._serialized_end=271
  _globals['_SIMSTATE']._serialized_start=273
  _globals['_SIMSTATE']._serialized_end=327
  _globals['_SIM']._serialized_start=330
  _globals['_SIM']._serialized_end=474
# @@protoc_insertion_point(module_scope)
