from pygame import *

class Tubik(sprite.Sprite):
    def __init__(self, x, y, img, sizeX, sizeY):
        super().__init__()
        self.image = transform.scale(image.load(img), (sizeX, sizeY))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

