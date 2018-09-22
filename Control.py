#Options: BG color, # pins,, reset
#Buttons: close, shutdown all

import os
import sys
import pygame
from gpiozero import OutputDevice
from pygame.locals import *

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
    return image, image.get_rect()

class switch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image, self.rect = load_image('text', -1)
    def set_pin(self,pin):
        self.pin = OutputDevice(pin)
        self.state = False
        self.pin.off()
    def toggle(self):
        if self.state:
            self.state = False
            self.pin.off()
        else:
            self.state = True
            self.pin.on()

def main():
    #Set number of switches
    switch_num = 8
    #Initialize available pins
    pins = [14,15,17,18,22,23,24,27]

    pygame.init()
    screen = pygame.display.set_mode((1280, 760))
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    SW1 = switch()
    SW1.set_pin(pins[1])

    RUN = True
    while RUN:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUN = False
            elif event.type == MOUSEBUTTONDOWN:
                RUN = False
    pygame.quit()

if __name__ == '__main__':
    main()
                
