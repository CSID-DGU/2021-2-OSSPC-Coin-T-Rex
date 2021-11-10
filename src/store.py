from src.item import *
from src.interface import *
from db.db_interface import InterfDB
db = InterfDB("db/score.db")
import src.game

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
    back_btn_image, back_btn_rect = load_image('btn_back.png', 100, 50, -1)
    r_back_btn_image, r_back_btn_rect = load_image(*resize('btn_back.png', 100, 50, -1))

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if pygame.mouse.get_pressed() == (1, 0, 0):
                     x, y = event.pos
            #         if r_char_btn_rect.collidepoint(x, y):
            #             #gameplay_easy()
            #         if r_skin_btn_rect.collidepoint(x, y):
            #             #gameplay_hard()
                     if r_item_btn_rect.collidepoint(x, y):
                         item_store()
                     if r_back_btn_rect.collidepoint(x, y):
                         src.game.select_mode()

        r_char_btn_rect.centerx = resized_screen.get_width() * 0.2
        r_char_btn_rect.centery = resized_screen.get_height() * 0.5
        r_skin_btn_rect.centerx = resized_screen.get_width() * (0.2 + width_offset)
        r_skin_btn_rect.centery = resized_screen.get_height() * 0.5
        r_item_btn_rect.centerx = resized_screen.get_width() * (0.2 + 2 * width_offset)
        r_item_btn_rect.centery = resized_screen.get_height() * 0.5
        r_back_btn_rect.centerx = resized_screen.get_width() * 0.1
        r_back_btn_rect.centery = resized_screen.get_height() * 0.1
        screen.blit(back_store, back_store_rect)
        disp_store_buttons(char_btn_image, skin_btn_image, item_btn_image, back_btn_image)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

