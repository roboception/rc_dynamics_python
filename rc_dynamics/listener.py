#!/usr/bin/env python

from __future__ import print_function, absolute_import

import sys
import logging
import socket
import threading

from google.protobuf.message import DecodeError

from os import path
sys.path.append(path.dirname(path.abspath(__file__)))

from roboception.msgs.frame_pb2 import Frame
from roboception.msgs.dynamics_pb2 import Dynamics
from roboception.msgs.imu_pb2 import Imu


class RcUdpListener(threading.Thread):
    """
    Asynchronous listener for Roboception UDP protobuf messages. Executes
    `default_callback()` during execution of `run()` per default. Accepts custom
    callback functions passed during construction. Use `start()` to start the
    listener and use `stop()` and `join()` after execution of the listener.
    """
    def __init__(self, msgtype, port, interface='', callback=None):
        super(RcUdpListener, self).__init__()
        self._running = False
        self.port = port
        self.msgtype = msgtype
        self.callback = callback if callback is not None else self.default_callback

        logging.info("Binding socket to listen for %s on %s, port %s" % (msgtype, interface, port))
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((interface, port))
            self.sock.settimeout(1.0)
        except socket.error as msg:
            logging.fatal('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit(1)

    def default_callback(self, msg):
        # Do something with the message...
        # print as an example
        logging.info("New {} message:\n{}".format(self.msgtype, msg))

    def run(self):
        self._running = True
        while self._running:
            # Receive response
            try:
                data, server = self.sock.recvfrom(2048)
            except socket.timeout as e:
                continue
            except socket.error as msg:
                # don't print Interrupted system call
                if msg[0] != 4:
                    logging.warning('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
                return
            logging.debug('received %d bytes from %s' % (len(data), server))
            self.handle_msg(data)

    def handle_msg(self, data):
        if self.msgtype == "Frame":
            msg = Frame()
        elif self.msgtype == "Dynamics":
            msg = Dynamics()
        elif self.msgtype == "Imu":
            msg = Imu()
        else:
            sys.exit("ERROR: Specified message type not supported [-t]!")
        try:
            msg.ParseFromString(data)
        except DecodeError as e:
            logging.warning(e)
            return
        self.callback(msg)

    def stop(self):
        self._running = False
        self.sock.close()


def main():
    import argparse
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Receive rc_dynamics messages via UDP and print them.")
    parser.add_argument("-p", "--port", default=9000, type=int,
                        help="UDP port to listen for incoming messages (default: 9000)")
    parser.add_argument("msgtype", type=str, choices=['Frame', 'Imu', 'Dynamics'],
                        help="rc_dynamics message type to be received via UDP port")

    opts = parser.parse_args()

    ul = None
    try:
        ul = RcUdpListener(msgtype=opts.msgtype, port=opts.port)
        ul.start()
        while True:
            pass
    except KeyboardInterrupt:
        logging.info("Received keyboard interrupt.")
    finally:
        logging.info("Shutting down.")
        if ul is not None:
            ul.stop()
            ul.join()


if __name__ == '__main__':
    main()
