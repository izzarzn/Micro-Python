from machine 
import Pin, ADC 
from time 
import sleep 
smoke = ADC(Pin(26)) # Smoke Sensor –GPIO26 
smoke.atten(ADC.ATTN_11DB) # Full range: 3.3v 
buzzer = Pin(14,Pin.OUT) 
while True: 
  smoke_value = smoke.read() 
  print(smoke_value) 
  sleep(1.0) 
  if smoke_value > 50: 
    buzzer.value(1) 
    else: buzzer.value(0)
