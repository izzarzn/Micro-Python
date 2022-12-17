#  2.	Get input from two switches and switch on corresponding LEDs. 

from machine import Pin
from time import sleep

led1 = Pin(18,Pin.OUT)
led0 = Pin(2,Pin.OUT)
button1 = Pin(35, Pin.IN)
button0 = Pin(0, Pin.IN)

while True:
  if button0.value() == 0:
    led0.value(1) 
  else:
    led0.value(0)  
    
  if button1.value():
    led1.value(1)
  else:
    led1.value(0)  

