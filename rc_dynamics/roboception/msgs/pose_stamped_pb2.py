# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: roboception/msgs/pose_stamped.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import roboception.msgs.time_pb2
import roboception.msgs.pose_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='roboception/msgs/pose_stamped.proto',
  package='roboception.msgs',
  serialized_pb='\n#roboception/msgs/pose_stamped.proto\x12\x10roboception.msgs\x1a\x1broboception/msgs/time.proto\x1a\x1broboception/msgs/pose.proto\"^\n\x0bPoseStamped\x12)\n\ttimestamp\x18\x01 \x01(\x0b\x32\x16.roboception.msgs.Time\x12$\n\x04pose\x18\x02 \x01(\x0b\x32\x16.roboception.msgs.PoseB)\n\x14\x63om.roboception.msgsB\x11PoseStampedProtos')




_POSESTAMPED = _descriptor.Descriptor(
  name='PoseStamped',
  full_name='roboception.msgs.PoseStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='roboception.msgs.PoseStamped.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pose', full_name='roboception.msgs.PoseStamped.pose', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=115,
  serialized_end=209,
)

_POSESTAMPED.fields_by_name['timestamp'].message_type = roboception.msgs.time_pb2._TIME
_POSESTAMPED.fields_by_name['pose'].message_type = roboception.msgs.pose_pb2._POSE
DESCRIPTOR.message_types_by_name['PoseStamped'] = _POSESTAMPED

class PoseStamped(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POSESTAMPED

  # @@protoc_insertion_point(class_scope:roboception.msgs.PoseStamped)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\024com.roboception.msgsB\021PoseStampedProtos')
# @@protoc_insertion_point(module_scope)