#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
import nxt.bluesock

# b = nxt.locator.find_one_brick()
b = nxt.bluesock.BlueSock('00:16:53:06:8C:55').connect()
while True:
	if Touch(b, PORT_1).get_sample() == False:
		print "salah"
	elif Touch(b, PORT_1).get_sample() == True:
		print "benar"
	# print 'Touch:', Touch(b, PORT_1).get_sample()
	# print 'Ultrasonic:', Ultrasonic(b, PORT_1).get_sample()
	# print 'Sound:', Sound(b, PORT_1).get_sample()


	# print 'Light:', Light(b, PORT_1).get_sample()
