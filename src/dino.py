import pygame
from pygame import mixer
from src.setting import check_point_sound
from src.setting import width, height, screen, gravity
from src.setting import load_sprite_sheet
from src.game_value import LIFE


class Dino:
    def __init__(self, sizex=-1, sizey=-1, type=None, loc=-1):
        self.type = type
        if type == 'ORIGINAL':
            self.images, self.rect = load_sprite_sheet('dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'RED':
            self.images, self.rect = load_sprite_sheet('red_dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('red_dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'YELLOW':
            self.images, self.rect = load_sprite_sheet('yellow_dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('yellow_dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'PURPLE':
            self.images, self.rect = load_sprite_sheet('purple_dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('purple_dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'TUX':
            self.images, self.rect = load_sprite_sheet('tux_walk.png',
                                                       6, 1, 60, 60, -1)
            self.images1, self.rect1 = load_sprite_sheet('tux_ducking.png',
                                                         2, 1, 60, 60, -1)
        else:
            self.images, self.rect = load_sprite_sheet('dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        if loc == -1:
            self.rect.bottom = int(0.98 * height)
            self.rect.left = width / 15
        else:
            self.rect.bottom = int(0.98 * height)
            self.rect.left = width * (13 / 15)
        self.image = self.images[0]
        self.type = type
        self.index = 0
        self.counter = 0
        self.score = 0
        self.is_jumping = False
        self.is_dead = False
        self.is_ducking = False
        self.is_blinking = False
        self.movement = [0, 0]
        self.jump_speed = 11.5
        self.super_jump_speed = self.jump_speed * 1.3
        self.collision_immune = False
        self.is_super = False
        self.stand_width = self.rect.width
        self.duck_width = self.rect1.width
        self.player1 = True
        self.life = LIFE

    def draw(self):
        screen.blit(self.image, self.rect)

    # 충돌판단
    def check_bounds(self):
        if self.rect.bottom > int(0.98 * height):
            self.rect.bottom = int(0.98 * height)
            self.is_jumping = False

    def update(self):
        if self.is_jumping:
            self.movement[1] = self.movement[1] + gravity
        ##
        if self.is_jumping:
            self.index = 0
        #
        elif self.is_blinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    # 눈깜빡
                    self.index = (self.index + 1) % 2
            else:  # 눈 깜빡
                if self.counter % 20 == 19:
                    self.index = (self.index + 1) % 2
        # is ducking이 True면
        elif self.is_ducking:
            if self.counter % 5 == 0:
                self.index = (self.index + 1) % 2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1) % 2 + 2
        if self.is_dead:
            self.index = 4
        if self.collision_immune:
            if self.counter % 10 == 0:
                self.index = 5
        #
        if not self.is_ducking:
            self.image = self.images[self.index]
            self.rect.width = self.stand_width
        else:
            self.image = self.images1[self.index % 2]
            if self.collision_immune is True:
                if self.counter % 5 == 0:
                    self.image = self.images[5]
            self.rect.width = self.duck_width
        self.rect = self.rect.move(self.movement)
        self.check_bounds()
        if not self.is_dead and self.counter % 7 == 6 and not self.is_blinking:
            self.score += 1
            if self.score % 100 == 0 and self.score != 0:
                if mixer.get_init() is not None:
                    check_point_sound.play()
        self.counter = (self.counter + 1)

    def increase_life(self):
        self.life += 1

    def decrease_life(self):
        self.life -= 1

    def is_life_zero(self):
        return True if self.life == 0 else False