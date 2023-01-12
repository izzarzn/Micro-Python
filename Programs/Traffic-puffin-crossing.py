# Inputs and outputs: putting it all together(GPIO-0-Boot Button with External LED) 
import machine
import utime
import _thread
led_red = machine.Pin(18, machine.Pin.OUT)
led_amber = machine.Pin(26, machine.Pin.OUT)
led_green = machine.Pin(27, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN)
buzzer = machine.Pin(14, machine.Pin.OUT)
global button_pressed
button_pressed = False

def button_reader_thread():
  global button_pressed
  while True:
    if button.value() == 0:
      button_pressed = True
    utime.sleep(0.01)
      
_thread.start_new_thread(button_reader_thread, ())


while True:
  if button_pressed == True:
    led_red.value(1)
    for i in range(10):
      buzzer.value(1)
      utime.sleep(0.2)
      buzzer.value(0)
      utime.sleep(0.2)
    global button_pressed
    button_pressed = False
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
