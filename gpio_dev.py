from signal import pause
from gpiozero import LED,Button
from time import sleep

red_led = LED(17)
yellow_led = LED(22)
green_led = LED(27)
#button = Button(2)
while True:
   red_led.on()
   sleep(2.5)
   red_led.off()
   green_led.on()
   sleep(2)
   green_led.off()
   yellow_led.on()
   sleep(1.5)
   yellow_led.off()
   green_led.on()
   sleep(2)
   green_led.off()

#button.when_pressed = led.on
#button.when_released = led.off

#pause()