def item_store():
    global resized_screen
    image_space = 0.3
    game_start = False
    btn_offset = 0.25
    item_price_offset = 0.18
    item_btn_offset = 0.28
    # 배경 이미지
    back_store, back_store_rect = load_image('coin_t_rex3.png', width, height)
    # 코인 이미지
    coin1_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin1_image = transform.scale(coin1_image[0], (25, 25))
    coin1_rect = coin1_image.get_rect()
    coin2_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin2_image = transform.scale(coin2_image[0], (25, 25))
    coin2_rect = coin2_image.get_rect()
    coin3_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin3_image = transform.scale(coin3_image[0], (25, 25))
    coin3_rect = coin3_image.get_rect()
    # 아이템 이미지
    shield_image, _ = load_sprite_sheet('item.png', 2, 1, -1, -1, -1)
    life_image, life_rect= load_image('heart_bullet.png', 70, 70, -1)
    time_image, _ = load_sprite_sheet('slow_pic.png', 2, 1, -1, -1, -1)
    shield_image = transform.scale(shield_image[0], (80, 80))
    shield_rect = shield_image.get_rect()
    time_image = transform.scale(time_image[0], (80, 80))
    time_rect = time_image.get_rect()
    #user가 가지고 있는 아이템 노출을 위한 이미지
    user_shield_image, _ = load_sprite_sheet('item.png', 2, 1, -1, -1, -1)
    user_shield_image = transform.scale(user_shield_image[0], (20, 20))
    user_shield_rect = user_shield_image.get_rect()
    user_life_image, user_life_rect =load_image('heart_bullet.png', 20, 20, -1)
    user_time_image, _ = load_sprite_sheet('slow_pic.png', 2, 1, -1, -1, -1)
    user_time_image =transform.scale(user_time_image[0], (20,20))
    user_time_rect = user_time_image.get_rect()
    user_coin_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    user_coin_image = transform.scale(user_coin_image[0], (20,20))
    user_coin_rect = user_coin_image.get_rect()
    # item store 버튼 이미지
    buy_btn1_image, buy_btn1_rect = load_image('buy.png', 100, 50, -1)
    buy_btn2_image, buy_btn2_rect = load_image('buy.png', 100, 50, -1)
    buy_btn3_image, buy_btn3_rect = load_image('buy.png', 100, 50, -1)
    no_money1_image, no_money1_rect = load_image('X.png', 100, 50, -1)
    no_money2_image, no_money2_rect = load_image('X.png', 100, 50, -1)
    no_money3_image, no_money3_rect = load_image('X.png', 100, 50, -1)
    #뒤로 가기 버튼 이미지
    back_btn_image, back_btn_rect = load_image('btn_back.png', 100, 50, -1)
    r_back_btn_image, r_back_btn_rect = load_image(*resize('btn_back.png', 100, 50, -1))
    #아이템
    shield_item_count = db.query_db("select shield from item where item_id=1;", one=True)['shield']
    life_item_count = db.query_db("select life from item where item_id=1;", one=True)['life']
    slow_item_count = db.query_db("select slow from item where item_id=1;", one=True)['slow']
    coin_item_count = db.query_db("select coin from item where item_id=1;", one=True)['coin']
    # 폰트
    s_price, l_price, t_price = 1, 1, 1
    my_font = pygame.font.Font('DungGeunMo.ttf', 18)
    user_font = pygame.font.Font('DungGeunMo.ttf', 16)
    shield_price = my_font.render(f"x {s_price}", True, black)
    life_price = my_font.render(f'x {l_price}', True, black)
    time_price = my_font.render(f'x {t_price}', True, black)
    # info = my_font.render(f"[YOU HAVE]", True, black)
    user_shield = user_font.render(f'X{shield_item_count}', True, black)
    user_life = user_font.render(f'X{life_item_count}', True, black)
    user_time = user_font.render(f'X{slow_item_count}', True, black)
    user_coin = user_font.render(f'X{coin_item_count}', True, black)
    #배치
    (shield_rect.centerx, shield_rect.centery) = (width * 0.25, height * 0.37)
    (coin1_rect.centerx, coin1_rect.centery) = (width * 0.23, height * (0.37 + item_price_offset))
    shield_price_rect = shield_price.get_rect(center=(width * 0.28, height * (0.37 + item_price_offset)))
    (buy_btn1_rect.centerx, buy_btn1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    (no_money1_rect.centerx, no_money1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    #
    (life_rect.centerx, life_rect.centery) = (width * (0.25 + btn_offset) , height * 0.37)
    (coin2_rect.centerx, coin2_rect.centery) = (width * (0.23 + btn_offset), height * (0.37 + item_price_offset))
    life_price_rect = life_price.get_rect(center=(width * (0.28 + btn_offset), height * (0.37 + item_price_offset)))
    (buy_btn2_rect.centerx, buy_btn2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    (no_money2_rect.centerx, no_money2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    #
    (time_rect.centerx, time_rect.centery) = (width * (0.25 + 2 * btn_offset), height * 0.37)
    (coin3_rect.centerx, coin3_rect.centery) = (width * (0.23 + 2 * btn_offset), height *(0.37 + item_price_offset))
    time_price_rect = time_price.get_rect(center=(width * (0.28 + 2 * btn_offset), height * (0.37 + item_price_offset)))
    (buy_btn3_rect.centerx, buy_btn3_rect.centery) = (width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
    (no_money3_rect.centerx, no_money3_rect.centery) = (width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
    #
    r_back_btn_rect.centerx = resized_screen.get_width() * 0.1
    r_back_btn_rect.centery = resized_screen.get_height() * 0.1
    #
    user_count_offset = 0.04
    user_btn_offset = 0.09
    # info_rect = info.get_rect(center=(width * 0.55, height * 0.08))
    (user_shield_rect.centerx, user_shield_rect.centery) = (width * 0.64, height * 0.08)
    user_sh_rect = user_shield.get_rect(center=(width * (0.64 + user_count_offset), height * 0.08))
    (user_life_rect.centerx, user_life_rect.centery) = (width * (0.64 + user_btn_offset), height * 0.08)
    user_l_rect = user_life.get_rect(center=(width * (0.64 + user_btn_offset + user_count_offset), height * 0.08))
    (user_time_rect.centerx, user_time_rect.centery ) = (width * (0.64 + 2 * user_btn_offset), height * 0.08)
    user_t_rect = user_time.get_rect(center=(width * (0.64 + (2 * user_btn_offset) + user_count_offset), height * 0.08))
    (user_coin_rect.centerx, user_coin_rect.centery) = (width * (0.64 + 3 * user_btn_offset), height * 0.08)
    user_c_rect = user_coin.get_rect(center = (width * (0.64 + (3 * user_btn_offset) + user_count_offset), height * 0.08))

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
            if pygame.mouse.get_pressed() == (1, 0, 0):
                x, y = event.pos
                if r_back_btn_rect.collidepoint(x, y):
                    store()
                if buy_btn1_rect.collidepoint(x, y) and coin_item_count >= s_price:
                    db.query_db(
                        f"update item set shield = {shield_item_count + 1 },  coin = {coin_item_count - s_price} where item_id=1;")
                    db.commit()
                if buy_btn2_rect.collidepoint(x,y) and coin_item_count >= l_price:
                    db.query_db(
                        f"update item set life = {life_item_count + 1},  coin = {coin_item_count - l_price} where item_id=1;")
                    db.commit()
                if buy_btn3_rect.collidepoint(x, y) and coin_item_count >= t_price:
                    db.query_db(
                        f"update item set slow = {slow_item_count + 1},  coin = {coin_item_count - t_price} where item_id=1;")
                    db.commit()

        shield_item_count = db.query_db("select shield from item where item_id=1;", one=True)['shield']
        life_item_count = db.query_db("select life from item where item_id=1;", one=True)['life']
        slow_item_count = db.query_db("select slow from item where item_id=1;", one=True)['slow']
        coin_item_count = db.query_db("select coin from item where item_id=1;", one=True)['coin']
        user_shield = user_font.render(f'X{shield_item_count}', True, black)
        user_life = user_font.render(f'X{life_item_count}', True, black)
        user_time = user_font.render(f'X{slow_item_count}', True, black)
        user_coin = user_font.render(f'X{coin_item_count}', True, black)

        screen.blit(back_store, back_store_rect)
        screen.blit(coin1_image, coin1_rect)
        screen.blit(coin2_image, coin2_rect)
        screen.blit(coin3_image, coin3_rect)
        screen.blit(shield_image, shield_rect)
        screen.blit(life_image, life_rect)
        screen.blit(time_image, time_rect)
        # screen.blit(info, info_rect)
        screen.blit(user_shield_image, user_shield_rect)
        screen.blit(user_shield, user_sh_rect)
        screen.blit(user_life_image, user_life_rect)
        screen.blit(user_life, user_l_rect)
        screen.blit(user_time_image, user_time_rect)
        screen.blit(user_time, user_t_rect)
        screen.blit(user_coin_image, user_coin_rect)
        screen.blit(user_coin, user_c_rect)


        if(coin_item_count >= s_price):
            screen.blit(buy_btn1_image, buy_btn1_rect)
        else:
            screen.blit(no_money1_image, no_money1_rect)
        if(coin_item_count >= l_price):
            screen.blit(buy_btn2_image, buy_btn2_rect)
        else :
            screen.blit(no_money2_image, no_money2_rect)
        if(coin_item_count >= t_price):
            screen.blit(buy_btn3_image, buy_btn3_rect)
        else:
            screen.blit(no_money3_image, no_money3_rect)
        screen.blit(shield_price, shield_price_rect)
        screen.blit(life_price, life_price_rect)
        screen.blit(time_price, time_price_rect)
        screen.blit(back_btn_image, back_btn_rect)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()