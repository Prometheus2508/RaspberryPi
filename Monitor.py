# Vehicle Monitor Software, V. 0.1
# Author: Jeff Layton
# Contact: Laytonjeffm@gmail.com
#
from picamera import PiCamera
from time import sleep
import datetime
import string
from gpiozero import Button, MotionSensor
#
camera = PiCamera()
camera.resolution = (2560,1920)
camera.iso = 1000
camera.awb_mode = 'auto'
camera.brightness = 55
#
pir = MotionSensor(4)
#
while 1:
    pir.wait_for_motion()
    
    #audible warning
    #wait for override
    #second warning

    #"warm up"
    print('taking picture...')
    camera.start_preview()
    sleep(2)
    #
    now = datetime.datetime.now()
    day = str(now)[:10]
    time = str(now)[11:19]
    camera.annotate_text = str(now)
    camera.capture('/home/pi/Desktop/capture_%s_%s.jpg' % (day, time))

    sleep(5)
    #Shut down
    camera.stop_preview()
#exit()
