from pygame import *
from gamesprite import Tubik
from const import *

class Enemy(Tubik):
    def __init__(self, x, y, img, sizeX, sizeY, xstep, ystep):
        super().__init__(x, y, img, sizeX, sizeY)
        self.tostart = -1
        self.xstep = xstep
        self.ystep = ystep


    def updateX(self, xstart, xend):
        if self.rect.x < xstart or self.rect.x > xend:
            self.tostart *= -1
        self.rect.x += self.xstep * self.tostart

    def updateY(self, ystart, yend):
        if self.rect.y < ystart or self.rect.y > yend:
            self.tostart *= -1
        self.rect.y += self.ystep * self.tostart
