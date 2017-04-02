import time 
import Adafruit_PCA9685 
def setup():
    global pwm
    global servo_straight  # Min pulse length out of 4096
    global servo_left
    global servo_right   # Max pulse length out of 4096
    pwm=Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(60)
    servo_straight =450
    servo_left= 400
    servo_right = 500
    global angle
def Map(x,in_min,in_max,out_min,out_max):
    return (x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

def left():
    global servo_left
    pwm.set_pwm(0,0,servo_left)

def right():
    global servo_right
    pwm.set_pwm(0,0,servo_right)

def turn(angle):
    tick=Map(angle,0,300,servo_left,servo_right)
    print tick    
    pwm.set_pwm(0,0,tick)
    

def home():
    global servo_straight
    pwm.set_pwm(0,0,servo_straight)

def test():
    while (1):
        #left()
        #time.sleep(1)
        #home()
        #time.sleep(1)
        #right()
        #time.sleep(1)
        
        angle=input("Enter the angle you want")
        turn(angle)
        time.sleep(1)
        
if __name__=='__main__':
    setup()
    home()
    test()

        
