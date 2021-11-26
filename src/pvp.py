from pygame.image import load
from src.dino import *
from src.obstacle import *
from src.item import *
from src.interface import *
from src.option import *
from db.db_interface import InterfDB
from src.store import store
import src.setting as setting
import src.game
from src.game_value import *

db = InterfDB("db/score.db")


def pvp():
    global resized_screen
    global high_score
    global cacti
    global fire_cacti
    global pteras
    global clouds
    global stones
    global last_obstacle
    cacti = pygame.sprite.Group()
    fire_cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    stones = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()

    Stone.containers = stones
    Cactus.containers = cacti
    FireCactus.containers = fire_cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    start_menu = False
    game_over = False
    game_quit = False
    # HERE: REMOVE SOUND!!
    if setting.bgm_on:
        pygame.mixer.music.play(-1)  # 배경음악 실행

    # 
    player1_dino = Dino(dino_size[0], dino_size[1], type='original')
    player2_dino = Dino(dino_size[0], dino_size[1], type='2p_original', loc=1)

    # 플레이어1과 플레이어 2의 목숨 수
    life_1p = 5
    life_2p = 5
    heart_1p = HeartIndicator(life_1p)
    heart_2p = HeartIndicator(life_2p, loc=1)
    PVP_GAME_SPEED = 4
    new_ground = Ground(-1 * PVP_GAME_SPEED)
    new_ground = ImgBack(-1 * PVP_GAME_SPEED, "pvp_back")
    alpha_back, alpha_back_rect = alpha_image('alpha_back2.png', width + 20, height)
    alpha_back_rect.left = -20
    speed_indicator = Scoreboard(width * 0.12, height * 0.15)
    counter = 0
    # 게임 중  pause 상태
    paused = False
    # 게임 종료 후 노출 문구
    game_over_image, game_over_rect = load_image('game_over.png', 380, 100, -1)
    # 게임 후 버튼
    r_btn_restart, r_btn_restart_rect = load_image(*resize('btn_restart.png', 150, 80, -1))
    btn_restart, btn_restart_rect = load_image('btn_restart.png', 150, 80, -1)
    r_btn_exit, r_btn_exit_rect = load_image(*resize('btn_exit.png', 150, 80, -1))
    btn_exit, btn_exit_rect = load_image('btn_exit.png', 150, 80, -1)

    # 방향키 구현
    go_left_1p = False
    go_right_1p = False
    go_left_2p = False
    go_right_2p = False

    # 미사일 발사.
    space_go_1p = False
    m_list_1p = []
    bk_1p = 0

    space_go_2p = False
    m_list_2p = []
    bk_2p = 0

    while not game_quit:
        while start_menu:
            pass
        while not game_over:
            if pygame.display.get_surface() is None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        # 1p dino
                        if event.key == pygame.K_w:
                            # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player1_dino.rect.bottom == int(0.98 * height):
                                player1_dino.is_jumping = True
                                if pygame.mixer.get_init() is not None:
                                    jump_sound.play()
                                player1_dino.movement[1] = -1 * player1_dino.jump_speed

                        if event.key == pygame.K_s:
                            # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player1_dino.is_jumping and player1_dino.is_dead):
                                player1_dino.is_ducking = True

                        if event.key == pygame.K_a:
                            go_left_1p = True

                        if event.key == pygame.K_d:
                            go_right_1p = True

                        if event.key == pygame.K_LCTRL:
                            space_go_1p = True
                            bk_1p = 0

                        # 2p dino        
                        if event.key == pygame.K_UP:
                            # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player2_dino.rect.bottom == int(0.98 * height):
                                player2_dino.is_jumping = True
                                if pygame.mixer.get_init() is not None:
                                    jump_sound.play()
                                player2_dino.movement[1] = -1 * player2_dino.jump_speed

                        if event.key == pygame.K_DOWN:
                            # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player2_dino.is_jumping and player2_dino.is_dead):
                                player2_dino.is_ducking = True

                        if event.key == pygame.K_LEFT:
                            # print("left")
                            go_left_2p = True

                        if event.key == pygame.K_RIGHT:
                            # print("right")
                            go_right_2p = True

                        if event.key == pygame.K_p:
                            space_go_2p = True
                            bk_2p = 0

                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                            paused = src.game.pausing()

                    if event.type == pygame.KEYUP:
                        # 1p dino
                        if event.key == pygame.K_s:
                            player1_dino.is_ducking = False

                        if event.key == pygame.K_a:
                            go_left_1p = False

                        if event.key == pygame.K_d:
                            go_right_1p = False

                        if event.key == pygame.K_LCTRL:
                            space_go_1p = False

                        # 2p dino
                        if event.key == pygame.K_DOWN:
                            player2_dino.is_ducking = False

                        if event.key == pygame.K_LEFT:
                            go_left_2p = False

                        if event.key == pygame.K_RIGHT:
                            go_right_2p = False

                        if event.key == pygame.K_p:
                            space_go_2p = False

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)
            if not paused:



                if go_left_1p:
                    if player1_dino.rect.left < 0:
                        player1_dino.rect.left = 0
                    else:
                        player1_dino.rect.left = player1_dino.rect.left - PVP_GAME_SPEED

                if go_right_1p:
                    if player1_dino.rect.right > width / 2:
                        player1_dino.rect.right = width / 2
                    else:
                        player1_dino.rect.left = player1_dino.rect.left + PVP_GAME_SPEED

                if space_go_1p and (int(bk_1p % 15) == 0):
                    # print(bk)
                    missile_1p = Obj()

                    # 디노의 종류에 따라 다른 총알이 나가도록 합니다.
                    if player1_dino.type == 'RED':
                        missile_1p.put_img("./sprites/black_bullet.png")
                        missile_1p.change_size(10, 10)
                    elif player1_dino.type == 'YELLOW':
                        missile_1p.put_img("./sprites/blue_bullet.png")
                        missile_1p.change_size(10, 10)
                    elif player1_dino.type == 'ORANGE':
                        missile_1p.put_img("./sprites/blue_bullet.png")
                        missile_1p.change_size(10, 10)
                    elif player1_dino.type == 'PURPLE':
                        missile_1p.put_img("./sprites/pink_bullet.png")
                        missile_1p.change_size(15, 5)
                    elif player1_dino.type == 'PINK':
                        missile_1p.put_img("./sprites/heart_bullet.png")
                        missile_1p.change_size(10, 10)
                    else:
                        missile_1p.put_img("./sprites/red_bullet.png")
                        missile_1p.change_size(10, 10)

                    if not player1_dino.is_ducking:
                        missile_1p.x = round(player1_dino.rect.centerx)
                        missile_1p.y = round(player1_dino.rect.top * 1.035)

                    if player1_dino.is_ducking:
                        missile_1p.x = round(player1_dino.rect.centerx)
                        missile_1p.y = round(player1_dino.rect.centery * 1.01)
                    missile_1p.move = 15
                    m_list_1p.append(missile_1p)
                bk_1p = bk_1p + 1
                d_list_1p = []

                for i in range(len(m_list_1p)):
                    m = m_list_1p[i]
                    m.x += m.move
                    if m.x > width:
                        d_list_1p.append(i)

                # 1p의 미사일이 2p를 맞추었을 때
                if len(m_list_1p) == 0:
                    pass
                else:
                    for m_1p in m_list_1p:
                        if (m_1p.x >= player2_dino.rect.left) and (m_1p.x <= player2_dino.rect.right) and (
                                m_1p.y > player2_dino.rect.top) and (m_1p.y < player2_dino.rect.bottom):
                            life_2p -= 1
                            if life_2p == 0:
                                player2_dino.is_dead = True
                            m_list_1p.remove(m_1p)

                d_list_1p.reverse()
                for d in d_list_1p:
                    del m_list_1p[d]

                if go_left_2p:
                    if player2_dino.rect.left < width/2:
                        player2_dino.rect.left = width/2
                    else:
                        player2_dino.rect.left = player2_dino.rect.left - PVP_GAME_SPEED

                if go_right_2p:
                    if player2_dino.rect.right > width:
                        player2_dino.rect.right = width
                    else:
                        player2_dino.rect.left = player2_dino.rect.left + PVP_GAME_SPEED

                if space_go_2p and (int(bk_2p % 15) == 0):
                    # print(bk)
                    missile_2p = Obj()

                    # 디노의 종류에 따라 다른 총알이 나가도록 합니다.
                    if player2_dino.type == 'RED':
                        missile_2p.put_img("./sprites/black_bullet.png")
                        missile_2p.change_size(10, 10)
                    elif player2_dino.type == 'YELLOW':
                        missile_2p.put_img("./sprites/blue_bullet.png")
                        missile_2p.change_size(10, 10)
                    elif player2_dino.type == 'ORANGE':
                        missile_2p.put_img("./sprites/blue_bullet.png")
                        missile_2p.change_size(10, 10)
                    elif player2_dino.type == 'PURPLE':
                        missile_2p.put_img("./sprites/pink_bullet.png")
                        missile_2p.change_size(15, 5)
                    elif player2_dino.type == 'PINK':
                        missile_2p.put_img("./sprites/heart_bullet.png")
                        missile_2p.change_size(10, 10)
                    else:
                        missile_2p.put_img("./sprites/red_bullet.png")
                        missile_2p.change_size(10, 10)

                    if not player2_dino.is_ducking:
                        missile_2p.x = round(player2_dino.rect.centerx)
                        missile_2p.y = round(player2_dino.rect.top * 1.035)

                    if player2_dino.is_ducking:
                        missile_2p.x = round(player2_dino.rect.centerx)
                        missile_2p.y = round(player2_dino.rect.centery * 1.01)
                    missile_2p.move = 15
                    m_list_2p.append(missile_2p)
                bk_2p = bk_2p + 1
                d_list_2p = []

                for i in range(len(m_list_2p)):
                    m = m_list_2p[i]
                    m.x -= m.move
                    if m.x > width:
                        d_list_2p.append(i)

                # 2p의 미사일이 1p를 맞추었을 때
                if len(m_list_2p) == 0:
                    pass
                else:
                    for m_2p in m_list_2p:
                        if (m_2p.x >= player1_dino.rect.left) and (m_2p.x <= player1_dino.rect.right) and (
                                m_2p.y > player1_dino.rect.top) and (m_2p.y < player1_dino.rect.bottom):
                            life_1p -= 1
                            if life_1p == 0:
                                player1_dino.is_dead = True
                            m_list_2p.remove(m_2p)

                d_list_2p.reverse()
                for d in d_list_2p:
                    del m_list_2p[d]

                player1_dino.update('pvp')
                player2_dino.update('pvp')

                # new_ground.update()
                speed_indicator.update(PVP_GAME_SPEED - 3)
                heart_1p.update(life_1p)
                heart_2p.update(life_2p)

                if pygame.display.get_surface() is not None:
                    screen.fill(background_col)
                    new_ground.draw()
                    screen.blit(alpha_back, alpha_back_rect)
                    pygame.draw.line(screen, black, [width/2,0],[width/2,height],3)

                    heart_1p.draw()
                    heart_2p.draw()

                    for m in m_list_1p:
                        m.show()

                    for m in m_list_2p:
                        m.show()
                player1_dino.draw()
                player2_dino.draw()
                display_obstacle(player1_dino, counter, "left")
                display_obstacle(player2_dino, counter, "right")
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
                clock.tick(FPS)

                if player1_dino.is_dead or player2_dino.is_dead:
                    game_over = True
                    pygame.mixer.music.stop()

            counter += 1


        if game_quit:
            break

        while game_over:
            if pygame.display.get_surface() is None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            game_quit = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # game_over = False
                        # game_quit = True
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            x, y = event.pos
                            if r_btn_restart_rect.collidepoint(x, y):
                                pvp()

                            if r_btn_exit_rect.collidepoint(x, y):
                                src.game.intro_screen()

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)
                r_btn_restart_rect.centerx, r_btn_restart_rect.centery = resized_screen.get_width() * 0.25, resized_screen.get_height() * 0.6
                r_btn_exit_rect.centerx, r_btn_exit_rect.centery = resized_screen.get_width() * 0.75, resized_screen.get_height() * 0.6
                disp_pvp_gameover_buttons(btn_restart, btn_exit)
                disp_pvp_winner_loser(player1_dino)

                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            if pygame.display.get_surface() is not None:
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()


