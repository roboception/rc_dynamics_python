#
# Makefile for re-generating the roboception protobuf bindings
#

all: gen_python

gen_python:
	protoc -I=rc_dynamics_msgs --python_out=rc_dynamics rc_dynamics_msgs/roboception/msgs/*.proto

clean:
	rm -rf rc_dynamics/roboception

.PHONY: all gen_python clean
