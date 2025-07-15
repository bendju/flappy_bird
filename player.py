import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_counter = 0
        self.timer = 0
        self.images = [
            pg.image.load('img/bird1.png').convert_alpha(),
            pg.image.load('img/bird2.png').convert_alpha(),
            pg.image.load('img/bird3.png').convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(200, 350))
        self.jump_speed = 9
        self.jump_frames = 0
        self.fall_speed = 0
        self.image_rotation = 0


    def update_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.fall_speed = 0
                self.image_rotation = 25
                self.jump_frames = 7



    def apply_gravity(self):

        if self.jump_frames > 0:
            self.rect.y -= self.jump_speed
            self.jump_frames -= 1
        else:
            self.fall_speed += 0.15 if self.fall_speed < 10 else 0
            self.rect.y += self.fall_speed



    def animation_delay(self):
        self.timer += 1
        if self.timer % 7 == 0:
            self.img_counter += 1
            if self.img_counter >= len(self.images):
                self.img_counter = 0
        self.image = self.images[self.img_counter]

        self.image_rotation -= 2 if self.image_rotation > -60 else 0

        rotated_image = pg.transform.rotate(self.image, self.image_rotation)
        self.image = rotated_image
        self.rect = rotated_image.get_rect(center=self.rect.center)


    def update(self):
        self.apply_gravity()
        self.animation_delay()

