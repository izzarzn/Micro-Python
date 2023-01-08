# Your first physical computing program: Hello, LED!(On Board LED)
import machine
import utime
led_onboard = machine.Pin(2, machine.Pin.OUT)
while True:
  led_onboard.value(1)
  utime.sleep(1)
  led_onboard.value(0)
  utime.sleep(1)
