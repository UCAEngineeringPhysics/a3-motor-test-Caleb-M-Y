#Ramp up motor speed forward for 4 seconds
#slow down motor speed for 4 seconds
#ramp up motor speed backwards for 4 seconds
#slow down the motor speed for 4 seconds
#stop the motors
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

#Ramp up both motors to full speed (forward)
INA_LEFT.on()
INA_RIGHT.on()
PWM_LEFT.duty_u16(int(65025/32)) # 1/32 max speed
PWM_RIGHT.duty_u16(int(65025/32)) # 1/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025/16)) # 2/32 max speed
PWM_RIGHT.duty_u16(int(65025/16)) # 2/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(3/32))) # 3/32 max speed
PWM_RIGHT.duty_u16(int(65025*(3/32))) # 3/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(4/32))) # 4/32 max speed
PWM_RIGHT.duty_u16(int(65025*(4/32))) # 4/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(5/32))) # 5/32 max speed
PWM_RIGHT.duty_u16(int(65025*(5/32))) # 5/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(6/32))) # 6/32 max speed
PWM_RIGHT.duty_u16(int(65025*(6/32))) # 6/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(7/32))) # 7/32 max speed
PWM_RIGHT.duty_u16(int(65025*(7/32))) # 7/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(8/32))) # 8/32 max speed
PWM_RIGHT.duty_u16(int(65025*(8/32))) # 8/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(9/32))) #9/32 max speed
PWM_RIGHT.duty_u16(int(65025*(9/32))) # 9/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(10/32))) # 10/32 max speed
PWM_RIGHT.duty_u16(int(65025*(10/32))) # 10/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(11/32))) # 11/32 max speed
PWM_RIGHT.duty_u16(int(65025*(11/32))) # 11/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(12/32))) # 12/32 max speed
PWM_RIGHT.duty_u16(int(65025*(12/32))) # 12/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(13/32))) # 13/32 max speed
PWM_RIGHT.duty_u16(int(65025*(13/32))) # 13/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(14/32))) # 14/32 max speed
PWM_RIGHT.duty_u16(int(65025*(14/32))) # 14/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(15/32))) #15/32 max speed
PWM_RIGHT.duty_u16(int(65025*(15/32))) # 15/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(1/2))) # 16/32 max speed
PWM_RIGHT.duty_u16(int(65025*(1/2))) # 16/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(17/32))) # 17/32 max speed
PWM_RIGHT.duty_u16(int(65025*(17/32))) # 17/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(18/32))) # 18/32 max speed
PWM_RIGHT.duty_u16(int(65025*(18/32))) # 18/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(19/32))) # 19/32 max speed
PWM_RIGHT.duty_u16(int(65025*(19/32))) # 19/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(20/32))) # 20/32 max speed
PWM_RIGHT.duty_u16(int(65025*(20/32))) # 20/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(21/32))) # 21/32 max speed
PWM_RIGHT.duty_u16(int(65025*(21/32))) # 21/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(22/32))) # 22/32 max speed
PWM_RIGHT.duty_u16(int(65025*(22/32))) # 22/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(23/32))) # 23/32 max speed
PWM_RIGHT.duty_u16(int(65025*(23/32))) # 23/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(24/32))) # 24/32 max speed
PWM_RIGHT.duty_u16(int(65025*(24/32))) # 24/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(25/32))) # 25/32 max speed
PWM_RIGHT.duty_u16(int(65025*(25/32))) # 25/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(26/32))) # 26/32 max speed
PWM_RIGHT.duty_u16(int(65025*(26/32))) # 26/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(27/32))) # 27/32 max speed
PWM_RIGHT.duty_u16(int(65025*(27/32))) # 27/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(28/32))) # 28/32 max speed
PWM_RIGHT.duty_u16(int(65025*(28/32))) # 28/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(29/32))) # 29/32 max speed
PWM_RIGHT.duty_u16(int(65025*(29/32))) # 29/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(30/32))) # 30/32 max speed
PWM_RIGHT.duty_u16(int(65025*(30/32))) # 30/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(31/32))) # 31/32 max speed
PWM_RIGHT.duty_u16(int(65025*(31/32))) # 31/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(32/32))) # max speed
PWM_RIGHT.duty_u16(int(65025*(32/32))) # max speed
sleep(0.125) #spin 1/32 sec

