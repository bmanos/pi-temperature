import RPi.GPIO as GPIO 
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

while True:
    try:
        myTempFile = open("/sys/class/thermal/thermal_zone0/temp")
        temp = float(myTempFile.read())
        tempC = temp/1000
        if tempC >= 45:
            GPIO.output(12, GPIO.HIGH) # Turn on
            print("The temp is higher than 45c, fan is ON : %s" %tempC)
            time.sleep(60)
        else:
            GPIO.output(12, GPIO.LOW) # Turn off
            print("The temp is lower than 45c, fan is OFF : %s" %tempC)
            time.sleep(60)
    except:
        myTempFile.close()
        GPIO.cleanup()
        exit