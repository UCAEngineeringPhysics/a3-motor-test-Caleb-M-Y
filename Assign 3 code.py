from machine import Pin, PWM, Timer
from time import sleep
import time

INA_LEFT = Pin(12, Pin.OUT)
INA_RIGHT = Pin(19, Pin.OUT)
INB_LEFT = Pin(11, Pin.OUT)
INB_RIGHT = Pin(20, Pin.OUT)
INA_LEFT.off()
INA_RIGHT.off()
INB_LEFT.off()
INB_RIGHT.off()
PWM_LEFT = PWM(Pin(13))
PWM_RIGHT = PWM(Pin(18))
PWM_LEFT.freq(1000)
PWM_RIGHT.freq(1000)

#ramp up speed forward
INA_LEFT.on()
#INA_RIGHT.on()
INB_LEFT.off()
PWM_LEFT.duty_u16(65025)
#INA_RIGHT.on()
#for duty in range(65025, 0 ,4):
    #PWM_LEFT.duty_u16(duty)
    #PWM_RIGHT.duty_u16(duty)
   # sleep(0.5)
    
#INA_LEFT.off()
#INA_RIGHT.off()
#INB_LEFT.off()
#INB_RIGHT.off()

#slow down speed forward


#ramp up speed backward


#slow down speed backward

