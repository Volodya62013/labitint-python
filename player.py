from pygame import *
from gamesprite import Tubik
from const import *

class Player(Tubik):
    def __init__(self, x, y, img, sizeX, sizeY, step):
        super().__init__(x, y, img, sizeX, sizeY)
        self.step = step
    
    def update(self, up, down, left, right):
        keys = key.get_pressed()
        if keys[up] and self.rect.y >= 0:
            self.rect.y -= self.step

        if keys[down] and self.rect.y <= WIN_H - self.rect.height:
            self.rect.y += self.step

        if keys[left] and self.rect.x >= 0:
            self.rect.x -= self.step
        
        if keys[right] and self.rect.x <= WIN_W - self.rect.width:
            self.rect.x += self.step