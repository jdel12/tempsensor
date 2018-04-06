import pigpio
from time import sleep
import time

pi = pigpio.pi()

import DHT22 
s = DHT22.sensor(pi, 4)
s.trigger()
sleep(.03) # Necessary on faster Raspberry Pi's


count = 0

while count != 10000:
    print time.time()
    print s.humidity()/1.
    print s.temperature()/1.
    s.trigger()
    sleep(.03)
    count += 1
    print time.time()
    print "end"

s.cancel()
pi.stop()
