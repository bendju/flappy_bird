import pygame as pg

class Ground(pg.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.speed = 2
        self.image = pg.image.load('img/ground.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(x,750))


    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()