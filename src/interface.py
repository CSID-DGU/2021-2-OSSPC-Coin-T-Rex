from src.setting import *


class Ground:
    def __init__(self, speed=-5):
        self.image, self.rect = load_image('ground.png', -1, -1, -1)
        self.image1, self.rect1 = load_image('ground.png', -1, -1, -1)
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect1.left = self.rect.right
        self.speed = speed

    def draw(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.image1, self.rect1)

    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image, self.rect = load_image('cloud.png', int(90*30/42), 30, -1)
        self.speed = 1
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1*self.speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


class Heart:
    def __init__(self, sizex=-1, sizey=-1, x=-1, y=-1):
        self.images, self.rect = load_sprite_sheet("hpbar.png", 2, 1, sizex, sizey, -1)
        self.image = self.images[1]
        if x == -1:
            self.rect.left = width * 0.01
        else:
            self.rect.left = x

        if y == -1:
            self.rect.top = height * 0.01
        else:
            self.rect.top = y

    def draw(self):
        screen.blit(self.image, self.rect)


class HeartIndicator:
    def __init__(self, life, loc = -1):
        # self.heart_size = 40
        self.life = life
        self.life_set = []
        self.loc = loc

    def draw(self):
        for life in self.life_set:
            life.draw()

    def update(self, life):
        self.life = life
        if self.loc == -1:
        # self.life_set = [Heart(self.heart_size, self.heart_size, width * 0.01 + i * self.heart_size) for i in range(self.life)]
            self.life_set = [Heart(object_size[0], object_size[1], width * 0.01 + i * (object_size[0]-i)) for i in range(self.life)]
        else:
            self.life_set = [Heart(object_size[0], object_size[1], width * 0.76 + i * (object_size[0]-i)) for i in range(self.life)]
        


# class Scoreboards:
#     def __init__(self, x=-1, y=-1):
#         self.score = 0
#         self.tempimages, self.temprect = load_sprite_sheet('numbers.png', 12, 1, 15, int(15*6/5), -1)
#         self.image = pygame.Surface((80, int(15*6/5)))
#         self.rect = self.image.get_rect()
#         if x == -1:
#             self.rect.left = width*0.89
#         else:
#             self.rect.left = x
#         if y == -1:
#             self.rect.top = height*0.05
#         else:
#             self.rect.top = y
#
#     def draw(self):
#         screen.blit(self.image, self.rect)
#
#     def update(self, score):
#         score_digits = extract_digits(score)
#         self.image.fill(background_col)
#         for s in score_digits:
#             self.image.blit(self.tempimages[s], self.temprect)
#             self.temprect.left += self.temprect.width
#         self.temprect.left = 0

class Scoreboard:
    def __init__(self, x=-1, y=-1):
        self.score = 0
        self.pos_x = 0
        self.pos_y = 0
        self.my_font = pygame.font.Font('DungGeunMo.ttf', 30)
        if x == -1:
            self.pos_x = width * 0.89
        else:
            self.pos_x = x
        if y == -1:
            self.pos_y = height*0.05
        else:
            self.pos_y = y

    def draw(self):
        screen.blit(self.sc, self.sc_rect)

    def update(self, score):
        score_digits = extract_digits(score)
        #self.image.fill(background_col)
        self.sc = self.my_font.render(f'{score}'.zfill(5),True, black)
        self.sc_rect = self.sc.get_rect()
        self.sc_rect.left = self.pos_x
        self.sc_rect.top = self.pos_y


#이미지 배경
class ImgBack:
    def __init__(self, speed=-5, name='ground'):
        self.image, self.rect = load_image(f'{name}.png', width, height)
        self.image1, self.rect1 = load_image(f'{name}.png', width, height)
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect1.left = self.rect.right
        #화면 맞추기
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect.top = 0
        self.rect1.top = 0
        #image1 우측에 붙이기
        self.rect.left = 0
        self.rect1.left = self.rect.right
        self.speed = speed
    def draw(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.image1, self.rect1)
    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed
        if self.rect.right < width:
            self.rect1.left = self.rect.right
        if self.rect1.right < width:
            self.rect.left = self.rect1.right

