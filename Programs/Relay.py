# 4. Switch on a relay at a given time using sleep function, where the relay’s contact terminals are connected to a load.

from machine import Pin
from time import sleep

relay = Pin(13,Pin.OUT)  # Relay
relay.value(0)
sleep(10.0)
relay.value(0)
sleep(2.0)
