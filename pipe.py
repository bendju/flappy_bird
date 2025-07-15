import pygame as pg

class Pipe(pg.sprite.Sprite):
    def __init__(self, y, flipped=False):
        super().__init__()
        self.image = pg.image.load('img/pipe.png').convert_alpha()
        self.padding = 100
        self.speed = 2
        self.flipped = flipped
        if flipped:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(bottomleft=(500, y - self.padding))
        else:
            self.rect = self.image.get_rect(topleft=(500, y + self.padding))


    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
