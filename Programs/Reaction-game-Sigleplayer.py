# Build a simple reaction timing game using an LED and push-button, for single player.
import machine
import utime
import urandom
pressed = False
led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN)

def button_handler(pin):
  global pressed
  if not pressed:
    pressed=True
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Your reaction time was " + str(timer_reaction) + " milliseconds!")
    
    
led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_start = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
