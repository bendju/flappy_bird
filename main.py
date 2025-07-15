import pygame as pg

from level import Level
from menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((400, 700))
        self.clock = pg.time.Clock()
        self.level = Level(self.screen)
        self.menu = Menu(self.screen)
        self.run()


    def run(self):
        running = True
        while running:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running = False

                self.menu.check_events(ev)

            self.screen.fill('black')
            self.menu.draw()

            self.menu.update()
            pg.display.update()
            self.clock.tick(60)

        pg.quit()

if __name__ == '__main__':
    Game()