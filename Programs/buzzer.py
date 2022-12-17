from machine import Pin
from time import sleep

buzzer = Pin(14,Pin.OUT)
button = Pin(35, Pin.IN)

while True:
  if button.value():
    buzzer.value(1)
  else:
    buzzer.value(0)  