#slow down both motors to stop (forward)
PWM_LEFT.duty_u16(int(65025*(31/32))) # 1/32 max speed
PWM_RIGHT.duty_u16(int(65025*(31/32))) # 1/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(30/32))) # 2/32 max speed
PWM_RIGHT.duty_u16(int(65025*(30/32))) # 2/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(29/32))) # 3/32 max speed
PWM_RIGHT.duty_u16(int(65025*(29/32))) # 3/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(28/32))) # 4/32 max speed
PWM_RIGHT.duty_u16(int(65025*(28/32))) # 4/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(27/32))) # 5/32 max speed
PWM_RIGHT.duty_u16(int(65025*(27/32))) # 5/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(26/32))) # 6/32 max speed
PWM_RIGHT.duty_u16(int(65025*(26/32))) # 6/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(25/32))) # 7/32 max speed
PWM_RIGHT.duty_u16(int(65025*(25/32))) # 7/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(24/32))) # 8/32 max speed
PWM_RIGHT.duty_u16(int(65025*(24/32))) # 8/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(23/32))) #9/32 max speed
PWM_RIGHT.duty_u16(int(65025*(23/32))) # 9/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(22/32))) # 10/32 max speed
PWM_RIGHT.duty_u16(int(65025*(22/32))) # 10/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(21/32))) # 11/32 max speed
PWM_RIGHT.duty_u16(int(65025*(21/32))) # 11/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(20/32))) # 12/32 max speed
PWM_RIGHT.duty_u16(int(65025*(20/32))) # 12/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(19/32))) # 13/32 max speed
PWM_RIGHT.duty_u16(int(65025*(19/32))) # 13/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(18/32))) # 14/32 max speed
PWM_RIGHT.duty_u16(int(65025*(18/32))) # 14/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(17/32))) #15/32 max speed
PWM_RIGHT.duty_u16(int(65025*(17/32))) # 15/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(1/2))) # 16/32 max speed
PWM_RIGHT.duty_u16(int(65025*(1/2))) # 16/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(15/32))) # 17/32 max speed
PWM_RIGHT.duty_u16(int(65025*(15/32))) # 17/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(14/32))) # 18/32 max speed
PWM_RIGHT.duty_u16(int(65025*(14/32))) # 18/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(13/32))) # 19/32 max speed
PWM_RIGHT.duty_u16(int(65025*(13/32))) # 19/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(12/32))) # 20/32 max speed
PWM_RIGHT.duty_u16(int(65025*(12/32))) # 20/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(11/32))) # 21/32 max speed
PWM_RIGHT.duty_u16(int(65025*(11/32))) # 21/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(10/32))) # 22/32 max speed
PWM_RIGHT.duty_u16(int(65025*(10/32))) # 22/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(9/32))) # 23/32 max speed
PWM_RIGHT.duty_u16(int(65025*(9/32))) # 23/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(8/32))) # 24/32 max speed
PWM_RIGHT.duty_u16(int(65025*(8/32))) # 24/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(7/32))) # 25/32 max speed
PWM_RIGHT.duty_u16(int(65025*(7/32))) # 25/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(6/32))) # 26/32 max speed
PWM_RIGHT.duty_u16(int(65025*(6/32))) # 26/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(5/32))) # 27/32 max speed
PWM_RIGHT.duty_u16(int(65025*(5/32))) # 27/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(4/32))) # 28/32 max speed
PWM_RIGHT.duty_u16(int(65025*(4/32))) # 28/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(3/32))) # 29/32 max speed
PWM_RIGHT.duty_u16(int(65025*(3/32))) # 29/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(2/32))) # 30/32 max speed
PWM_RIGHT.duty_u16(int(65025*(2/32))) # 30/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(1/32))) # 31/32 max speed
PWM_RIGHT.duty_u16(int(65025*(1/32))) # 31/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(0)) 
PWM_RIGHT.duty_u16(int(0)) 
sleep(0.125) #spin 1/32 sec
INA_LEFT.off()
INA_RIGHT.off()
INB_LEFT.off()
INB_RIGHT.off()


