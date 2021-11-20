from pygame.image import load
from src.dino import *
from src.obstacle import *
from src.item import *
from src.interface import *
import src.game as game
import src.setting as setting
from src.game import *
from db.db_interface import InterfDB
from src.store import store

db = InterfDB("db/score.db")


def option():
    global on_pushtime
    global off_pushtime
    # global bgm_on
    global high_score
    global resized_screen
    btnpush_interval = 500  # ms
    pygame.mixer.music.stop()
    done = False
    db_init = False
    large_text = pygame.font.Font('freesansbold.ttf', 60)
    text_surf, text_rect = text_objects("[ OPTION ]", large_text)
    btn_bgm_on, btn_bgm_on_rect = load_image('btn_bgm_on.png', 80, 80, -1)
    btn_bgm_off, btn_bgm_off_rect = load_image('btn_bgm_off.png', 80, 80, -1)
    r_btn_bgm_on, r_btn_bgm_on_rect = load_image(*resize('btn_bgm_on.png', 80, 80, -1))
    init_btn_image, init_btn_rect = load_image('scorereset.png', 80, 80, -1)
    r_init_btn_image, r_init_btn_rect = load_image(*resize('scorereset.png', 80, 80, -1))
    btn_gamerule, btn_gamerule_rect = load_image('btn_gamerule.png', 80, 80, -1)
    r_btn_gamerule, r_btn_gamerule_rect = load_image(*resize('btn_gamerule.png', 80, 80, -1))
    btn_home, btn_home_rect = load_image('main_button.png', 70, 62, -1)
    r_btn_home, r_btn_home_rect = load_image(*resize('main_button.png', 70, 62, -1))
    btn_credit, btn_credit_rect = load_image('btn_credit.png', 150, 50, -1)
    r_btn_credit, r_btn_credit_rect = load_image(*resize('btn_credit.png', 180, 80, -1))

    text_rect.center = (width * 0.5, height * 0.15)
    btn_bgm_on_rect.center = (width * 0.25, height * 0.5)
    init_btn_rect.center = (width * 0.5, height * 0.5)
    btn_gamerule_rect.center = (width * 0.75, height * 0.5)
    btn_home_rect.center = (width * 0.9, height * 0.15)
    btn_credit_rect.center = (width * 0.9, height * 0.85)

    while not done:
        for event in pygame.event.get():

            # CHANGE SIZE START
            if event.type == pygame.VIDEORESIZE and not full_screen:
                # r_btn_gamestart, r_btn_gamestart_rect = load_image(*resize('btn_start.png', 150, 50, -1))
                # btn_gamestart, btn_gamestart_rect = load_image('btn_start.png', 150, 50, -1)
                # r_btn_board, r_btn_board_rect = load_image(*resize('btn_board.png', 150, 50, -1))
                # btn_board, btn_board_rect = load_image('btn_board.png', 150, 50, -1)
                # r_btn_option, r_btn_option_rect = load_image(*resize('btn_option.png', 150, 50, -1))
                # btn_option, btn_option_rect = load_image('btn_option.png', 150, 50, -1)
                pass
                # IMGPOS
                # BACKGROUND IMG POS
                # background_rect.bottomleft = (width*0, height)

            # CHANGE SIZE END

            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    x, y = event.pos
                    if r_btn_home_rect.collidepoint(x, y):
                        game.intro_screen()

                    if r_btn_bgm_on_rect.collidepoint(x, y) and setting.bgm_on:
                        off_pushtime = pygame.time.get_ticks()
                        if off_pushtime - on_pushtime > btnpush_interval:
                            setting.bgm_on = False

                    if r_btn_bgm_on_rect.collidepoint(x, y) and not setting.bgm_on:
                        on_pushtime = pygame.time.get_ticks()
                        if on_pushtime - off_pushtime > btnpush_interval:
                            setting.bgm_on = True

                    if r_init_btn_rect.collidepoint(x, y):
                        db.query_db("delete from hard_mode;")
                        db.query_db("delete from easy_mode")
                        db.commit()
                        high_score = 0
                        db_init = True

                    if r_btn_gamerule_rect.collidepoint(x, y):
                        gamerule()

                    if r_btn_credit_rect.collidepoint(x, y):
                        credit()

            # if event.type == pygame.VIDEORESIZE:
            #     check_scr_size(event.w, event.h)

        r_init_btn_rect.centerx = resized_screen.get_width() * 0.5
        r_init_btn_rect.centery = resized_screen.get_height() * 0.5
        r_btn_gamerule_rect.centerx = resized_screen.get_width() * 0.75
        r_btn_gamerule_rect.centery = resized_screen.get_height() * 0.5
        r_btn_home_rect.centerx = resized_screen.get_width() * 0.9
        r_btn_home_rect.centery = resized_screen.get_height() * 0.15
        r_btn_credit_rect.centerx = resized_screen.get_width() * 0.9
        r_btn_credit_rect.centery = resized_screen.get_height() * 0.85

        screen.fill(background_col)
        screen.blit(text_surf, text_rect)
        screen.blit(init_btn_image, init_btn_rect)
        screen.blit(btn_gamerule, btn_gamerule_rect)
        screen.blit(btn_home, btn_home_rect)
        screen.blit(btn_credit, btn_credit_rect)

        if setting.bgm_on:
            screen.blit(btn_bgm_on, btn_bgm_on_rect)
            r_btn_bgm_on_rect.centerx = resized_screen.get_width() * 0.25
            r_btn_bgm_on_rect.centery = resized_screen.get_height() * 0.5
        if not setting.bgm_on:
            screen.blit(btn_bgm_off, btn_bgm_on_rect)
            r_btn_bgm_on_rect.centerx = resized_screen.get_width() * 0.25
            r_btn_bgm_on_rect.centery = resized_screen.get_height() * 0.5
        if db_init:
            draw_text("Scoreboard cleared", font, screen, 400, 300, black)

        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()

        clock.tick(FPS)
    pygame.quit()
    quit()


