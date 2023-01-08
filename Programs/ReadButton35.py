# Read data from Button which is connected at GPIO-35 
import machine
import utime
button = machine.Pin(35, machine.Pin.IN)
while True:
  if button.value() == 1:
    print("You pressed the button!")
    utime.sleep(2)
