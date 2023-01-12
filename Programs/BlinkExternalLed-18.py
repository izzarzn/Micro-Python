# Blink External LED connected at GPIO-18
import machine
import utime
led_onboard = machine.Pin(18, machine.Pin.OUT)
while True:
  led_onboard.value(1)
  utime.sleep(1)
  led_onboard.value(0)
  utime.sleep(1)
