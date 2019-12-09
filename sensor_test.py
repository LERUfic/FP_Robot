import nxt.locator
from nxt.sensor import *
import nxt.bluesock
# b = nxt.locator.find_one_brick()
b = nxt.bluesock.BlueSock('00:16:53:06:8C:55').connect()
ultrasonic1 = Ultrasonic(b, PORT_1)
while True:
	# print 'Ultrasonic4 :', Ultrasonic(b, PORT_4).get_sample()
	print ultrasonic1.get_sample()
