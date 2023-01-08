# Inputs and outputs: putting it all together(GPIO-0-Boot Button with External LED) 
import machine
import utime
led_red = machine.Pin(18, machine.Pin.OUT)
led_amber = machine.Pin(26, machine.Pin.OUT)
led_green = machine.Pin(27, machine.Pin.OUT)
while True:
  led_red.value(1)
  utime.sleep(5)
  led_amber.value(1)
  utime.sleep(2)
  led_red.value(0)
  led_amber.value(0)
  led_green.value(1)
  utime.sleep(5)
  led_green.value(0)
  led_amber.value(1)
  utime.sleep(5)
  led_amber.value(0)
