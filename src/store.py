from src.item import *
from src.interface import *
from db.db_interface import InterfDB
from src.game_value import *
db = InterfDB("db/data.db")
import src.game

global btn_offset
global item_price_offset
global item_btn_offset
global char_offset
global user_font
user_font = pygame.font.Font('DungGeunMo.ttf', 16)


def store():
    global resized_screen
    game_start = False

    # 배경 이미지
    back_store, back_store_rect = load_image('coin_t_rex3.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('alpha_back.png', width + ALPHA_MOVE, height)
    alpha_back_rect.left = -ALPHA_MOVE
    # 버튼 이미지
    char_btn_image, char_btn_rect = load_image('character.png', 150, 80, -1)
    r_char_btn_image, r_char_btn_rect = load_image(*resize('character.png', 150, 80, -1))
    skin_btn_image, skin_btn_rect = load_image('skin.png', 150, 80, -1)
    r_skin_btn_image, r_skin_btn_rect = load_image(*resize('skin.png', 150, 80, -1))
    item_btn_image, item_btn_rect = load_image('item_btn.png', 150, 80, -1)
    r_item_btn_image, r_item_btn_rect = load_image(*resize('item_btn.png', 150, 80, -1))
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
                    if r_char_btn_rect.collidepoint(x, y):
                        char_store()
                    if r_skin_btn_rect.collidepoint(x, y):
                        skin_store()
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
        screen.blit(alpha_back, alpha_back_rect)
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
    # 배경 이미지
    back_store, back_store_rect = load_image('coin_t_rex3.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('alpha_back.png', width + ALPHA_MOVE, height)
    alpha_back_rect.left = -ALPHA_MOVE
    # 코인 이미지
    coin1_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin1_image = transform.scale(coin1_image[0], (COIN_SIZE, COIN_SIZE))
    coin1_rect = coin1_image.get_rect()
    coin2_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin2_image = transform.scale(coin2_image[0], (COIN_SIZE, COIN_SIZE))
    coin2_rect = coin2_image.get_rect()
    coin3_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin3_image = transform.scale(coin3_image[0], (COIN_SIZE, COIN_SIZE))
    coin3_rect = coin3_image.get_rect()
    # 아이템 이미지
    shield_image, _ = load_sprite_sheet('item.png', 2, 1, -1, -1, -1)
    life_image, life_rect = load_image('love-shield.png', ITEM_SIZE, ITEM_SIZE, -1)
    time_image, _ = load_sprite_sheet('slow_pic.png', 2, 1, -1, -1, -1)
    shield_image = transform.scale(shield_image[0], (ITEM_SIZE, ITEM_SIZE))
    shield_rect = shield_image.get_rect()
    time_image = transform.scale(time_image[0], (ITEM_SIZE, ITEM_SIZE))
    time_rect = time_image.get_rect()
    # user가 가지고 있는 아이템 노출을 위한 이미지
    user_shield_image, _ = load_sprite_sheet('item.png', 2, 1, -1, -1, -1)
    user_shield_image = transform.scale(user_shield_image[0], (USER_ITEM_SIZE, USER_ITEM_SIZE))
    user_shield_rect = user_shield_image.get_rect()
    user_life_image, user_life_rect = load_image('love-shield.png', USER_ITEM_SIZE, USER_ITEM_SIZE, -1)
    user_time_image, _ = load_sprite_sheet('slow_pic.png', 2, 1, -1, -1, -1)
    user_time_image = transform.scale(user_time_image[0], (USER_ITEM_SIZE, USER_ITEM_SIZE))
    user_time_rect = user_time_image.get_rect()
    user_coin_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    user_coin_image = transform.scale(user_coin_image[0], (USER_ITEM_SIZE, USER_ITEM_SIZE))
    user_coin_rect = user_coin_image.get_rect()
    # item store 버튼 이미지
    buy_btn1_image, buy_btn1_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn2_image, buy_btn2_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn3_image, buy_btn3_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money1_image, no_money1_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money2_image, no_money2_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money3_image, no_money3_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    # 뒤로 가기 버튼 이미지
    back_btn_image, back_btn_rect = load_image('btn_back.png', STORE_BTN_X, STORE_BTN_Y, -1)
    r_back_btn_image, r_back_btn_rect = load_image(*resize('btn_back.png', STORE_BTN_X, STORE_BTN_Y, -1))
    # 아이템
    shield_item_count = db.query_db("select count from item where name='shield';", one=True)['count']
    life_item_count = db.query_db("select count from item where name='life';", one=True)['count']
    slow_item_count = db.query_db("select count from item where name='slow';", one=True)['count']
    coin_item_count = db.query_db("select count from item where name='coin';", one=True)['count']
    # 가격
    s_price = db.query_db("SELECT price from item where name = 'shield'", one=True)['price']
    l_price = db.query_db("SELECT price from item where name = 'life'", one=True)['price']
    t_price = db.query_db("SELECT price from item where name = 'slow'", one=True)['price']
    # 폰트
    my_font = pygame.font.Font('DungGeunMo.ttf', 18)
    # user_font = pygame.font.Font('DungGeunMo.ttf', 16)
    shield_price = my_font.render(f"x {s_price}", True, black)
    life_price = my_font.render(f'x {l_price}', True, black)
    time_price = my_font.render(f'x {t_price}', True, black)
    # info = my_font.render(f"[YOU HAVE]", True, black)
    user_shield = user_font.render(f'X{shield_item_count}', True, black)
    user_life = user_font.render(f'X{life_item_count}', True, black)
    user_time = user_font.render(f'X{slow_item_count}', True, black)
    user_coin = user_font.render(f'X{coin_item_count}', True, black)
    # 배치
    (shield_rect.centerx, shield_rect.centery) = (width * 0.25, height * 0.37)
    (coin1_rect.centerx, coin1_rect.centery) = (width * 0.23, height * (0.37 + item_price_offset))
    shield_price_rect = shield_price.get_rect(center=(width * 0.28, height * (0.37 + item_price_offset)))
    (buy_btn1_rect.centerx, buy_btn1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    (no_money1_rect.centerx, no_money1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    #
    (life_rect.centerx, life_rect.centery) = (width * (0.25 + btn_offset), height * 0.37)
    (coin2_rect.centerx, coin2_rect.centery) = (width * (0.23 + btn_offset), height * (0.37 + item_price_offset))
    life_price_rect = life_price.get_rect(center=(width * (0.28 + btn_offset), height * (0.37 + item_price_offset)))
    (buy_btn2_rect.centerx, buy_btn2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    (no_money2_rect.centerx, no_money2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    #
    (time_rect.centerx, time_rect.centery) = (width * (0.25 + 2 * btn_offset), height * 0.37)
    (coin3_rect.centerx, coin3_rect.centery) = (width * (0.23 + 2 * btn_offset), height * (0.37 + item_price_offset))
    time_price_rect = time_price.get_rect(center=(width * (0.28 + 2 * btn_offset), height * (0.37 + item_price_offset)))
    (buy_btn3_rect.centerx, buy_btn3_rect.centery) = (
                                                    width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
    (no_money3_rect.centerx, no_money3_rect.centery) = (
                                                    width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
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
    (user_time_rect.centerx, user_time_rect.centery) = (width * (0.64 + 2 * user_btn_offset), height * 0.08)
    user_t_rect = user_time.get_rect(center=(width * (0.64 + (2 * user_btn_offset) + user_count_offset), height * 0.08))
    (user_coin_rect.centerx, user_coin_rect.centery) = (width * (0.64 + 3 * user_btn_offset), height * 0.08)
    user_c_rect = user_coin.get_rect(center=(width * (0.64 + (3 * user_btn_offset) + user_count_offset), height * 0.08))

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
                        f"UPDATE item SET count = {shield_item_count + 1} where name = 'shield'"
                    )
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - 1} where name = 'coin'"
                    )
                    db.commit()
                if buy_btn2_rect.collidepoint(x, y) and coin_item_count >= l_price:
                    db.query_db(
                        f"UPDATE item SET count = {life_item_count + 1} where name = 'life'"
                    )
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - 1} where name = 'coin'"
                    )
                    db.commit()
                if buy_btn3_rect.collidepoint(x, y) and coin_item_count >= t_price:
                    db.query_db(
                        f"UPDATE item SET count = {slow_item_count + 1} where name = 'slow'"
                    )
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - 1} where name = 'coin'"
                    )
                    db.commit()

        shield_item_count = db.query_db("select count from item where name ='shield';", one=True)['count']
        life_item_count = db.query_db("select count from item where name='life';", one=True)['count']
        slow_item_count = db.query_db("select count from item where name='slow';", one=True)['count']
        coin_item_count = db.query_db("select count from item where name='coin';", one=True)['count']
        user_shield = user_font.render(f'X{shield_item_count}', True, black)
        user_life = user_font.render(f'X{life_item_count}', True, black)
        user_time = user_font.render(f'X{slow_item_count}', True, black)
        user_coin = user_font.render(f'X{coin_item_count}', True, black)

        screen.blit(back_store, back_store_rect)
        screen.blit(alpha_back, alpha_back_rect)
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

        if (coin_item_count >= s_price):
            screen.blit(buy_btn1_image, buy_btn1_rect)
        else:
            screen.blit(no_money1_image, no_money1_rect)
        if (coin_item_count >= l_price):
            screen.blit(buy_btn2_image, buy_btn2_rect)
        else:
            screen.blit(no_money2_image, no_money2_rect)
        if (coin_item_count >= t_price):
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


def char_store():
    global resized_screen
    image_space = 0.3
    game_start = False
    # 배경 이미지
    back_store, back_store_rect = load_image('coin_t_rex3.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('alpha_back.png', width + ALPHA_MOVE, height)
    alpha_back_rect.left = -ALPHA_MOVE
    # 코인 이미지
    coin1_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin1_image = transform.scale(coin1_image[0], (COIN_SIZE, COIN_SIZE))
    coin1_rect = coin1_image.get_rect()
    coin2_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin2_image = transform.scale(coin2_image[0], (COIN_SIZE, COIN_SIZE))
    coin2_rect = coin2_image.get_rect()
    coin3_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin3_image = transform.scale(coin3_image[0], (COIN_SIZE, COIN_SIZE))
    coin3_rect = coin3_image.get_rect()
    coin4_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin4_image = transform.scale(coin4_image[0], (COIN_SIZE, COIN_SIZE))
    coin4_rect = coin4_image.get_rect()
    # 아이템 이미지
    purple_image, _ = load_sprite_sheet('purple_dino.png', 6, 1, -1, -1, -1)
    purple_image = transform.scale(purple_image[0], (CHAR_SIZE, CHAR_SIZE))
    purple_rect = purple_image.get_rect()
    red_image, _ = load_sprite_sheet('red_dino.png', 6, 1, -1, -1, -1)
    red_image = transform.scale(red_image[0], (CHAR_SIZE, CHAR_SIZE))
    red_rect = red_image.get_rect()
    yellow_image, _ = load_sprite_sheet('yellow_dino.png', 6, 1, -1, -1, -1)
    yellow_image = transform.scale(yellow_image[0], (CHAR_SIZE, CHAR_SIZE))
    yellow_rect = yellow_image.get_rect()
    tux_image, _ = load_sprite_sheet('tux.png', 8, 9, -1, -1, -1)
    tux_image = transform.scale(tux_image[0], (CHAR_SIZE, CHAR_SIZE))
    tux_rect = tux_image.get_rect()
    # user의 코인
    coin_item_count = db.query_db("SELECT count FROM item WHERE name='coin';", one=True)['count']
    user_coin_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    user_coin_image = transform.scale(user_coin_image[0], (USER_ITEM_SIZE, USER_ITEM_SIZE))
    user_coin_rect = user_coin_image.get_rect()

    user_coin = user_font.render(f'X {coin_item_count}', True, black)
    # skin store 버튼 이미지
    buy_btn1_image, buy_btn1_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn2_image, buy_btn2_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn3_image, buy_btn3_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn4_image, buy_btn4_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money1_image, no_money1_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money2_image, no_money2_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money3_image, no_money3_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money4_image, no_money4_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out1_image, sold_out1_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out2_image, sold_out2_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out3_image, sold_out3_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out4_image, sold_out4_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    # 뒤로 가기 버튼 이미지
    back_btn_image, back_btn_rect = load_image('btn_back.png', STORE_BTN_X, STORE_BTN_Y, -1)
    r_back_btn_image, r_back_btn_rect = load_image(*resize('btn_back.png', STORE_BTN_X, STORE_BTN_Y, -1))
    # 가격
    p_price = db.query_db("SELECT price FROM character WHERE name = 'Purple'", one=True)['price']
    r_price = db.query_db("SELECT price FROM character WHERE name = 'Red'", one=True)['price']
    y_price = db.query_db("SELECT price FROM character WHERE name = 'Yellow'", one=True)['price']
    t_price = db.query_db("SELECT price FROM character WHERE name = 'Tux'", one=True)['price']
    # 폰트
    my_font = pygame.font.Font('DungGeunMo.ttf', 18)
    purple_price = my_font.render(f"x {p_price}", True, black)
    red_price = my_font.render(f'x {r_price}', True, black)
    yellow_price = my_font.render(f'x {y_price}', True, black)
    tux_price = my_font.render(f'x {y_price}', True, black)
    # 배치
    (purple_rect.centerx, purple_rect.centery) = (width * 0.2, height * 0.37)
    (coin1_rect.centerx, coin1_rect.centery) = (width * 0.18, height * (0.37 + item_price_offset))
    purple_price_rect = purple_price.get_rect(center=(width * 0.23, height * (0.37 + item_price_offset)))
    (buy_btn1_rect.centerx, buy_btn1_rect.centery) = (width * 0.2, height * (0.37 + item_btn_offset))
    (no_money1_rect.centerx, no_money1_rect.centery) = (width * 0.2, height * (0.37 + item_btn_offset))
    (sold_out1_rect.centerx, sold_out1_rect.centery) = (width * 0.2, height * (0.37 + item_btn_offset))
    #
    (red_rect.centerx, red_rect.centery) = (width * (0.2 + char_offset), height * 0.37)
    (coin2_rect.centerx, coin2_rect.centery) = (width * (0.18 + char_offset), height * (0.37 + item_price_offset))
    red_price_rect = red_price.get_rect(center=(width * (0.23 + char_offset), height * (0.37 + item_price_offset)))
    (buy_btn2_rect.centerx, buy_btn2_rect.centery) = (width * (0.2 + char_offset), height * (0.37 + item_btn_offset))
    (no_money2_rect.centerx, no_money2_rect.centery) = (width * (0.2 + char_offset), height * (0.37 + item_btn_offset))
    (sold_out2_rect.centerx, sold_out2_rect.centery) = (width * (0.2 + char_offset), height * (0.37 + item_btn_offset))
    #
    (yellow_rect.centerx, yellow_rect.centery) = (width * (0.2 + 2 * char_offset), height * 0.37)
    (coin3_rect.centerx, coin3_rect.centery) = (width * (0.18 + 2 * char_offset), height * (0.37 + item_price_offset))
    yellow_price_rect = yellow_price.get_rect(
                                        center=(width * (0.23 + 2 * char_offset), height * (0.37 + item_price_offset)))
    (buy_btn3_rect.centerx, buy_btn3_rect.centery) = (
                                                width * (0.2 + 2 * char_offset), height * (0.37 + item_btn_offset))
    (no_money3_rect.centerx, no_money3_rect.centery) = (
                                                width * (0.2 + 2 * char_offset), height * (0.37 + item_btn_offset))
    (sold_out3_rect.centerx, sold_out3_rect.centery) = (
                                                width * (0.2 + 2 * char_offset), height * (0.37 + item_btn_offset))
    #
    (tux_rect.centerx, tux_rect.centery) = (width * (0.2 + 3 * char_offset), height * 0.37)
    (coin4_rect.centerx, coin4_rect.centery) = (width * (0.18 + 3 * char_offset), height * (0.37 + item_price_offset))
    tux_price_rect = tux_price.get_rect(center=(width * (0.23 + 3 * char_offset), height * (0.37 + item_price_offset)))
    (buy_btn4_rect.centerx, buy_btn4_rect.centery) = (
    width * (0.2 + 3 * char_offset), height * (0.37 + item_btn_offset))
    (no_money4_rect.centerx, no_money4_rect.centery) = (
    width * (0.2 + 3 * char_offset), height * (0.37 + item_btn_offset))
    (sold_out4_rect.centerx, sold_out4_rect.centery) = (
    width * (0.2 + 3 * char_offset), height * (0.37 + item_btn_offset))
    #
    r_back_btn_rect.centerx = resized_screen.get_width() * 0.1
    r_back_btn_rect.centery = resized_screen.get_height() * 0.1
    #
    (user_coin_rect.centerx, user_coin_rect.centery) = (width * (0.65 + btn_offset), height * 0.08)
    user_c_rect = user_coin.get_rect(center=(width * (0.69 + btn_offset), height * 0.08))
    user_coin = user_font.render(f'X {coin_item_count}', True, black)
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
                if buy_btn1_rect.collidepoint(x, y) and coin_item_count >= p_price:
                    db.query_db(
                        f"UPDATE character SET  is_paid=1  WHERE name = 'Purple';")
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - p_price} WHERE name='coin'"
                    )
                    db.commit()
                if buy_btn2_rect.collidepoint(x, y) and coin_item_count >= r_price:
                    db.query_db(
                        f"UPDATE character SET  is_paid=1  WHERE name = 'Red';")
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - r_price} WHERE name='coin'"
                    )
                    db.commit()
                if buy_btn3_rect.collidepoint(x, y) and coin_item_count >= y_price:
                    db.query_db(
                        f"UPDATE character SET  is_paid=1  WHERE name = 'Yellow';")
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - y_price} WHERE name='coin'"
                    )
                    db.commit()
                if buy_btn4_rect.collidepoint(x, y) and coin_item_count >= t_price:
                    db.query_db(
                        f"UPDATE character SET  is_paid=1  WHERE name = 'Tux';")
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - t_price} WHERE name='coin'"
                    )
                    db.commit()
        coin_item_count = db.query_db("SELECT count FROM item WHERE name='coin';", one=True)['count']
        user_coin = user_font.render(f'X {coin_item_count}', True, black)

        screen.blit(back_store, back_store_rect)
        screen.blit(alpha_back, alpha_back_rect)
        screen.blit(coin1_image, coin1_rect)
        screen.blit(coin2_image, coin2_rect)
        screen.blit(coin3_image, coin3_rect)
        screen.blit(coin4_image, coin4_rect)
        screen.blit(purple_image, purple_rect)
        screen.blit(red_image, red_rect)
        screen.blit(yellow_image, yellow_rect)
        screen.blit(tux_image, tux_rect)
        screen.blit(purple_price, purple_price_rect)
        screen.blit(red_price, red_price_rect)
        screen.blit(yellow_price, yellow_price_rect)
        screen.blit(tux_price, tux_price_rect)
        # 구매했는지 내역
        # 구매했으면 1, 구매 안했으면 0
        is_purple_buy = db.query_db("SELECT is_paid FROM character WHERE name = 'Purple';", one=True)['is_paid']
        is_red_buy = db.query_db("SELECT is_paid FROM character WHERE name = 'Red';", one=True)['is_paid']
        is_yellow_buy = db.query_db("SELECT is_paid FROM character WHERE name = 'Yellow';", one=True)['is_paid']
        is_tux_buy = db.query_db("SELECT is_paid FROM character WHERE name = 'Tux';", one=True)['is_paid']

        # 구매했으면
        if (is_purple_buy == 1):
            screen.blit(sold_out1_image, sold_out1_rect)
        elif (coin_item_count >= p_price):
            screen.blit(buy_btn1_image, buy_btn1_rect)
        else:
            screen.blit(no_money1_image, no_money1_rect)
        #
        if (is_red_buy == 1):
            screen.blit(sold_out2_image, sold_out2_rect)
        elif (coin_item_count >= r_price):
            screen.blit(buy_btn2_image, buy_btn2_rect)
        else:
            screen.blit(no_money2_image, no_money2_rect)
        #
        if (is_yellow_buy == 1):
            screen.blit(sold_out3_image, sold_out3_rect)
        elif (coin_item_count >= y_price):
            screen.blit(buy_btn3_image, buy_btn3_rect)
        else:
            screen.blit(no_money3_image, no_money3_rect)
        #
        if (is_tux_buy == 1):
            screen.blit(sold_out4_image, sold_out4_rect)
        elif (coin_item_count >= t_price):
            screen.blit(buy_btn4_image, buy_btn4_rect)
        else:
            screen.blit(no_money4_image, no_money4_rect)
        # sold out 버튼 구현 필요
        screen.blit(back_btn_image, back_btn_rect)
        screen.blit(user_coin, user_c_rect)
        screen.blit(user_coin_image, user_coin_rect)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def skin_store():
    global resized_screen
    image_space = 0.3
    game_start = False
    # 배경 이미지
    back_store, back_store_rect = load_image('coin_t_rex3.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('alpha_back.png', width + 20, height)
    alpha_back_rect.left = -20
    # 코인 이미지
    coin1_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin1_image = transform.scale(coin1_image[0], (COIN_SIZE, COIN_SIZE))
    coin1_rect = coin1_image.get_rect()
    coin2_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin2_image = transform.scale(coin2_image[0], (COIN_SIZE, COIN_SIZE))
    coin2_rect = coin2_image.get_rect()
    coin3_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    coin3_image = transform.scale(coin3_image[0], (COIN_SIZE, COIN_SIZE))
    coin3_rect = coin3_image.get_rect()
    # 아이템 이미지
    spring_image, spring_rect = load_image('ex_spring.png', SKIN_X, SKIN_Y, -1)
    fall_image, fall_rect = load_image('ex_fall.png', SKIN_X, SKIN_Y, -1)
    winter_image, winter_rect = load_image('ex_winter.png', SKIN_X, SKIN_Y, -1)
    # user의 코인
    coin_item_count = db.query_db("SELECT count FROM item WHERE name='coin';", one=True)['count']
    user_coin_image, _ = load_sprite_sheet('coin.png', 1, 7, -1, -1, -1)
    user_coin_image = transform.scale(user_coin_image[0], (USER_ITEM_SIZE, USER_ITEM_SIZE))
    user_coin_rect = user_coin_image.get_rect()
    # user_font = pygame.font.Font('DungGeunMo.ttf', 16)
    user_coin = user_font.render(f'X {coin_item_count}', True, black)
    # skin store 버튼 이미지
    buy_btn1_image, buy_btn1_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn2_image, buy_btn2_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    buy_btn3_image, buy_btn3_rect = load_image('buy.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money1_image, no_money1_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money2_image, no_money2_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    no_money3_image, no_money3_rect = load_image('X.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out1_image, sold_out1_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out2_image, sold_out2_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    sold_out3_image, sold_out3_rect = load_image('sold_out.png', STORE_BTN_X, STORE_BTN_Y, -1)
    # 뒤로 가기 버튼 이미지
    back_btn_image, back_btn_rect = load_image('btn_back.png', STORE_BTN_X, STORE_BTN_Y, -1)
    r_back_btn_image, r_back_btn_rect = load_image(*resize('btn_back.png', STORE_BTN_X, STORE_BTN_Y, -1))
    # 가격
    s_price = db.query_db("SELECT price FROM skin WHERE name = 'Spring'", one=True)['price']
    f_price = db.query_db("SELECT price FROM skin WHERE name = 'Fall'", one=True)['price']
    w_price = db.query_db("SELECT price FROM skin WHERE name = 'Winter'", one=True)['price']
    # 폰트
    my_font = pygame.font.Font('DungGeunMo.ttf', 18)
    spring_price = my_font.render(f"x {s_price}", True, black)
    fall_price = my_font.render(f'x {f_price}', True, black)
    winter_price = my_font.render(f'x {w_price}', True, black)
    # 배치
    (spring_rect.centerx, spring_rect.centery) = (width * 0.25, height * 0.37)
    (coin1_rect.centerx, coin1_rect.centery) = (width * 0.23, height * (0.37 + item_price_offset))
    spring_price_rect = spring_price.get_rect(center=(width * 0.28, height * (0.37 + item_price_offset)))
    (buy_btn1_rect.centerx, buy_btn1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    (no_money1_rect.centerx, no_money1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    (sold_out1_rect.centerx, sold_out1_rect.centery) = (width * 0.25, height * (0.37 + item_btn_offset))
    #
    (fall_rect.centerx, fall_rect.centery) = (width * (0.25 + btn_offset), height * 0.37)
    (coin2_rect.centerx, coin2_rect.centery) = (width * (0.23 + btn_offset), height * (0.37 + item_price_offset))
    fall_price_rect = fall_price.get_rect(center=(width * (0.28 + btn_offset), height * (0.37 + item_price_offset)))
    (buy_btn2_rect.centerx, buy_btn2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    (no_money2_rect.centerx, no_money2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    (sold_out2_rect.centerx, sold_out2_rect.centery) = (width * (0.25 + btn_offset), height * (0.37 + item_btn_offset))
    #
    (winter_rect.centerx, winter_rect.centery) = (width * (0.25 + 2 * btn_offset), height * 0.37)
    (coin3_rect.centerx, coin3_rect.centery) = (width * (0.23 + 2 * btn_offset), height * (0.37 + item_price_offset))
    winter_price_rect = winter_price.get_rect(
        center=(width * (0.28 + 2 * btn_offset), height * (0.37 + item_price_offset)))
    (buy_btn3_rect.centerx, buy_btn3_rect.centery) = (
    width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
    (no_money3_rect.centerx, no_money3_rect.centery) = (
    width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
    (sold_out3_rect.centerx, sold_out3_rect.centery) = (
    width * (0.25 + 2 * btn_offset), height * (0.37 + item_btn_offset))
    #
    r_back_btn_rect.centerx = resized_screen.get_width() * 0.1
    r_back_btn_rect.centery = resized_screen.get_height() * 0.1
    #
    (user_coin_rect.centerx, user_coin_rect.centery) = (width * (0.65 + btn_offset), height * 0.08)
    user_c_rect = user_coin.get_rect(center=(width * (0.69 + btn_offset), height * 0.08))

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
                        f"UPDATE skin SET  is_paid=1  WHERE name = 'Spring';")
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - s_price} WHERE name='coin'"
                    )
                    db.commit()
                if buy_btn2_rect.collidepoint(x, y) and coin_item_count >= f_price:
                    db.query_db(
                        f"UPDATE skin SET  is_paid=1  WHERE name = 'Fall';")
                    db.query_db(
                        f"update item SET count = {coin_item_count - f_price} WHERE name='coin'"
                    )
                    db.commit()
                if buy_btn3_rect.collidepoint(x, y) and coin_item_count >= w_price:
                    db.query_db(
                        f"UPDATE skin SET  is_paid=1  WHERE name = 'Winter';")
                    db.query_db(
                        f"UPDATE item SET count = {coin_item_count - w_price} WHERE name='coin'"
                    )
                    db.commit()
        coin_item_count = db.query_db("SELECT count FROM item WHERE name='coin';", one=True)['count']
        user_coin = user_font.render(f'X {coin_item_count}', True, black)

        screen.blit(back_store, back_store_rect)
        screen.blit(alpha_back, alpha_back_rect)
        screen.blit(coin1_image, coin1_rect)
        screen.blit(coin2_image, coin2_rect)
        screen.blit(coin3_image, coin3_rect)
        screen.blit(spring_image, spring_rect)
        screen.blit(fall_image, fall_rect)
        screen.blit(winter_image, winter_rect)
        screen.blit(spring_price, spring_price_rect)
        screen.blit(fall_price, fall_price_rect)
        screen.blit(winter_price, winter_price_rect)
        # 구매 내역
        # 구매 했으면 1, 안했으면 0
        is_spring_buy = db.query_db("SELECT is_paid FROM skin WHERE name = 'Spring';", one=True)['is_paid']
        is_fall_buy = db.query_db("SELECT is_paid FROM skin WHERE name = 'Fall';", one=True)['is_paid']
        is_winter_buy = db.query_db("SELECT is_paid FROM skin WHERE name = 'Winter';", one=True)['is_paid']
        if (is_spring_buy == 1):
            screen.blit(sold_out1_image, sold_out1_rect)
        elif (coin_item_count >= s_price):
            screen.blit(buy_btn1_image, buy_btn1_rect)
        else:
            screen.blit(no_money1_image, no_money1_rect)
        #
        if (is_fall_buy == 1):
            screen.blit(sold_out2_image, sold_out2_rect)
        elif (coin_item_count >= f_price):
            screen.blit(buy_btn2_image, buy_btn2_rect)
        else:
            screen.blit(no_money2_image, no_money2_rect)
        #
        if (is_winter_buy == 1):
            screen.blit(sold_out3_image, sold_out3_rect)
        elif (coin_item_count >= w_price):
            screen.blit(buy_btn3_image, buy_btn3_rect)
        else:
            screen.blit(no_money3_image, no_money3_rect)
        screen.blit(back_btn_image, back_btn_rect)
        screen.blit(user_coin, user_c_rect)
        screen.blit(user_coin_image, user_coin_rect)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