#Ramp up both motors to full speed (backward)
INB_LEFT.on()
INB_RIGHT.on()
PWM_LEFT.duty_u16(int(65025/32)) # 1/32 max speed
PWM_RIGHT.duty_u16(int(65025/32)) # 1/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025/16)) # 2/32 max speed
PWM_RIGHT.duty_u16(int(65025/16)) # 2/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(3/32))) # 3/32 max speed
PWM_RIGHT.duty_u16(int(65025*(3/32))) # 3/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(4/32))) # 4/32 max speed
PWM_RIGHT.duty_u16(int(65025*(4/32))) # 4/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(5/32))) # 5/32 max speed
PWM_RIGHT.duty_u16(int(65025*(5/32))) # 5/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(6/32))) # 6/32 max speed
PWM_RIGHT.duty_u16(int(65025*(6/32))) # 6/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(7/32))) # 7/32 max speed
PWM_RIGHT.duty_u16(int(65025*(7/32))) # 7/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(8/32))) # 8/32 max speed
PWM_RIGHT.duty_u16(int(65025*(8/32))) # 8/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(9/32))) #9/32 max speed
PWM_RIGHT.duty_u16(int(65025*(9/32))) # 9/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(10/32))) # 10/32 max speed
PWM_RIGHT.duty_u16(int(65025*(10/32))) # 10/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(11/32))) # 11/32 max speed
PWM_RIGHT.duty_u16(int(65025*(11/32))) # 11/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(12/32))) # 12/32 max speed
PWM_RIGHT.duty_u16(int(65025*(12/32))) # 12/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(13/32))) # 13/32 max speed
PWM_RIGHT.duty_u16(int(65025*(13/32))) # 13/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(14/32))) # 14/32 max speed
PWM_RIGHT.duty_u16(int(65025*(14/32))) # 14/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(15/32))) #15/32 max speed
PWM_RIGHT.duty_u16(int(65025*(15/32))) # 15/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(1/2))) # 16/32 max speed
PWM_RIGHT.duty_u16(int(65025*(1/2))) # 16/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(17/32))) # 17/32 max speed
PWM_RIGHT.duty_u16(int(65025*(17/32))) # 17/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(18/32))) # 18/32 max speed
PWM_RIGHT.duty_u16(int(65025*(18/32))) # 18/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(19/32))) # 19/32 max speed
PWM_RIGHT.duty_u16(int(65025*(19/32))) # 19/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(20/32))) # 20/32 max speed
PWM_RIGHT.duty_u16(int(65025*(20/32))) # 20/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(21/32))) # 21/32 max speed
PWM_RIGHT.duty_u16(int(65025*(21/32))) # 21/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(22/32))) # 22/32 max speed
PWM_RIGHT.duty_u16(int(65025*(22/32))) # 22/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(23/32))) # 23/32 max speed
PWM_RIGHT.duty_u16(int(65025*(23/32))) # 23/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(24/32))) # 24/32 max speed
PWM_RIGHT.duty_u16(int(65025*(24/32))) # 24/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(25/32))) # 25/32 max speed
PWM_RIGHT.duty_u16(int(65025*(25/32))) # 25/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(26/32))) # 26/32 max speed
PWM_RIGHT.duty_u16(int(65025*(26/32))) # 26/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(27/32))) # 27/32 max speed
PWM_RIGHT.duty_u16(int(65025*(27/32))) # 27/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(28/32))) # 28/32 max speed
PWM_RIGHT.duty_u16(int(65025*(28/32))) # 28/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(29/32))) # 29/32 max speed
PWM_RIGHT.duty_u16(int(65025*(29/32))) # 29/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(30/32))) # 30/32 max speed
PWM_RIGHT.duty_u16(int(65025*(30/32))) # 30/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(31/32))) # 31/32 max speed
PWM_RIGHT.duty_u16(int(65025*(31/32))) # 31/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(32/32))) # max speed
PWM_RIGHT.duty_u16(int(65025*(32/32))) # max speed
sleep(0.125) #spin 1/32 sec

