# Inputs and outputs: putting it all together(GPIO-0-Boot Button with External LED) 
import machine
import utime
led_external = machine.Pin(18, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN)
while True:
  if button.value() == 0:
    led_external.value(1)
    utime.sleep(2)
  led_external.value(0)
