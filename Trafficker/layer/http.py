#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from Trafficker.layer.layer import layer


class HTTP(layer):

    def __init__(self):
        pass

    def pack(self):
        pass

    @classmethod
    def unpack(cls, packet):
        h = HTTP()
        h.content = packet
        return h


if __name__ == '__main__':
    print(HTTP().name)