#slow down both motors to stop (backward)
PWM_LEFT.duty_u16(int(65025*(31/32))) # 1/32 max speed
PWM_RIGHT.duty_u16(int(65025*(31/32))) # 1/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(30/32))) # 2/32 max speed
PWM_RIGHT.duty_u16(int(65025*(30/32))) # 2/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(29/32))) # 3/32 max speed
PWM_RIGHT.duty_u16(int(65025*(29/32))) # 3/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(28/32))) # 4/32 max speed
PWM_RIGHT.duty_u16(int(65025*(28/32))) # 4/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(27/32))) # 5/32 max speed
PWM_RIGHT.duty_u16(int(65025*(27/32))) # 5/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(26/32))) # 6/32 max speed
PWM_RIGHT.duty_u16(int(65025*(26/32))) # 6/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(25/32))) # 7/32 max speed
PWM_RIGHT.duty_u16(int(65025*(25/32))) # 7/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(24/32))) # 8/32 max speed
PWM_RIGHT.duty_u16(int(65025*(24/32))) # 8/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(23/32))) #9/32 max speed
PWM_RIGHT.duty_u16(int(65025*(23/32))) # 9/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(22/32))) # 10/32 max speed
PWM_RIGHT.duty_u16(int(65025*(22/32))) # 10/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(21/32))) # 11/32 max speed
PWM_RIGHT.duty_u16(int(65025*(21/32))) # 11/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(20/32))) # 12/32 max speed
PWM_RIGHT.duty_u16(int(65025*(20/32))) # 12/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(19/32))) # 13/32 max speed
PWM_RIGHT.duty_u16(int(65025*(19/32))) # 13/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(18/32))) # 14/32 max speed
PWM_RIGHT.duty_u16(int(65025*(18/32))) # 14/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(17/32))) #15/32 max speed
PWM_RIGHT.duty_u16(int(65025*(17/32))) # 15/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(1/2))) # 16/32 max speed
PWM_RIGHT.duty_u16(int(65025*(1/2))) # 16/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(15/32))) # 17/32 max speed
PWM_RIGHT.duty_u16(int(65025*(15/32))) # 17/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(14/32))) # 18/32 max speed
PWM_RIGHT.duty_u16(int(65025*(14/32))) # 18/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(13/32))) # 19/32 max speed
PWM_RIGHT.duty_u16(int(65025*(13/32))) # 19/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(12/32))) # 20/32 max speed
PWM_RIGHT.duty_u16(int(65025*(12/32))) # 20/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(11/32))) # 21/32 max speed
PWM_RIGHT.duty_u16(int(65025*(11/32))) # 21/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(10/32))) # 22/32 max speed
PWM_RIGHT.duty_u16(int(65025*(10/32))) # 22/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(9/32))) # 23/32 max speed
PWM_RIGHT.duty_u16(int(65025*(9/32))) # 23/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(8/32))) # 24/32 max speed
PWM_RIGHT.duty_u16(int(65025*(8/32))) # 24/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(7/32))) # 25/32 max speed
PWM_RIGHT.duty_u16(int(65025*(7/32))) # 25/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(6/32))) # 26/32 max speed
PWM_RIGHT.duty_u16(int(65025*(6/32))) # 26/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(5/32))) # 27/32 max speed
PWM_RIGHT.duty_u16(int(65025*(5/32))) # 27/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(4/32))) # 28/32 max speed
PWM_RIGHT.duty_u16(int(65025*(4/32))) # 28/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(3/32))) # 29/32 max speed
PWM_RIGHT.duty_u16(int(65025*(3/32))) # 29/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(2/32))) # 30/32 max speed
PWM_RIGHT.duty_u16(int(65025*(2/32))) # 30/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(65025*(1/32))) # 31/32 max speed
PWM_RIGHT.duty_u16(int(65025*(1/32))) # 31/32 max speed
sleep(0.125) #spin 1/32 sec
PWM_LEFT.duty_u16(int(0)) # 31/32 max speed
PWM_RIGHT.duty_u16(int(0)) # 31/32 max speed
sleep(0.125) #spin 1/32 sec


INA_LEFT.off()
INA_RIGHT.off()
INB_LEFT.off()
INB_RIGHT.off()