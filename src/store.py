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
    char_btn_image, char_btn_rect = load_image('character.png', 150, 80,-1)
    r_char_btn_image, r_char_btn_rect = load_image(*resize('character.png', 150, 80,-1))
    skin_btn_image, skin_btn_rect = load_image('skin.png', 150, 80,-1)
    r_skin_btn_image, r_skin_btn_rect = load_image(*resize('skin.png', 150, 80,-1))
    item_btn_image, item_btn_rect = load_image('item_btn.png', 150, 80,-1)
    r_item_btn_image, r_item_btn_rect = load_image(*resize('item_btn.png', 150, 80,-1))

    while not game_start:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE and not full_screen:
                back_store_rect.bottomleft = (width * 0, height)
            if event.type == pygame.VIDEORESIZE:
                check_scr_size(event.w, event.h)
            if event.type == pygame.QUIT:
                game_start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if pygame.mouse.get_pressed() == (1, 0, 0):
            #         x, y = event.pos
            #         if r_char_btn_rect.collidepoint(x, y):
            #             #gameplay_easy()
            #         if r_skin_btn_rect.collidepoint(x, y):
            #             #gameplay_hard()
            #         if r_item_btn_rect.collidepoint(x, y):
            #             #store()

        r_char_btn_rect.centerx = resized_screen.get_width() * 0.2
        r_char_btn_rect.centery = resized_screen.get_height() * 0.5
        r_skin_btn_rect.centerx = resized_screen.get_width() * (0.2 + width_offset)
        r_skin_btn_rect.centery = resized_screen.get_height() * 0.5
        r_item_btn_rect.centerx = resized_screen.get_width() * (0.2 + 2 * width_offset)
        r_item_btn_rect.centery = resized_screen.get_height() * 0.5
        screen.blit(back_store, back_store_rect)
        disp_store_buttons(char_btn_image, skin_btn_image, item_btn_image)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
