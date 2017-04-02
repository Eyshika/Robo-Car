import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

motor0a=11
motor0b=12
motor1a=13
motor1b=15

en_m0=0
en_m1=1
global pwm
pins=[motor0a,motor0b,motor1a,motor1b]
pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def setSpeed(speed):
    speed *=40
    print 'speed is: ',speed
    pwm.set_pwm(en_m0,0,speed)
    pwm.set_pwm(en_m1,0,speed)

def setup(motion):
    global forward0,forward1,backward0,backward1
    forward0=motion
    forward1=motion
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    if forward0 == 1:
        backward0=2

    if forward0 == 2:

        backward0=1

    if forward1 ==1:
        backward1=2

    if forward1==2:
        backward1=1
    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)

def motor0(x):
    if x==1:
        GPIO.output(motor0a,GPIO.LOW)
        GPIO.output(motor0b,GPIO.HIGH)
    if x==2:
        GPIO.output(motor0a,GPIO.HIGH)
        GPIO.output(motor0b,GPIO.LOW)

def motor1(x):
    if x==1:
        GPIO.output(motor1a,GPIO.LOW)
        GPIO.output(motor1b,GPIO.HIGH)
    if x==2:
        GPIO.output(motor1a,GPIO.HIGH)
        GPIO.output(motor1b,GPIO.LOW)

def forward():
    motor0(forward0)
    motor1(forward1)

def backward():
    motor0(backward0)
    motor1(backward1)

def forwardwithspeed(spd=50):
    setSpeed(spd)
    motor0(forward0)
    motor1(forward1)
def backwardwithspeed(spd=50):
    setSpeed(spd)
    motor0(backward0)
    motor1(backward1)
        
def stop():
    for pin in pins:
        GPIO.output(pin,GPIO.LOW)
def test():
    while(1):
        motion=input("Enter the motion")
        setup(motion)
        setSpeed(10)
        forward()
        time.sleep(2)
        backward()
        #setSpeed(60)
        forward()
        time.sleep(2)
        backward()
        time.sleep(2)
        forwardwithspeed(spd=50)
        time.sleep(2)
        backwardwithspeed(spd=50)
        time.sleep(2)
        stop()
if __name__ == '__main__':
    test()
        
