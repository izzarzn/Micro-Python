from machine import Pin, ADC
from time import sleep

smoke = ADC(0)
buzzer=Pin(12,Pin.OUT)

while True:
  smoke_value = smoke.read()
  print(smoke_value)
  if smoke_value > 550:
    buzzer.value(1)
    sleep(0.5)
  else:
    buzzer.value(0)
    sleep(0.5)
    


