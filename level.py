import pygame as pg
from player import Player
from pipe import Pipe
from random import randint
from ground import Ground

class Level:
    def __init__(self, display_surface):
        self.display_surface = display_surface

        self.player = pg.sprite.GroupSingle()
        self.player.add(Player())

        self.pipes = pg.sprite.Group()
        self.pipes_event = pg.USEREVENT + 1
        self.pipes_time = 2000
        pg.time.set_timer(self.pipes_event, self.pipes_time)

        self.background_image = pg.image.load('img/bg.png').convert_alpha()
        self.ground = pg.sprite.Group()
        self.ground.add(Ground(0))


    def draw(self):
        self.display_surface.blit(self.background_image, (0,0))
        self.player.draw(self.display_surface)
        self.pipes.draw(self.display_surface)
        self.ground.draw(self.display_surface)


    def update_level_events(self, event):
        self.player.sprite.update_events(event)

        if event.type == self.pipes_event:
            y = randint(200, 400)
            top_pipe = Pipe(y, True)
            bottom_pipe = Pipe(y)
            self.pipes.add(top_pipe)
            self.pipes.add(bottom_pipe)


    def update_level(self):
        self.player.update()
        self.pipes.update()
        self.ground.update()
        self.ground_operator()


    def ground_operator(self):
        if len(self.ground) < 2:
            last_ground_x = list(self.ground)[-1].rect.x
            self.ground.add(Ground(last_ground_x + 900))

