#!/usr/bin/env python

import nxt.locator
from nxt.motor import *
import nxt.bluesock

def spin_around(b):
    m_left = Motor(b, PORT_A)
    m_left.turn(-10, 40)

# b = nxt.locator.find_one_brick()
b = nxt.bluesock.BlueSock('00:16:53:06:8C:55').connect()
spin_around(b)