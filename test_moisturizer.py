#import libraries
import time
import RPi.GPIO as GPIO

#GPIO setup -- pin 29 = moisture sensor; pin 7 = LED
#Sensor: GPIO 29, Relay 1: GPIO 37, Relay 2: GPIO 38, Relay 3: GPIO 40

relay3=40
relay2=38
relay1=37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)



#Set up variables: internal in minutes, water in seconds
interval = 3600*24*2
water = 30
pic_num = 1

def detect_moist():
    GPIO.output(relay2,False)
    time.sleep(water)
    if (GPIO.input(29))==1:
        print("dry")
    else:
        print("wet")
    GPIO.output(relay2,True)

def water_plants():
    GPIO.output(relay3,False)
    time.sleep(water)
    GPIO.output(relay3,True)

try:
    while True:
        detect_moist()
        time.sleep(interval)


finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
