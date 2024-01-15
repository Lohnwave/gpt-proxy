# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/gpt_proto/gpt_request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"client/gpt_proto/gpt_request.proto\x12\x0bgpt.request\"N\n\x0eRequestContext\x12\x15\n\rbusiness_name\x18\x01 \x01(\t\x12\x12\n\ntime_limit\x18\x02 \x01(\x05\x12\x11\n\tclient_ip\x18\x03 \x01(\t\"\x84\x01\n\x08UserData\x12\x0c\n\x04imei\x18\x01 \x01(\t\x12\x38\n\nschema_map\x18\x02 \x03(\x0b\x32$.gpt.request.UserData.SchemaMapEntry\x1a\x30\n\x0eSchemaMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x08ItemData\x12\r\n\x05texts\x18\x01 \x03(\x0c\x12\x0e\n\x06images\x18\x02 \x03(\x0c\x12\x0e\n\x06\x61udios\x18\x03 \x03(\x0c\x12\x0e\n\x06videos\x18\x04 \x03(\x0c\"l\n\x07\x43ontent\x12\r\n\x05query\x18\x01 \x01(\t\x12(\n\tuser_data\x18\x02 \x01(\x0b\x32\x15.gpt.request.UserData\x12(\n\titem_data\x18\x03 \x01(\x0b\x32\x15.gpt.request.ItemData\"\xd4\x01\n\x07Request\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12,\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x1b.gpt.request.RequestContext\x12%\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x14.gpt.request.Content\x12\x31\n\x07\x65xt_map\x18\n \x03(\x0b\x32 .gpt.request.Request.ExtMapEntry\x1a-\n\x0b\x45xtMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x03\xf8\x01\x01\x62\x06proto3')



_REQUESTCONTEXT = DESCRIPTOR.message_types_by_name['RequestContext']
_USERDATA = DESCRIPTOR.message_types_by_name['UserData']
_USERDATA_SCHEMAMAPENTRY = _USERDATA.nested_types_by_name['SchemaMapEntry']
_ITEMDATA = DESCRIPTOR.message_types_by_name['ItemData']
_CONTENT = DESCRIPTOR.message_types_by_name['Content']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REQUEST_EXTMAPENTRY = _REQUEST.nested_types_by_name['ExtMapEntry']
RequestContext = _reflection.GeneratedProtocolMessageType('RequestContext', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCONTEXT,
  '__module__' : 'client.gpt_proto.gpt_request_pb2'
  # @@protoc_insertion_point(class_scope:gpt.request.RequestContext)
  })
_sym_db.RegisterMessage(RequestContext)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {

  'SchemaMapEntry' : _reflection.GeneratedProtocolMessageType('SchemaMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _USERDATA_SCHEMAMAPENTRY,
    '__module__' : 'client.gpt_proto.gpt_request_pb2'
    # @@protoc_insertion_point(class_scope:gpt.request.UserData.SchemaMapEntry)
    })
  ,
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'client.gpt_proto.gpt_request_pb2'
  # @@protoc_insertion_point(class_scope:gpt.request.UserData)
  })
_sym_db.RegisterMessage(UserData)
_sym_db.RegisterMessage(UserData.SchemaMapEntry)

ItemData = _reflection.GeneratedProtocolMessageType('ItemData', (_message.Message,), {
  'DESCRIPTOR' : _ITEMDATA,
  '__module__' : 'client.gpt_proto.gpt_request_pb2'
  # @@protoc_insertion_point(class_scope:gpt.request.ItemData)
  })
_sym_db.RegisterMessage(ItemData)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
  'DESCRIPTOR' : _CONTENT,
  '__module__' : 'client.gpt_proto.gpt_request_pb2'
  # @@protoc_insertion_point(class_scope:gpt.request.Content)
  })
_sym_db.RegisterMessage(Content)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'ExtMapEntry' : _reflection.GeneratedProtocolMessageType('ExtMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_EXTMAPENTRY,
    '__module__' : 'client.gpt_proto.gpt_request_pb2'
    # @@protoc_insertion_point(class_scope:gpt.request.Request.ExtMapEntry)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'client.gpt_proto.gpt_request_pb2'
  # @@protoc_insertion_point(class_scope:gpt.request.Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.ExtMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _USERDATA_SCHEMAMAPENTRY._options = None
  _USERDATA_SCHEMAMAPENTRY._serialized_options = b'8\001'
  _REQUEST_EXTMAPENTRY._options = None
  _REQUEST_EXTMAPENTRY._serialized_options = b'8\001'
  _REQUESTCONTEXT._serialized_start=51
  _REQUESTCONTEXT._serialized_end=129
  _USERDATA._serialized_start=132
  _USERDATA._serialized_end=264
  _USERDATA_SCHEMAMAPENTRY._serialized_start=216
  _USERDATA_SCHEMAMAPENTRY._serialized_end=264
  _ITEMDATA._serialized_start=266
  _ITEMDATA._serialized_end=339
  _CONTENT._serialized_start=341
  _CONTENT._serialized_end=449
  _REQUEST._serialized_start=452
  _REQUEST._serialized_end=664
  _REQUEST_EXTMAPENTRY._serialized_start=619
  _REQUEST_EXTMAPENTRY._serialized_end=664
# @@protoc_insertion_point(module_scope)