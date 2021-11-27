import random
from src.setting import pygame
from src.setting import load_sprite_sheet
from src.setting import width, height
from src.setting import screen
from src.game_value import *


class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images, self.rect = load_sprite_sheet('cacti-small.png', 3, 1, sizex, sizey, -1)
        self.rect.bottom = int(0.98*height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0,3)]
        self.movement = [-1*speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

class Stone(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images, self.rect = load_sprite_sheet('stone.png', 1, 1, sizex, sizey, -1)
        self.rect.top = height *0.9
        self.rect.bottom = int(0.98*height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1*speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

class FireCactus(
    pygame.sprite.Sprite):  # class fire_Cactus(pygame.sprite.Sprite) => class FireCactus(pygame.sprite.Sprite)
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('fire_cacti6.png',
                                                   3, 1, sizex, sizey, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0, 3)]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

# Spring 스킨의 장애물 (3개)
class PinkTree(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('spring1.png',
                                                   2, 1, 60, 60, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0, 2)]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()


class CutTree(
    pygame.sprite.Sprite):  # class fire_Cactus(pygame.sprite.Sprite) => class FireCactus(pygame.sprite.Sprite)
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('spring2.png',
                                                   1, 1, 60, 60, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


class FruitTree(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('spring3.png', 1, 1, 60, 60, -1)
        self.rect.top = height * 0.9
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


# fall 스킨의 장애물
class Pumpkin(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('fall1.png',
                                                   1, 1, 40, 40, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()


class FallTree(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('fall2.png',
                                                   2, 1, 60, 60, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


class FallBush(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('fall3.png', 1, 1, 40, 40, -1)
        self.rect.top = height * 0.9
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


# winter 스킨의 장애물
class Snowman(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('winter1.png',
                                                   1, 1, 70, 70, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()


class WinterBush(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('winter2.png',
                                                   1, 1, 60, 60, -1)
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


class WinterTree(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('winter3.png', 1, 1, 60, 60, -1)
        self.rect.top = height * 0.9
        self.rect.bottom = int(DEFAULT_HEIGHT * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


# pteraking 클래스
class PteraKing(pygame.sprite.Sprite):
    def __init__(self, speed=0, sizex=-1, sizey=-1, life=5):
        print("Boss 등장")
        pygame.sprite.Sprite.__init__(self)
        self.images, self.rect = load_sprite_sheet('pteraking.png',
                                                   2, 1, sizex, sizey, -1)
        # self.ptera_height = [height*0.82, height*0.75, height*0.60]
        self.ptera_height = height * 0.3
        # self.rect.centery = self.ptera_height[random.randrange(0, 3)]
        self.rect.centery = self.ptera_height
        self.rect.left = width - self.rect.width - 50
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        # 
        self.down_speed = SPEED_UP_DOWN
        self.down_movement = [0, self.down_speed]
        self.up_speed = SPEED_UP_DOWN
        self.up_movement = [0, -self.up_speed]

        self.stop_movement = [0, 0]
        # 
        self.index = 0
        self.counter = 1
        # 새로운 정의.
        self.is_alive = True  # self.isAlive => self.is_alive
        self.pattern_idx = 0
        self.go_left = True  # self.goleft => self.go_left
        self.reached_leftmost = False
        self.reached_rightmost = False
        self.pattern0_time = 200
        self.pattern0_counter = 0

        self.pattern1_time = 200
        self.pattern1_counter = 0
        self.pattern1_speed = 15
        self.pattern1_lastmove = False

        self.pattern2_counter = 0
        self.go_down = True  # self.godown => self.go_down
        self.bottommost = height * 0.6
        self.topmost = height * 0.3
        # 보스가 내려가서 머무르는 시간
        self.pattern2_bottommost_time = 200

        self.stop = False

        self.go_up = False  # self.goup => self.go_up
        self.topmost = height * 0.3
        # 
        self.life = life

    def draw(self):
        screen.blit(self.image, self.rect)
        # 총알 그리기

    def decrease_life(self):
        self.life -= 1

    def pattern0(self):
        self.pattern1_lastmove = False
        self.pattern0_counter += 1
        self.movement[0] = 0

        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2

        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)

        if self.pattern0_counter % self.pattern0_time == 0:
            self.pattern_idx = 1

    def pattern1(self):
        self.pattern1_counter += 1

        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]

        if (self.go_left == True) and (self.reached_leftmost == False):  # self.goleft => self.go_left
            self.movement[0] = -1 * self.pattern1_speed
            self.rect = self.rect.move(self.movement)

            if self.rect.left < 0:
                self.go_left = False  # self.goleft => self.go_left
                self.reached_leftmost = True
                self.reached_rightmost = False

        else:
            self.movement[0] = self.pattern1_speed
            self.rect = self.rect.move(self.movement)

            if self.pattern1_lastmove:
                if self.rect.left > width - self.rect.width - 50:
                    self.go_left = True  # self.goleft => self.go_left
                    self.reached_rightmost = True
                    self.reached_leftmost = False

                    self.pattern_idx = 2
            else:
                if self.rect.left > width - self.rect.width - 50:
                    self.go_left = True  # self.goleft => self.go_left
                    self.reached_rightmost = True
                    self.reached_leftmost = False

            if self.pattern1_counter % self.pattern1_time == 0:
                self.pattern1_lastmove = True

        # 총알발사.

    def pattern2(self):

        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]

        if self.go_down:  # self.godown => self.go_down
            self.rect = self.rect.move(self.down_movement)

            if self.rect.centery > self.bottommost:
                self.go_down = False  # self.godown => self.go_down
                self.go_up = False  # self.goup => self.go_up
                self.stop = True

        if self.stop:
            self.pattern2_counter += 1
            self.rect = self.rect.move(self.stop_movement)

            if self.pattern2_counter % self.pattern2_bottommost_time == 0:
                self.go_down = False  # self.godown => self.go_down
                self.go_up = True  # self.goup => self.go_up
                self.stop = False

        if self.go_up:  # self.goup => self.go_up
            self.rect = self.rect.move(self.up_movement)

            if self.rect.centery < self.topmost:
                self.go_down = True  # self.godown => self.go_down
                self.go_up = False  # self.goup => self.go_up
                self.stop = False
                self.pattern_idx = 0

    def update(self):
        self.counter = self.counter + 1

        # 패턴0
        if self.pattern_idx == 0:
            # self.pattern0_counter=0
            self.pattern0()

        # 패턴1 
        elif self.pattern_idx == 1:
            # self.pattern1_counter = 0
            self.pattern1()

        # 패턴2
        else:
            # self.pattern2_counter = 0 
            self.pattern2()

class Ptera(pygame.sprite.Sprite):

    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('ptera.png', 2, 1, sizex, sizey, -1)
        self.ptera_height = [height*0.82, height*0.75, height*0.60]
        self.rect.centery = self.ptera_height[random.randrange(0, 3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1*speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index+1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)
        if self.rect.right < 0:
            self.kill()
#

class PvP:
    def __init__(self, speed=4, moving=''):
        self.moving = moving
        self.speed = speed

    def get_movement(self):
        if self.moving == "left":
            self.rect.left = width * 0.5
            self.movement = [-1 * self.speed, 0]
        elif self.moving == "right":
            self.rect.right = width * 0.5
            self.movement = [self.speed, 0]
        else:
            self.rect.left = width + self.rect.width
            self.movement = [-1 * self.speed, 0]

    def update(self):
        if self.rect.right < 0 or self.rect.left > width:
            self.kill()


class Cactus_pvp(PvP, pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1, moving=''):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(speed, moving)
        self.images, self.rect = load_sprite_sheet('cacti-small.png',
                                                   3, 1, sizex, sizey, -1)
        self.rect.bottom = int(0.98 * height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0, 3)]
        super().get_movement()

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        super().update()

# class Stone_pvp(PvP, pygame.sprite.Sprite):
#     def __init__(self, speed=5, sizex=-1, sizey=-1, moving=''):
#         pygame.sprite.Sprite.__init__(self, self.containers)
#         super().__init__(speed, moving)
#         self.images, self.rect = load_sprite_sheet('stone.png', 1, 1, sizex, sizey, -1)
#         self.rect.top = height * 0.9
#         self.rect.bottom = int(0.98 * height)
#         self.rect.left = width + self.rect.width

#         self.image = self.images[0]
#         super().get_movement()

#     def draw(self):
#         screen.blit(self.image, self.rect)

#     def update(self):
#         self.rect = self.rect.move(self.movement)

#         super().update()

class Ptera_pvp(PvP, pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1, moving=''):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(speed, moving)
        self.images, self.rect = load_sprite_sheet('ptera.png', 2, 1, sizex, sizey, -1)
        self.ptera_height = [height * 0.82, height * 0.75, height * 0.60]
        self.rect.centery = self.ptera_height[random.randrange(0, 3)]
        self.image = self.images[0]
        super().get_movement()
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        if self.moving == "right":
            self.image = pygame.transform.flip(self.images[self.index], True, False)
        else:
            self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)

        super().update()
