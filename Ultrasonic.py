import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

try:
    trigPin=16
    echoPin=18
    GPIO.setup(trigPin,GPIO.OUT)
    GPIO.setup(echoPin,GPIO.IN)

    while True:
        GPIO.output(trigPin,GPIO.LOW)
        time.sleep(2E-6)           #micro sec
        GPIO.output(trigPin,GPIO.HIGH)
        time.sleep(10E-6)
        GPIO.output(trigPin,GPIO.LOW)
        while GPIO.input(echoPin)==0:
            echoStartTime=time.time()
        while GPIO.input(echoPin)==1:
            echoStopTime=time.time()
        ptt=echoStopTime-echoStartTime
        distance=767*5280*12/3600*ptt*0.5  
            #767 miles/hr sound speed, covert to inches, 
            #time 0.5 bc the the org distance measure from the start to object and back
        print(round(distance,1)," inches")
        time.sleep(0.2)             #sec
        
except KeyboardInterrupt:
    GPIO.cleanup()
