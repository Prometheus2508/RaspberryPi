# Vehicle Monitor Software, V. 0.1
# Author: Jeff Layton
# Contact: Laytonjeffm@gmail.com
#
from picamera import PiCamera
from time import sleep
import datetime
import string
from gpiozero import Button, MotionSensor, PWMOutputDevice
#
disable = False
#
camera = PiCamera()
camera.resolution = (2560,1920)
camera.iso = 1000
camera.awb_mode = 'auto'
camera.brightness = 55
#
pir = MotionSensor(4)
#
button = Button(16,pull_up=True,bounce_time=None,hold_time=1,hold_repeat=False)
#
def buzz(duration):
    buzzer = PWMOutputDevice(22,initial_value=0.6,frequency=1000)
    sleep(duration)
    buzzer.off()
#
def capture():
    print('taking picture...')
    #"warm up"
    camera.start_preview()
    sleep(2)
#
    now = datetime.datetime.now()
    day = str(now)[:10]
    time = str(now)[11:19]
    camera.annotate_text = str(now)
    camera.capture('/home/pi/Desktop/capture_%s_%s.jpg' % (day, time))
#
    sleep(5)
    #Shut down
    camera.stop_preview()
#
print('Initialized')
buzz(0.25)
#
while True:
    pir.wait_for_motion()
    print('Motion Detected')

    #Test for car running
    
    #audible warning
    ###Warning here###
    buzz(0.25)
    sleep(0.25)
    buzz(0.25)
    
    #wait for override
    button.wait_for_press(4.0)
    if button.is_pressed:
        buzz(0.5)
        print('Override detected')
        exit()
    else:
        capture()
