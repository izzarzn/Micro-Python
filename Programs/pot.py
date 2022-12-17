from machine import Pin, ADC
from time import sleep

temp = ADC(Pin(39))             # Termister -GPIO39
temp.atten(ADC.ATTN_11DB)       # Full range: 3.3v

while True:
  temp_value = temp.read()
  print(temp_value)
  sleep(1.0)


