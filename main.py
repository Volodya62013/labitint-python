# -- coding: utf-8 --

import time as sigma
from random import randint

from pygame import *
from const import *
from gamesprite import Tubik
from player import Player
from enemy import Enemy
from wall import Wall

window = display.set_mode((WIN_W, WIN_H))

clock = time.Clock()

display.set_caption("Labirint")

font.init()

myfont, score = font.SysFont('Papyrus', 70), 0

gameres = ''

fon = Tubik(0, 0, 'src/fon.jpg', WIN_W, WIN_H)

tanos = Player(20, 400, "src/player.jpg", 70, 50, 1)
tanos2 = Player(610, 20, "src/player.jpg", 70, 50, 1)

sigmaDeD = Enemy(315, 225, "src/sigmatanos.jpg", 70, 50, 1, 1)

hito = Tubik(0, 150, 'src/hito.jpg', 70, 70)

wall1 = Wall(150, 0, 50, 450)
wall2 = Wall(550, 0, 50, 450)

walls = [wall1, wall2]
players = sprite.Group()
players.add(tanos)
players.add(tanos2)

# игровой цикл
finish = False
game = True
while game:
    if not finish:
        # отобразить картинку фона
        fon.draw(window)

        for wall in walls:
            wall.draw(window)
            wall.outline(window)

        scoretxt = myfont.render(str(score), True, (204, 0, 204))
        gamerestxt = myfont.render(str(gameres), True, (204, 0, 204))
        window.blit(scoretxt, (150, 50))
        window.blit(gamerestxt, (150, 100))
        hito.draw(window)

        sigmaDeD.draw(window)
        for p in players:
            p.draw(window)

        tanos.update(K_w, K_s, K_a, K_d)
        tanos2.update(K_UP, K_DOWN, K_LEFT, K_RIGHT)
        sigmaDeD.updateY(0, 470)

            
        if sprite.collide_rect(tanos, sigmaDeD):
            tanos.rect.x = 20
            tanos.rect.y = 400
            sigma.sleep(0.5)
            score -= 1

        if sprite.collide_rect(tanos2, sigmaDeD):
            tanos2.rect.x = 610
            tanos2.rect.y = 20
            sigma.sleep(0.5)
            score -= 1


        if sprite.spritecollide(hito, players, False):
            hito.rect.x = 1000
            hito.rect.y = 1000
            sigma.sleep(0.5)
            hito.rect.x = randint(0, 630)
            hito.rect.y = randint(0, 430)
            score += 1

        if sprite.collide_rect(hito, sigmaDeD):
            hito.rect.x = 1000
            hito.rect.y = 1000
            sigma.sleep(0.5)
            hito.rect.x = randint(0, 630)
            hito.rect.y = randint(0, 430)
            score -= 1

        if sprite.groupcollide(walls, players, False, False):
            for w in walls:
                if sprite.collide_rect(tanos, w):
                    tanos.rect.x = 20
                    tanos.rect.y = 400
                if sprite.collide_rect(tanos2, w):
                    tanos2.rect.x = 610
                    tanos2.rect.y = 20

        if score >= 20:
            gameres = 'Win!'
            finish = True


        if score == -1:
            gameres = 'Lose!'
            finish = True
            display.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    gamerestxt = myfont.render(str(gameres), True, (204, 0, 204))
    window.blit(gamerestxt, (150, 100))
    
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick()


display.update()
