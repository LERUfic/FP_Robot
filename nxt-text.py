#!/usr/bin/env python

#Lists various information from all bricks it can connect to.

import sys, traceback

if '--help' in sys.argv:
    print '''nxt_test -- Tests the nxt-python setup and brick firmware interaction
Usage:  nxt_test (takes no arguments except --help)'''
    exit(0)

import nxt.locator
import nxt.brick
from nxt.motor import *

try:
    b = nxt.locator.find_one_brick()
    m_left = Motor(b, PORT_B)
    m_left.turn(5, 10)
    name, host, signal_strength, user_flash = b.get_device_info()
    print 'NXT brick name: %s' % name
    print 'Host address: %s' % host
    print 'Bluetooth signal strength: %s' % signal_strength
    print 'Free user flash: %s' % user_flash
    prot_version, fw_version = b.get_firmware_version()
    print 'Protocol version %s.%s' % prot_version
    print 'Firmware version %s.%s' % fw_version
    millivolts = b.get_battery_level()
    print 'Battery level %s mV' % millivolts
    b.sock.close()
except:
    print "Error while running test:"
    traceback.print_tb(sys.exc_info()[2])
    print str(sys.exc_info()[1])
    if b:
        b.sock.close()