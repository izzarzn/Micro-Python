import machine
import utime
sensor_pir = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)  # GPIO-26
led = machine.Pin(18, machine.Pin.OUT)  # GPIO-18
buzzer = machine.Pin(14, machine.Pin.OUT) # GPIO-14

def pir_handler(pin):
  utime.sleep_ms(100)
  if pin.value():
    print("ALARM! Motion detected!")
    for i in range(10):
      led.value(1)
      buzzer.value(1)
      utime.sleep_ms(100)
      led.value(0)
      buzzer.value(0)
      utime.sleep_ms(100)
      

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
  led.value(1)
  utime.sleep(5)
  led.value(0)
  utime.sleep(5)
  


