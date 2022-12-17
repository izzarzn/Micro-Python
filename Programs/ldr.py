
from machine import Pin, ADC
from time import sleep

ldr = ADC(Pin(36))             # LDR -GPIO36
ldr.atten(ADC.ATTN_11DB)       # Full range: 3.3v
led = Pin(18,Pin.OUT)

while True:
  ldr_value = ldr.read()
  print(ldr_value)
  sleep(1.0)
  if  ldr_value < 500:
    led.value(1)
  else:
    led.value(0)
  
  




