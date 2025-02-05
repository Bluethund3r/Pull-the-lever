import time
from machine import Pin

SLEEP_TIME = 1
MAX_BLINKS = 20

def blink_led():
    led.toggle()
    time.sleep(SLEEP_TIME)
    
led = Pin(25, Pin.OUT)

led.off()
count = 0

while count < MAX_BLINKS:
    blink_led()
    count =  count + 1
led.off()
print('done')
