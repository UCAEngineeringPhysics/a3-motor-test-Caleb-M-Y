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

INA_LEFT.on()
INA_RIGHT.on()
PWM_LEFT.duty_u16(65025/2)
PWM_RIGHT.duty_u16(65025/2)
sleep(60)

INA_LEFT.off()
INA_RIGHT.off()
PWM_LEFT.duty_u16(0)
PWM_RIGHT.duty_u16(0)
