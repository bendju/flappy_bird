import pygame as pg
from level import Level

class Menu:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.points = 0
        self.level = None
        self.font = pg.font.SysFont(None, 32)
        self.play_game_text = self.font.render('Nyomd meg a space-t a kezdéshez.', True, 'white')
        self.play_game_text_rect = self.play_game_text.get_rect(center=(200, 100))

        self.points_font = self.font.render(str(self.points), True, 'white')
        self.points_font_rect = self.points_font.get_rect(center=(200, 100))

        self.background_image = pg.image.load('img/bg.png').convert_alpha()

    def draw(self):
        if self.level:
            self.level.draw()
            self.display_surface.blit(self.points_font, self.points_font_rect)

        else:
            self.display_surface.blit(self.background_image, (0, 0))
            self.display_surface.blit(self.play_game_text, self.play_game_text_rect)


    def check_events(self, event):
        if self.level is None:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.level = Level(self.display_surface)
        else:
            self.level.update_level_events(event)

    def update(self):
        if self.level:
            self.level.update_level()

            for sprite in self.level.pipes:
                if sprite.rect.x < 200 and sprite.flipped:
                    sprite.flipped = False
                    self.points += 1
                    self.points_font = self.font.render(str(self.points), True, 'white')
                    self.points_font_rect = self.points_font.get_rect(center=(200, 100))

            if pg.sprite.groupcollide(self.level.player, self.level.pipes, False, False):
                self.level = None
                self.points = 0
                self.points_font = self.font.render(str(self.points), True, 'white')
                self.points_font_rect = self.points_font.get_rect(center=(200, 100))

            elif pg.sprite.groupcollide(self.level.player, self.level.ground, False, False):
                self.level = None
                self.points = 0
                self.points_font = self.font.render(str(self.points), True, 'white')
                self.points_font_rect = self.points_font.get_rect(center=(200, 100))

            elif self.level.player.sprite.rect.top < 0:
                self.level = None
                self.points = 0
                self.points_font = self.font.render(str(self.points), True, 'white')
                self.points_font_rect = self.points_font.get_rect(center=(200, 100))


