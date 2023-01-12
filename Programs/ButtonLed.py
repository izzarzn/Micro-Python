# Inputs and outputs: putting it all together
import machine
import utime
led_external = machine.Pin(18, machine.Pin.OUT)
button = machine.Pin(35, machine.Pin.IN)
while True:
  if button.value() == 1:
    led_external.value(1)
    utime.sleep(2)
  led_external.value(0)
