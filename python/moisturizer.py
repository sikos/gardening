#import libraries
import time
import RPi.GPIO as GPIO

#GPIO setup
#Sensor: GPIO 29
#Relay 1: GPIO 37, Relay 2: GPIO 38, Relay 3: GPIO 40

relay3=40
relay2=38
relay1=37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)

#Set up variables
interval = 3600*24*2
water = 2.5

def detect_moist():
    def result=False
    GPIO.output(relay2,False)
    time.sleep(water)
    if (GPIO.input(29))==1:
        print("dry")
        result=False
    else:
        print("wet")
        result=True 
    GPIO.output(relay2,True)
    return result

def water_plants():
    GPIO.output(relay3,False)
    time.sleep(water)
    GPIO.output(relay3,True)

try:
    while True:
        GPIO.output(relay1,True)
        GPIO.output(relay2,True)
        GPIO.output(relay3,True)
        water_plants()
        time.sleep(interval)

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
