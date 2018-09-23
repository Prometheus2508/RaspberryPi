#Options: BG color, # pins,, reset
#Buttons: close, shutdown all

import os
import sys
import pygame
from gpiozero import OutputDevice
from pygame.locals import *

pygame.init()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error(message):
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

class switch(pygame.sprite.Sprite):
    def __init__(self,pin,loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('/home/pi/Pictures/Switch_0.jpg', -1)
        self.rect = self.image.get_rect()
        self.off_image = self.image
        self.on_image = load_image('/home/pi/Pictures/Switch_1.jpg', -1)
        
        screen = pygame.display.get_surface()
        #self.area = screen.get_rect()
        print(str(loc))
        self.rect.topleft = loc
        self.set_pin(pin)
    def set_pin(self,pin):
        self.pin = OutputDevice(pin)
        self.state = False
        self.pin.off()
    def toggle(self):
        if self.state:
            self.state = False
            self.image = self.off_image
            #self.pin.off()
        else:
            self.state = True
            self.image = self.on_image
            #self.pin.on()

def main():
    #Interface size
    intf_size = (1280,340)
    #Set number of switches
    switch_num = 4
    #Initialize available pins
    pins = [14,15,17,18,22,23,24,27]
    #Hide mouse
    pygame.mouse.set_visible(0)
    #Background color
    backgr = 255, 255, 255

    #Initialize screen
    screen = pygame.display.set_mode(intf_size)

    #Build switches and switch library
    sw_dict = {}
    switch_group = pygame.sprite.Group()
    
    for n in range(switch_num):
        m = n+1
        sw_left = (10+100)*n+10
        sw_top = 10
        sw_dict["SW_" + str(m)] = switch(pins[m],(sw_left,sw_top))
        switch_group.add(sw_dict["SW_" + str(m)])

    #SW1 = switch()
    #switch_group = pygame.sprite.Group(sw_dict)
    
    RUN = True
    while RUN:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUN = False
            elif event.type == MOUSEBUTTONDOWN:
                m_pos = pygame.mouse.get_pos()
                for s in switch_group:
                    if s.rect.collidepoint(m_pos):
                        s.toggle()

        screen.fill(backgr)
        switch_group.update()
        switch_group.draw(screen)
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()
                
