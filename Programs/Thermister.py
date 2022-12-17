from machine import Pin, ADC
from time import sleep

temp = ADC(Pin(39))             # Termister -GPIO39
temp.atten(ADC.ATTN_11DB)       # Full range: 3.3v
led = Pin(18,Pin.OUT)

while True:
  temp_value = temp.read()
  print(temp_value)
  if  temp_value > 1900:
    led.value(1)
  else:
    led.value(0)
  
  



