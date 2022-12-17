# 3.	Flash an LED at a given on time and off time cycle, where the two times are taken from a file.
from machine import Pin
from time import sleep

led = Pin(18, Pin.OUT)
try:
   s = open('delay.txt','r')
   line = s.readline()
   s.close()
except:
  print('No such File')      
delay=line.split()
on=float(delay[0])
off=float(delay[1])
print('ON:',on)
print('OFF:',off)
while True:
  led.value(1)
  sleep(on)
  led.value(0)
  sleep(off)



