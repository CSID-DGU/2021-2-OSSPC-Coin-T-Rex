from pygame.image import load
from src.item import *
from src.interface import *
from db.db_interface import InterfDB
db = InterfDB("db/score.db")


def store():
    global resized_screen
    game_start = False

    #배경 이미지
    back_store, back_store_rect = load_image('coin_t_rex3.png', width, height)
    #버튼 이미지

    while not game_start:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE and not full_screen:
                back_store_rect.bottomleft = (width * 0, height)
            if event.type == pygame.VIDEORESIZE:
                check_scr_size(event.w, event.h)
            if event.type == pygame.QUIT:
                game_start = True
        screen.blit(back_store, back_store_rect)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
