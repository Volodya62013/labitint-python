from pygame import * # Importing pygame library
from const import * # Importing constants

class Wall(sprite.Sprite):
    def __init__(self, x, y, sizeX, sizeY, color=PURPLE, stroke=BLACK):
        self.rect = Rect(x, y, sizeX, sizeY)
        self.stroke = stroke
        self.fillcolor = color
    
    def outline(self, window, size=10):
        draw.rect(window, self.stroke, self.rect, size)

    def draw(self, window):
        draw.rect(window, self.fillcolor, self.rect)