def display_obstacle(dino, counter, moving):
    global cacti
    global fire_cacti
    global pteras
    global clouds
    global stones
    global last_obstacle

    for s in stones:
        if not dino.collision_immune:
            if pygame.sprite.collide_mask(dino, s):
                dino.collision_immune = True
                collision_time = pygame.time.get_ticks()
                if pygame.mixer.get_init() is not None:
                    die_sound.play()

    for c in cacti:
        if not dino.collision_immune:
            if pygame.sprite.collide_mask(dino, c):
                dino.collision_immune = True
                collision_time = pygame.time.get_ticks()
                if pygame.mixer.get_init() is not None:
                    die_sound.play()

        # elif not dino.is_super:
        #     immune_time = pygame.time.get_ticks()
        #     if immune_time - collision_time > collision_immune_time:
        #         dino.collision_immune = False

    for f in fire_cacti:
        if not dino.collision_immune:
            if pygame.sprite.collide_mask(dino, f):
                dino.collision_immune = True
                collision_time = pygame.time.get_ticks()
                if pygame.mixer.get_init() is not None:
                    die_sound.play()

        # elif not dino.is_super:
        #     immune_time = pygame.time.get_ticks()
        #     if immune_time - collision_time > collision_immune_time:
        #         dino.collision_immune = False

    for p in pteras:
        if not dino.collision_immune:
            if pygame.sprite.collide_mask(dino, p):
                dino.collision_immune = True
                dino.decrease_life()
                collision_time = pygame.time.get_ticks()
                if dino.is_life_zero():
                    dino.is_dead = True
                if pygame.mixer.get_init() is not None:
                    die_sound.play()
        # elif not dino.is_super:
        #     immune_time = pygame.time.get_ticks()
        #     if immune_time - collision_time > collision_immune_time:
        #         dino.collision_immune = False

    if len(cacti) < 1:
        if len(cacti) == 0:
            last_obstacle.empty()
            last_obstacle.add(Cactus(PVP_GAME_SPEED, object_size[0], object_size[1], moving=moving))
        else:
            for l in last_obstacle:
                if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL) == MAGIC_NUM:
                    last_obstacle.empty()
                    last_obstacle.add(Cactus(PVP_GAME_SPEED, object_size[0], object_size[1], moving=moving))

    # if len(fire_cacti) < 2:
    #     for l in last_obstacle:
    #         if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL * 5) == MAGIC_NUM:
    #             last_obstacle.empty()
    #             last_obstacle.add(fire_cacti(PVP_GAME_SPEED, object_size[0], object_size[1]))

    if len(stones) < 1:
        for l in last_obstacle:
            if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(STONE_INTERVAL * 3) == MAGIC_NUM:
                last_obstacle.empty()
                last_obstacle.add(Stone(PVP_GAME_SPEED, object_size[0], object_size[1], moving=moving))

    if len(pteras) == 0 and random.randrange(PTERA_INTERVAL) == MAGIC_NUM and counter > PTERA_INTERVAL:
        print("???")
        # for l in last_obstacle:
        #     print("!!!")
        #     if l.rect.right < OBJECT_REFRESH_LINE:
        last_obstacle.empty()
        last_obstacle.add(Ptera(PVP_GAME_SPEED, ptera_size[0], ptera_size[1], moving=moving))

    cacti.update()
    fire_cacti.update()
    stones.update()
    pteras.update()

    cacti.draw(screen)
    stones.draw(screen)
    fire_cacti.draw(screen)
    pteras.draw(screen)