def select_mode():
    global resized_screen
    game_start = False
    btnpush_interval = 500

    # 배경 이미지
    background, background_rect = load_image('coin_t_rex2.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('alpha_back.png', width + 20, height)
    alpha_back_rect.left = -20
    # 버튼 이미지
    # easy mode button
    easymode_btn_image, easymode_btn_rect = load_image('easy.png', 160, 80, -1)
    r_easymode_btn_image, r_easy_btn_rect = load_image(*resize('easy.png', 160, 80, -1))
    # hardmode button
    btn_hardmode, btn_hardmode_rect = load_image('hard.png', 160, 80, -1)
    r_btn_hardmode, r_btn_hardmode_rect = load_image(*resize('hard.png', 160, 80, -1))
    # store button
    btn_store, btn_store_rect = load_image('store.png', 160, 80, -1)
    r_btn_store, r_btn_store_rect = load_image(*resize('store.png', 160, 80, -1))
    # set button
    btn_set, btn_set_rect = load_image('set.png', 160, 80, -1)
    r_btn_set, r_btn_set_rect = load_image(*resize('set.png', 160, 80, -1))
    # back button
    btn_back, btn_back_rect = load_image('btn_back.png', 100, 50, -1)
    r_btn_back, r_btn_back_rect = load_image(*resize('btn_back.png', 100, 50, -1))
    # easymode_btn_rect.center = (width * 0.5, height * 0.3)
    # btn_hardmode_rect.center = (width * 0.5, height * 0.55)
    # btn_store_rect.center = (width * 0.5, height * 0.7)

    while not game_start:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE and not full_screen:
                background_rect.bottomleft = (width * 0, height)
            if event.type == pygame.QUIT:
                game_start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    x, y = event.pos
                    if r_easy_btn_rect.collidepoint(x, y):
                        game.gameplay_easy()
                    if r_btn_hardmode_rect.collidepoint(x, y):
                        game.gameplay_hard()
                    if r_btn_store_rect.collidepoint(x, y):
                        store()
                    if r_btn_back_rect.collidepoint(x, y):
                        game.intro_screen()
                    if r_btn_set_rect.collidepoint(x, y):
                        set()

            if event.type == pygame.VIDEORESIZE:
                check_scr_size(event.w, event.h)

        r_easy_btn_rect.centerx = resized_screen.get_width() * 0.5
        r_easy_btn_rect.centery = resized_screen.get_height() * 0.26
        r_btn_hardmode_rect.centerx = resized_screen.get_width() * 0.5
        r_btn_hardmode_rect.centery = resized_screen.get_height() * (0.26 + select_offset)
        r_btn_store_rect.centerx = resized_screen.get_width() * 0.5
        r_btn_store_rect.centery = resized_screen.get_height() * (0.26 + 2 * select_offset)
        r_btn_set_rect.centerx = resized_screen.get_width() * 0.5
        r_btn_set_rect.centery = resized_screen.get_height() * (0.26 + 3 * select_offset)
        r_btn_back_rect.centerx = resized_screen.get_width() * 0.1
        r_btn_back_rect.centery = resized_screen.get_height() * 0.1

        screen.blit(background, background_rect)
        screen.blit(alpha_back, alpha_back_rect)
        disp_select_buttons(easymode_btn_image, btn_hardmode, btn_store, btn_set, btn_back)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()

        clock.tick(FPS)
    pygame.quit()
    quit()


def gamerule():
    global resized_screen
    game_quit = False
    max_per_screen = 10
    screen_board_height = resized_screen.get_height()
    screen_board = pygame.surface.Surface((
        resized_screen.get_width(),
        screen_board_height
    ))

    gamerule_image, gamerule_rect = load_image("gamerule.png", 800, 300, -1)
    gamerule_rect.centerx = width * 0.5
    gamerule_rect.centery = height * 0.5

    # back button
    btn_back, btn_back_rect = load_image('btn_back.png', 100, 50, -1)
    r_btn_back, r_btn_back_rect = load_image(*resize('btn_back.png', 100, 50, -1))

    while not game_quit:
        if pygame.display.get_surface() is None:
            game_quit = True
        else:
            screen_board.fill(background_col)
            screen_board.blit(gamerule_image, gamerule_rect)
            screen_board.blit(btn_back, btn_back_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        game_quit = True
                        # intro_screen()
                        option()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        x, y = event.pos
                        if r_btn_back_rect.collidepoint(x, y):
                            option()
                    # if event.button == 1:
                    # game_quit = True
                    # intro_screen()
                    # option()
                if event.type == pygame.VIDEORESIZE:
                    check_scr_size(event.w, event.h)
            r_btn_back_rect.centerx = resized_screen.get_width() * 0.1
            r_btn_back_rect.centery = resized_screen.get_height() * 0.1
            score_board(btn_back)
            screen.blit(screen_board, (0, 0))
            resized_screen.blit(
                pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                resized_screen_center)
            pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


def credit():
    global resized_screen
    done = False
    creditimg, creditimg_rect = load_image('credit.png', width, height, -1)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return False
            if event.type == pygame.VIDEORESIZE:
                check_scr_size(event.w, event.h)
        screen.blit(creditimg, creditimg_rect)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def set():
    global resized_screen
    game_start = False
    btnpush_interval = 500
    # 배경 이미지
    background, background_rect = load_image('default_back.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('alpha_back.png', width + 20, height)
    alpha_back_rect.left = -20
    # 폰트 배치
    big_font = pygame.font.Font('DungGeunMo.ttf', 40)
    # 뒤로가기
    back_btn_image, back_btn_rect = load_image('btn_back.png', 100, 50, -1)
    r_back_btn_image, r_back_btn_rect = load_image(*resize('btn_back.png', 100, 50, -1))
    # 폰트
    char_title = big_font.render('CHARACTER', True, black)
    skin_title = big_font.render('SKIN', True, black)
    #
    spring_image, spring_rect = load_image('ex_spring.png', 230, 210, -1)
    un_spring_image, un_spring_rect = load_image('unselect_spring.png', 230, 210, -1)
    fall_image, fall_rect = load_image('ex_fall.png', 230, 210, -1)
    un_fall_image, un_fall_rect = load_image('unselect_fall.png', 230, 210, -1)
    winter_image, winter_rect = load_image('ex_winter.png', 230, 210, -1)
    un_winter_image, un_winter_rect = load_image('unselect_winter.png', 230, 210, -1)
    #
    purple_image, _ = load_sprite_sheet('purple_dino.png', 6, 1, -1, -1, -1)
    purple_image = transform.scale(purple_image[0], (50, 50))
    purple_rect = purple_image.get_rect()
    un_purple_image, un_purple_rect = load_image('unselect_purple.png', 50, 50, -1)
    red_image, _ = load_sprite_sheet('red_dino.png', 6, 1, -1, -1, -1)
    red_image = transform.scale(red_image[0], (50, 50))
    red_rect = red_image.get_rect()
    un_red_image, un_red_rect = load_image('unselect_red.png', 50, 50, -1)
    yellow_image, _ = load_sprite_sheet('yellow_dino.png', 6, 1, -1, -1, -1)
    yellow_image = transform.scale(yellow_image[0], (50, 50))
    yellow_rect = yellow_image.get_rect()
    un_yellow_image, un_yellow_rect = load_image('unselect_yellow.png', 50, 50, -1)
    tux_image, _ = load_sprite_sheet('tux.png', 8, 9, -1, -1, -1)
    tux_image = transform.scale(tux_image[0], (50, 50))
    tux_rect = tux_image.get_rect()
    un_tux_image, un_tux_rect = load_image('unselect_tux.png', 50, 50, -1)
    #
    check1, check1_rect = load_image('check.png', 60, 60, -1)
    check2, check2_rect = load_image('check.png', 60, 60, -1)
    check3, check3_rect = load_image('check.png', 60, 60, -1)
    check4, check4_rect = load_image('check.png', 60, 60, -1)
    check5, check5_rect = load_image('check.png', 60, 60, -1)
    check6, check6_rect = load_image('check.png', 60, 60, -1)
    check7, check7_rect = load_image('check.png', 60, 60, -1)

    # 각 skin, character 구매여부
    buy_spring = db.query_db("select is_paid from skin where name='Spring'", one=True)['is_paid']
    buy_fall = db.query_db("select is_paid from skin where name='Fall'", one=True)['is_paid']
    buy_winter = db.query_db("select is_paid from skin where name='Winter'", one=True)['is_paid']
    buy_purple = db.query_db("select is_paid from character where name='Purple'", one=True)['is_paid']
    buy_red = db.query_db("select is_paid from character where name='Red'", one=True)['is_paid']
    buy_yellow = db.query_db("select is_paid from character where name='Yellow'", one=True)['is_paid']
    buy_tux = db.query_db("select is_paid from character where name='Tux'", one=True)['is_paid']
    # 오프셋 지정
    skin_height = 0.32
    char_height = 0.72
    skin_offset = 0.25
    char_offset = 0.2
    # 배치
    skin_title_rect = skin_title.get_rect(center=(width * 0.5, height * 0.13))
    (check1_rect.centerx, check1_rect.centery) = (width * (skin_offset), height * (skin_height))
    (spring_rect.centerx, spring_rect.centery) = (width * (skin_offset), height * (skin_height))
    (un_spring_rect.centerx, un_spring_rect.centery) = (width * (skin_offset), height * (skin_height))
    (check2_rect.centerx, check2_rect.centery) = (width * (2 * skin_offset), height * (skin_height))
    (fall_rect.centerx, fall_rect.centery) = (width * (2 * skin_offset), height * (skin_height))
    (un_fall_rect.centerx, un_fall_rect.centery) = (width * (2 * skin_offset), height * (skin_height))
    (check3_rect.centerx, check3_rect.centery) = (width * (3 * skin_offset), height * (skin_height))
    (winter_rect.centerx, winter_rect.centery) = (width * (3 * skin_offset), height * (skin_height))
    (un_winter_rect.centerx, un_winter_rect.centery) = (width * (3 * skin_offset), height * (skin_height))
    #
    char_title_rect = char_title.get_rect(center=(width * 0.5, height * 0.55))
    (purple_rect.centerx, purple_rect.centery) = (width * (char_offset), height * (char_height))
    (un_purple_rect.centerx, un_purple_rect.centery) = (width * (char_offset), height * (char_height))
    (check4_rect.centerx, check4_rect.centery) = (width * (char_offset), height * (char_height))
    (red_rect.centerx, red_rect.centery) = (width * (2 * char_offset), height * (char_height))
    (un_red_rect.centerx, un_red_rect.centery) = (width * (2 * char_offset), height * (char_height))
    (check5_rect.centerx, check5_rect.centery) = (width * (2 * char_offset), height * (char_height))
    (yellow_rect.centerx, yellow_rect.centery) = (width * (3 * char_offset), height * (char_height))
    (un_yellow_rect.centerx, un_yellow_rect.centery) = (width * (3 * char_offset), height * (char_height))
    (check6_rect.centerx, check6_rect.centery) = (width * (3 * char_offset), height * (char_height))
    (tux_rect.centerx, tux_rect.centery) = (width * (4 * char_offset), height * (char_height))
    (un_tux_rect.centerx, un_tux_rect.centery) = (width * (4 * char_offset), height * (char_height))
    (check7_rect.centerx, check7_rect.centery) = (width * (4 * char_offset), height * (char_height))
    r_back_btn_rect.centerx = resized_screen.get_width() * 0.1
    r_back_btn_rect.centery = resized_screen.get_height() * 0.1
    while not game_start:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE and not full_screen:
                background_rect.bottomleft = (width * 0, height)
            if event.type == pygame.QUIT:
                game_start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    x, y = event.pos
                    if r_back_btn_rect.collidepoint(x, y):
                        select_mode()
                    if spring_rect.collidepoint(x, y) and buy_spring == 1:
                        # 이미 적용이 됐으면
                        if is_spring == 1:
                            db.query_db(f"UPDATE skin SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE skin SET is_apply = CASE WHEN name = 'Spring' THEN 1 ELSE 0 END;")
                            db.commit()
                    if fall_rect.collidepoint(x, y) and buy_fall == 1:
                        if is_fall == 1:
                            db.query_db(f"UPDATE skin SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE skin SET is_apply = CASE WHEN name = 'Fall' THEN 1 ELSE 0 END;")
                            db.commit()
                    if winter_rect.collidepoint(x, y) and buy_winter == 1:
                        if is_winter == 1:
                            db.query_db(f"UPDATE skin SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE skin SET is_apply = CASE WHEN name = 'Winter' THEN 1 ELSE 0 END;")
                            db.commit()
                    if purple_rect.collidepoint(x, y) and buy_purple == 1:
                        if is_purple == 1:
                            db.query_db(f"UPDATE character SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE character SET is_apply = CASE WHEN name = 'Purple' THEN 1 ELSE 0 END;")
                            db.commit()
                    if red_rect.collidepoint(x, y) and buy_red == 1:
                        if is_red == 1:
                            db.query_db(f"UPDATE character SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE character SET is_apply = CASE WHEN name = 'Red' THEN 1 ELSE 0 END;")
                            db.commit()
                    if yellow_rect.collidepoint(x, y) and buy_yellow == 1:
                        if is_yellow == 1:
                            db.query_db(f"UPDATE character SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE character SET is_apply = CASE WHEN name = 'Yellow' THEN 1 ELSE 0 END;")
                            db.commit()
                    if tux_rect.collidepoint(x, y) and buy_tux == 1:
                        if is_tux == 1:
                            db.query_db(f"UPDATE character SET is_apply = 0")
                            db.commit()
                        else:
                            db.query_db(
                                f"UPDATE character SET is_apply = CASE WHEN name = 'Tux' THEN 1 ELSE 0 END;")
                            db.commit()
            if event.type == pygame.VIDEORESIZE:
                check_scr_size(event.w, event.h)

        # 각 skin 및 char 적용 여부
        is_spring = db.query_db("select is_apply from skin where name='Spring'", one=True)['is_apply']
        is_fall = db.query_db("select is_apply from skin where name = 'Fall'", one=True)['is_apply']
        is_winter = db.query_db("select is_apply from skin where name = 'Winter'", one=True)['is_apply']
        is_purple = db.query_db("select is_apply from character where name = 'Purple'", one=True)['is_apply']
        is_red = db.query_db("select is_apply from character where name = 'Red'", one=True)['is_apply']
        is_yellow = db.query_db("select is_apply from character where name = 'Yellow'", one=True)['is_apply']
        is_tux = db.query_db("select is_apply from character where name = 'Tux'", one=True)['is_apply']
        # (갱신)) 구매여부
        buy_spring = db.query_db("select is_paid from skin where name='Spring'", one=True)['is_paid']
        buy_fall = db.query_db("select is_paid from skin where name='Fall'", one=True)['is_paid']
        buy_winter = db.query_db("select is_paid from skin where name='Winter'", one=True)['is_paid']
        buy_purple = db.query_db("select is_paid from character where name='Purple'", one=True)['is_paid']
        buy_red = db.query_db("select is_paid from character where name='Red'", one=True)['is_paid']
        buy_yellow = db.query_db("select is_paid from character where name='Yellow'", one=True)['is_paid']
        buy_tux = db.query_db("select is_paid from character where name='Tux'", one=True)['is_paid']

        screen.blit(background, background_rect)
        screen.blit(alpha_back, alpha_back_rect)
        screen.blit(char_title, char_title_rect)
        screen.blit(skin_title, skin_title_rect)
        screen.blit(back_btn_image, back_btn_rect)
        # is_apply = 1은 적용 됐다는 뜻, 0은 안됐다는 뜻
        # is_paied = 1은 샀다는 뜻, 0은 안샀다는 뜻
        if buy_spring == 1:
            screen.blit(spring_image, spring_rect)
            if is_spring == 1:
                screen.blit(check1, check1_rect)
        else:
            screen.blit(un_spring_image, un_spring_rect)
        #
        if buy_fall == 1:
            screen.blit(fall_image, fall_rect)
            if is_fall == 1:
                screen.blit(check2, check2_rect)
        else:
            screen.blit(un_fall_image, un_fall_rect)
        #
        if buy_winter == 1:
            screen.blit(winter_image, winter_rect)
            if is_winter == 1:
                screen.blit(check3, check3_rect)
        else:
            screen.blit(un_winter_image, un_winter_rect)
        #
        if buy_purple == 1:
            screen.blit(purple_image, purple_rect)
            if is_purple == 1:
                screen.blit(check4, check4_rect)
        else:
            screen.blit(un_purple_image, un_purple_rect)
        #
        if buy_red == 1:
            screen.blit(red_image, red_rect)
            if is_red == 1:
                screen.blit(check5, check5_rect)
        else:
            screen.blit(un_red_image, un_red_rect)
        #
        if buy_yellow == 1:
            screen.blit(yellow_image, yellow_rect)
            if is_yellow == 1:
                screen.blit(check6, check6_rect)
        else:
            screen.blit(un_yellow_image, un_yellow_rect)
        if buy_tux == 1:
            screen.blit(tux_image, tux_rect)
            if is_tux == 1:
                screen.blit(check7, check7_rect)
        else:
            screen.blit(un_tux_image, un_tux_rect)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
