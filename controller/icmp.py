#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.icmp import ICMP
from layer.layer import layer


class ICMPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config = loads(self.get_argument('ip'))
        icmp_config = loads(self.get_argument('icmp'))
        mac = ETHER(mac_config)
        ip = IP(ip_config)
        icmp = ICMP(icmp_config)
        s = layer.send([mac, ip, icmp])
        print s
        # print s.recv(4096)
