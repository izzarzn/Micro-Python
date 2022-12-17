# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

buzzer = Pin(14, Pin.OUT)
pir = Pin(0, Pin.IN)        # GPIO 0 used as Interrupting source (Falling edge 1->0)

pir.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    buzzer.value(1)
    sleep(1)
    buzzer.value(0)
    print('Motion stopped!')
    motion = False


