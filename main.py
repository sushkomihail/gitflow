from logic import *
import pygame as pg
import sys


def interface(score):
    k_x, k_y = window_location()
    have_bon_im = have_bon_improve1()
    have_bon_del = have_bon_del1()
    font_bon = pg.font.SysFont('stxingkai', 32)
    font_exit = pg.font.SysFont('stxingkai', 20)
    text_exit = font_exit.render('Выйти с сохранением', True, BLACK)
    text_exit1 = font_exit.render('Выйти без сохранения', True, BLACK)
    text_im = font_bon.render('Бонусы', True, BLACK)
    title_rect = pg.Rect(k_x, k_y, width, size_rect + 50)

    bon_improve = pg.image.load('data/improve.jpg').convert_alpha()
    k_improve = font_bon.render(f' {have_bon_im}', True, BLACK)

    bon_del = pg.image.load('data/del.png').convert_alpha()
    k_del = font_bon.render(f' {have_bon_del}', True, BLACK)

    pg.draw.rect(screen, WHITE, title_rect)
    f = have_fon()
    if '1' in f:
        fon1 = pg.image.load('data/фон1.jpg')
    elif '2' in f:
        fon1 = pg.image.load('data/фон2.jpg')
    elif '3' in f:
        fon1 = pg.image.load('data/фон3.jpg')
    elif '4' in f:
        fon1 = pg.image.load('data/фон4.jpg')
    elif '5' in f:
        fon1 = pg.image.load('data/фон5.jpg')
    elif '6' in f:
        fon1 = pg.image.load('data/фон6.jpg')
    elif '7' in f:
        fon1 = pg.image.load('data/фон7.jpeg')
    x, y = window_location()
    x1 = (x + width // 2) * 2
    y1 = (y + height // 2) * 2
    screen.blit(pg.transform.scale(fon1, (x1, y1)), (0, 0))
    screen.fill(pg.Color(255, 255, 255), pg.Rect(10 + k_x, 10 + k_y, 430, 590))
    screen.fill(pg.Color(0, 0, 0), pg.Rect(10 + k_x, 150 + k_y, 430, 450))
    font = pg.font.SysFont('stxingkai', 70)
    font_score = pg.font.SysFont('stxingkai', 48)
    text_score = font_score.render('Счет: ', True, BLACK)
    score_value = font_score.render(f'{score}', True, BLACK)
    screen.blit(text_score, (20 + k_x, 80 + k_y))
    screen.blit(score_value, (130 + k_x, 80 + k_y))
    screen.blit(text_im, (272 + k_x, 20 + k_y))
    screen.blit(pg.transform.scale(bon_improve, (40, 40)), (250 + k_x, 70 + k_y))
    screen.blit(k_improve, (290 + k_x, 80 + k_y))
    screen.blit(pg.transform.scale(bon_del, (35, 35)), (330 + k_x, 70 + k_y))
    screen.blit(k_del, (360 + k_x, 80 + k_y))
    screen.blit(text_exit, (10 + k_x, 10 + k_y))
    screen.blit(text_exit1, (10 + k_x, 30 + k_y))
    print_board(board)
    for row in range(rects):
        for col in range(rects):
            value = board[row][col]
            text = font.render(f'{value}', True, BLACK)
            w = col * size_rect + (col + 1) * indent + k_x
            h = row * size_rect + (row + 1) * indent + size_rect + 50 + k_y
            pg.draw.rect(screen, COLORS[value], (w, h, size_rect, size_rect))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (size_rect - font_w) / 2
                text_y = h + (size_rect - font_h) / 2
                screen.blit(text, (text_x, text_y))


board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def init_cells(board):
    list_of_index = get_list_of_index(board)
    random.shuffle(list_of_index)
    random_number = list_of_index.pop()
    x, y = get_index_of_number(random_number)
    board = add_2_or_4(board, x, y)
    return board


COLORS = {
    0: (128, 128, 128),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 128, 255),
    32: (255, 0, 255),
    64: (128, 255, 255),
    128: (0, 255, 255),
    256: (0, 128, 255),
    512: (0, 0, 255),
    1024: (11, 218, 81),
    2048: (76, 187, 23)
}

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

rects = 4
size_rect = 100
indent = 10
width = 4 * size_rect + 5 * indent
height = 4 * size_rect + 5 * indent + 100
score = 0
best_score = best_score1()
count_of_games = count_of_games1()
is_not_play = True
home_page = None
game = False
count_of_tap = 0
count_of_tap1 = 0
print_board(board)
print(get_list_of_index(board))
hour_to_next = 2

pg.init()

def start_game():
    global best_score, gain, count, width, height, hour_to_next
    fon0 = pg.image.load('data/фон главный.jpg')
    x, y = window_location()
    x1 = (x + width // 2) * 2
    y1 = (y + height // 2) * 2
    screen.blit(pg.transform.scale(fon0, (x1, y1)), (0, 0))
    k_x, k_y = window_location()
    rect_back = pg.Rect(20 + k_x, 25 + k_y, 50, 50)
    new_med_score = medium_score(count_of_games)
    new_money = count_of_money(score)
    have_bon_im = have_bon_improve1()
    have_bon_del = have_bon_del1()
    img = pg.image.load('data/2048.png')
    lotery = pg.image.load('data/lotery.png').convert_alpha()
    play = pg.image.load('data/play.png')
    shop = pg.image.load('data/shop.png')
    stat = pg.image.load('data/stat.png')
    font = pg.font.SysFont('stxingkai', 60)
    font_money = pg.font.SysFont('stxingkai', 40)
    font_bon = pg.font.SysFont('stxingkai', 32)
    text_start = font.render('Welcome to', True, BLACK)
    rect_play = pg.Rect(140 + k_x, 250 + k_y, 170, 170)
    rect_shop = pg.Rect(10 + k_x, 500 + k_y, 100, 100)
    rect_lotery = pg.Rect(340 + k_x, 500 + k_y, 100, 100)
    rect_stat = pg.Rect(175 + k_x, 500 + k_y, 100, 100)
    global is_not_play
    while is_not_play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(event.pos):
                    is_not_play = False
                if rect_shop.collidepoint(event.pos):
                    text_shop = font.render('Магазин', True, BLACK)
                    money = pg.image.load('data/money.png').convert_alpha()
                    text_money = font_money.render(f': {new_money}', True, BLACK)
                    back = pg.image.load('data/back.png').convert_alpha()

                    bon_improve = pg.image.load('data/improve.jpg').convert_alpha()
                    text_improve = font_bon.render('Бонус улучшения', True, BLACK)
                    text_buy_improve = font_bon.render('Купить', True, BLACK)
                    rect_but_buy_improve = pg.Rect(40 + k_x, 425 + k_y, 150, 50)
                    k_improve = font_money.render(f' {have_bon_im}', True, BLACK)

                    bon_del = pg.image.load('data/del.png').convert_alpha()
                    text_del = font_bon.render('Бонус удаления', True, BLACK)
                    text_buy_del = font_bon.render('Купить', True, BLACK)
                    rect_but_buy_del = pg.Rect(265 + k_x, 425 + k_y, 150, 50)
                    k_del = font_money.render(f' {have_bon_del}', True, BLACK)

                    cost = pg.image.load('data/cost.png').convert_alpha()
                    cost_improve = font_bon.render('20', True, BLACK)
                    cost_del = font_bon.render('10', True, BLACK)

                    is_back = False
                    while not is_back:
                        new_money = count_of_money(score)
                        screen.blit(pg.transform.scale(fon0, (x1, y1)), (0, 0))
                        screen.fill(pg.Color(255, 255, 255), pg.Rect(10 + k_x, 10 + k_y, 430, 590))
                        screen.blit(pg.transform.scale(back, (50, 50)), (20 + k_x, 25 + k_y))
                        screen.blit(text_shop, (150 + k_x, 30 + k_y))
                        screen.blit(pg.transform.scale(money, (50, 50)), (20 + k_x, 100 + k_y))
                        screen.blit(text_money, (70 + k_x, 110 + k_y))

                        screen.blit(text_improve, (20 + k_x, 200 + k_y))
                        screen.blit(text_del, (260 + k_x, 200 + k_y))

                        screen.blit(pg.transform.scale(bon_improve, (80, 80)), (45 + k_x, 240 + k_y))
                        screen.blit(pg.transform.scale(bon_del, (80, 80)), (285 + k_x, 240 + k_y))

                        screen.blit(k_improve, (120 + k_x, 265 + k_y))
                        screen.blit(k_del, (360 + k_x, 265 + k_y))

                        screen.blit(pg.transform.scale(cost, (60, 60)), (45 + k_x, 330 + k_y))
                        screen.blit(cost_improve, (100 + k_x, 350 + k_y))
                        screen.blit(pg.transform.scale(cost, (60, 60)), (285 + k_x, 330 + k_y))
                        screen.blit(cost_del, (340 + k_x, 350 + k_y))
                        if new_money >= 20 and have_bon_im < 999:
                            screen.fill(pg.Color(50, 240, 50), pg.Rect(40 + k_x, 425 + k_y, 150, 50))
                            screen.blit(text_buy_improve, (75 + k_x, 440 + k_y))
                        if new_money >= 10 and have_bon_del < 999:
                            screen.fill(pg.Color(50, 240, 50), pg.Rect(265 + k_x, 425 + k_y, 150, 50))
                            screen.blit(text_buy_del, (300 + k_x, 440+ k_y))

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()
                                sys.exit(0)
                            elif event.type == pg.MOUSEBUTTONDOWN:
                                if rect_back.collidepoint(event.pos):
                                    is_back = True
                                    is_not_play = True
                                elif rect_but_buy_improve.collidepoint(event.pos):
                                    have_bon_im = have_bon_improve1()
                                    have_bon_del = have_bon_del1()
                                    buy_bon_improve(best_score, count_of_games, new_med_score, new_money, have_bon_im,
                                                    have_bon_del)
                                    have_bon_im = have_bon_improve1()
                                    k_improve = font_money.render(f' {have_bon_im}', True, BLACK)
                                    screen.fill(pg.Color(255, 255, 255), pg.Rect(85 + k_x, 250 + k_y, 100, 70))
                                    screen.blit(k_improve, (85 + k_x, 250 + k_y))
                                    screen.fill(pg.Color(255, 255, 255), pg.Rect(70 + k_x, 110 + k_y, 100, 50))
                                    new_money = count_of_money(score)
                                    text_money = font_money.render(f': {new_money}', True, BLACK)
                                    screen.blit(text_money, (70 + k_x, 110 + k_y))
                                elif rect_but_buy_del.collidepoint(event.pos):
                                    have_bon_im = have_bon_improve1()
                                    have_bon_del = have_bon_del1()
                                    buy_bon_del(best_score, count_of_games, new_med_score, new_money, have_bon_im,
                                                have_bon_del)
                                    have_bon_del = have_bon_del1()
                                    k_del = font_money.render(f' {have_bon_del}', True, BLACK)
                                    screen.fill(pg.Color(255, 255, 255), pg.Rect(325 + k_x, 250 + k_y, 100, 70))
                                    screen.blit(k_del, (325 + k_x, 250 + k_y))
                                    screen.fill(pg.Color(255, 255, 255), pg.Rect(70 + k_x, 110 + k_y, 100, 50))
                                    new_money = count_of_money(score)
                                    text_money = font_money.render(f': {new_money}', True, BLACK)
                                    screen.blit(text_money, (70 + k_x, 110 + k_y))
                        pg.display.update()
                if rect_lotery.collidepoint(event.pos):
                    text_lotery = font.render('Ежедневный сундук', True, BLACK)
                    back = pg.image.load('data/back.png').convert_alpha()
                    is_back_from_lotery = False
                    wheel = pg.image.load('data/chest.png').convert_alpha()
                    text_go_wheel = font_bon.render('Открыть сундук!', True, BLACK)
                    gain = ''
                    hour_to, minut_to = get_time_to_open()
                    if int(hour_to) > 0:
                        can_tap = False
                    else:
                        can_tap = True
                    if int(hour_to) > 0:
                        hour, minut = get_time()
                        time1 = int(hour + minut)
                        hour1, minut1 = new_time()
                        time2 = int(hour1 + minut1)
                        hour_to_chess = time1 - time2
                        print(time1, time2)
                        print(hour_to_chess)
                        if len(str(hour_to_chess)) < 4:
                            hour_to = str(hour_to_chess)[0]
                            minut_to = str(hour_to_chess)[1] + str(hour_to_chess)[2]
                        else:
                            hour_to = str(hour_to_chess)[0] + str(hour_to_chess)[1]
                            minut_to = str(hour_to_chess)[2] + str(hour_to_chess)[3]
                        load_time_to_open(hour_to, minut_to)
                    rect_go_wheel = pg.Rect(125 + k_x, 385 + k_y, 210, 80)
                    count = 0
                    was = False
                    while not is_back_from_lotery:
                        text_time = font_bon.render(f'Сундук через: {hour_to}:{minut_to}', True, BLACK)
                        screen.blit(pg.transform.scale(fon0, (x1, y1)), (0, 0))
                        screen.fill(pg.Color(255, 255, 255), pg.Rect(10 + k_x, 10 + k_y, 430, 590))
                        screen.blit(pg.transform.scale(back, (50, 50)), (20 + k_x, 25 + k_y))
                        screen.blit(text_lotery, (10 + k_x, 80 + k_y))
                        screen.blit(pg.transform.scale(wheel, (200, 200)), (125 + k_x, 150 + k_y))

                        screen.fill(pg.Color(150, 100, 30), pg.Rect(125 + k_x, 385 + k_y, 210, 80))
                        screen.fill(pg.Color(255, 255, 255), pg.Rect(130 + k_x, 390 + k_y, 200, 70))
                        screen.fill(pg.Color(150, 100, 30), pg.Rect(135 + k_x, 395 + k_y, 190, 60))
                        screen.fill(pg.Color(50, 180, 180), pg.Rect(140 + k_x, 400 + k_y, 180, 50))

                        screen.blit(text_go_wheel, (142 + k_x, 410 + k_y))

                        screen.blit(text_time, (130 + k_x, 470 + k_y))
                        if was:
                            pg.draw.rect(screen, WHITE, (50 + k_x, 500 + k_y, 350, 100))
                            k_improve = font_money.render(f'Новый игровой фон!', True, BLACK)
                            screen.blit(k_improve, (110 + k_x, 520 + k_y))

                        if gain == '' and count == 0:
                            pg.draw.rect(screen, WHITE, (50 + k_x, 500 + k_y, 350, 100))
                        elif gain == 'im':
                            pg.draw.rect(screen, WHITE, (50 + k_x, 500 + k_y, 350, 100))
                            bon_improve = pg.image.load('data/improve.jpg').convert_alpha()
                            k_improve = font_money.render(f'{count}', True, BLACK)
                            screen.blit(pg.transform.scale(bon_improve, (100, 100)),
                                        (180 + k_x, 480 + k_y))
                            screen.blit(k_improve, (295 + k_x, 510 + k_y))
                            load_to_file(best_score, count_of_games, new_med_score, new_money,
                                         have_bon_im + count, have_bon_del)
                        elif gain == 'del':
                            pg.draw.rect(screen, WHITE, (50 + k_x, 500 + k_y, 350, 100))
                            bon_del = pg.image.load('data/del.png').convert_alpha()
                            k_improve = font_money.render(f'{count}', True, BLACK)
                            screen.blit(pg.transform.scale(bon_del, (100, 100)),
                                        (180 + k_x, 480 + k_y))
                            screen.blit(k_improve, (295 + k_x, 510 + k_y))
                            load_to_file(best_score, count_of_games, new_med_score, new_money,
                                         have_bon_im, have_bon_del + count)
                        elif gain == 'fon' and not was:
                            n = new_fon()
                            was = True
                        pg.display.update()
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()
                                sys.exit(0)
                            elif event.type == pg.MOUSEBUTTONDOWN:
                                if rect_back.collidepoint(event.pos):
                                    is_back_from_lotery = True
                                    is_not_play = True
                                elif rect_go_wheel.collidepoint(event.pos) and can_tap:
                                    if can_tap:
                                        time()
                                    hour, minut = get_time()
                                    time1 = int(hour + minut)
                                    hour1, minut1 = new_time()
                                    time2 = int(hour1 + minut1)
                                    hour_to_chess = time1 - time2
                                    print(time1, time2)
                                    print(hour_to_chess)
                                    if len(str(hour_to_chess)) < 4:
                                        hour_to = str(hour_to_chess)[0]
                                        minut_to = str(hour_to_chess)[1] + str(hour_to_chess)[2]
                                    else:
                                        hour_to = str(hour_to_chess)[0] + str(hour_to_chess)[1]
                                        minut_to = str(hour_to_chess)[2] + str(hour_to_chess)[3]
                                    load_time_to_open(hour_to, minut_to)
                                    running = True
                                    x_pos = 100
                                    fps = 60
                                    move = - 10
                                    clock = pg.time.Clock()
                                    gain, count = prize()
                                    while running:
                                        screen.fill(BLACK)
                                        screen.blit(pg.transform.scale(wheel, (200, 200)), (x_pos + k_x, 100 + k_y))
                                        if move < 0:
                                            x_pos += 1
                                        else:
                                            if (move // 20) % 2 == 0:
                                                x_pos -= 1
                                            else:
                                                x_pos += 1
                                        move += 1
                                        clock.tick(fps)
                                        pg.display.flip()
                                        for event in pg.event.get():
                                            if event.type == pg.MOUSEBUTTONDOWN:
                                                running = False
                                                print(gain, count)
                        pg.display.update()
                pg.display.update()

                if rect_stat.collidepoint(event.pos):
                    best_score = best_score1()
                    games, med_score, money = stat1()
                    bon_im = have_bon_improve1()
                    bon_del = have_bon_del1()
                    font_stat = pg.font.SysFont('stxingkai', 40)
                    text_stat = font.render('Статистика', True, BLACK)
                    text_best_score = font_stat.render(f'Лучший результат: {best_score}', True, BLACK)
                    text_games = font_stat.render(f'Количество игр: {games}', True, BLACK)
                    text_med_score = font_stat.render(f'Средний результат: {med_score}', True, BLACK)
                    text_money = font_stat.render(f'Количество монет: {money}', True, BLACK)
                    text_bon_im = font_stat.render(f'Бонусов улучшения: {bon_im}', True, BLACK)
                    text_bon_del = font_stat.render(f'Бонусов удаления: {bon_del}', True, BLACK)
                    back = pg.image.load('data/back.png').convert_alpha()
                    is_back_from_stat = False
                    while not is_back_from_stat:
                        screen.blit(pg.transform.scale(fon0, (x1, y1)), (0, 0))
                        screen.fill(pg.Color(255, 255, 255), pg.Rect(10 + k_x, 10 + k_y, 430, 590))
                        screen.blit(pg.transform.scale(back, (50, 50)), (20 + k_x, 25 + k_y))
                        screen.blit(text_stat, (150 + k_x, 30 + k_y))
                        screen.blit(text_best_score, (20 + k_x, 130 + k_y))
                        screen.blit(text_games, (20 + k_x, 180 + k_y))
                        screen.blit(text_med_score, (20 + k_x, 230 + k_y))
                        screen.blit(text_money, (20 + k_x, 280 + k_y))
                        screen.blit(text_bon_im, (20 + k_x, 330 + k_y))
                        screen.blit(text_bon_del, (20 + k_x, 380 + k_y))
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()
                                sys.exit(0)
                            elif event.type == pg.MOUSEBUTTONDOWN:
                                if rect_back.collidepoint(event.pos):
                                    is_back_from_stat = True
                                    is_not_play = True
                        pg.display.update()
        screen.fill(pg.Color(255, 255, 255), pg.Rect(10 + k_x, 10 + k_y, 430, 590))
        screen.blit(pg.transform.scale(stat, (100, 100)), (175 + k_x, 500 + k_y))
        screen.blit(pg.transform.scale(lotery, (100, 100)), (340 + k_x, 500 + k_y))
        screen.blit(pg.transform.scale(shop, (100, 100)), (10 + k_x, 500 + k_y))
        screen.blit(pg.transform.scale(play, (170, 170)), (140 + k_x, 250 + k_y))
        screen.blit(pg.transform.scale(img, (150, 150)), (270 + k_x, 10 + k_y))
        screen.blit(text_start, (30 + k_x, 65 + k_y))
        pg.display.update()
    screen.fill(BLACK)


def end_of_game():
    global home_page, board, score, is_not_play
    k_x, k_y = window_location()
    home = pg.image.load('data/home.png').convert_alpha()
    rect_home = pg.Rect(125 + k_x, 315 + k_y, 325 + k_x, 515 + k_y)
    font = pg.font.SysFont('stxingkai', 70)
    font_score = pg.font.SysFont('stxingkai', 50)
    text_end = font.render('Конец игры!', True, BLACK)
    score_value = font_score.render(f'Вы набрали {score} очков', True, BLACK)
    text_win = font.render(f'Вы победили!', True, BLACK)
    decision = False
    while not decision:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if rect_home.collidepoint(event.pos):
                    home_page = None
                    decision = True
                    is_not_play = True
                    board = [
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ]
                    score = 0
        fon0 = pg.image.load('data/фон главный.jpg')
        x, y = window_location()
        x1 = (x + width // 2) * 2
        y1 = (y + height // 2) * 2
        screen.blit(pg.transform.scale(fon0, (x1, y1)), (0, 0))
        screen.fill(pg.Color(255, 255, 255), pg.Rect(10 + k_x, 10 + k_y, 430, 590))

        screen.blit(pg.transform.scale(home, (200, 200)), (125 + k_x, 315 + k_y))
        screen.blit(score_value, (20 + k_x, 230 + k_y))
        if check_win(board) == 1:
            screen.blit(text_win, (65 + k_x, 150 + k_y))
        else:
            screen.blit(text_end, (65 + k_x, 150 + k_y))
        pg.display.update()


def window_location():
    surface = pg.display.get_surface()
    x, y = surface.get_width(), surface.get_height()
    k_x = x // 2 - width // 2
    k_y = y // 2 - height // 2
    print(x, y)
    return k_x, k_y


def results():
    new_med_score = medium_score(count_of_games)
    new_money = count_of_money(score)
    return new_med_score, new_money


screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

pg.display.set_caption('2048')


def game_loop():
    global score, board, best_score, count_of_tap, count_of_tap1, is_not_play, in_game, count_of_games
    k_x, k_y = window_location()
    count_of_games += 1
    rect_but_buy_improve = pg.Rect(250 + k_x, 70 + k_y, 40, 40)
    rect_but_buy_del = pg.Rect(330 + k_x, 70 + k_y, 35, 35)
    new_med_score = medium_score(count_of_games)
    new_money = count_of_money(score)
    have_bon_im = have_bon_improve1()
    have_bon_del = have_bon_del1()
    init_cells(board)
    interface(score)
    pg.display.update()
    rect_yes = pg.Rect(10 + k_x, 10 + k_y, 140, 20)
    rect_no = pg.Rect(10 + k_x, 30 + k_y, 150, 20)
    board_move = False
    while (zero_on_board(board) or can_move(board)) and check_win(board) == 0:
        if count_of_tap == 1 and count_of_tap1 == 0:
            pg.draw.rect(screen, (30, 220, 30), (250 + k_x, 120 + k_y, 40, 10))
            pg.draw.rect(screen, (255, 255, 255), (330 + k_x, 120 + k_y, 40, 10))
        elif count_of_tap1 == 1 and count_of_tap == 0:
            pg.draw.rect(screen, (220, 30, 30), (330 + k_x, 120 + k_y, 40, 10))
            pg.draw.rect(screen, (255, 255, 255), (250 + k_x, 120 + k_y, 40, 10))
        elif count_of_tap1 == 0 and count_of_tap == 0:
            pg.draw.rect(screen, (255, 255, 255), (250 + k_x, 120 + k_y, 40, 10))
            pg.draw.rect(screen, (255, 255, 255), (330 + k_x, 120 + k_y, 40, 10))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if rect_but_buy_improve.collidepoint(event.pos):
                    if count_of_tap == 1:
                        count_of_tap = 0
                    elif count_of_tap == 0:
                        count_of_tap = 1
                    count_of_tap1 = 0
                elif event.pos[1] > 150 + k_y and count_of_tap == 1 and have_bon_im > 0:
                    x, y = event.pos
                    board, a = use_bon_improve(x, y, board, k_x, k_y)
                    if a:
                        have_bon_im -= 1
                        load_to_file(best_score, count_of_games, new_med_score, new_money, have_bon_im, have_bon_del)
                        interface(score)
                pg.display.update()

                if rect_but_buy_del.collidepoint(event.pos):
                    if count_of_tap1 == 1:
                        count_of_tap1 = 0
                    elif count_of_tap1 == 0:
                        count_of_tap1 = 1
                    count_of_tap = 0
                elif event.pos[1] > 150 + k_y and count_of_tap1 == 1 and have_bon_del != 0:
                    x, y = event.pos
                    board, a = use_bon_del(x, y, board, k_x, k_y)
                    if a:
                        have_bon_del -= 1
                        load_to_file(best_score, count_of_games, new_med_score, new_money, have_bon_im, have_bon_del)
                        interface(score)
                pg.display.update()

                if rect_yes.collidepoint(event.pos):
                    list_of_index = get_list_of_index(board)
                    if len(list_of_index) != 0:
                        is_not_play = True
                        start_game()
                        interface(score)

                elif rect_no.collidepoint(event.pos):
                    is_not_play = True
                    board = [
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ]
                    score = 0
                    count_of_tap1 = 0
                    count_of_tap = 0
                    init_cells(board)
                    start_game()
                    interface(score)

            elif event.type == pg.KEYDOWN:
                score1 = 0
                f = 0
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    board, score1, board_move = move_left(board)
                    f = 1
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    board, score1, board_move = move_right(board)
                    f = 1
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    board, score1, board_move = move_top(board)
                    f = 1
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    board, score1, board_move = move_down(board)
                    f = 1
                score += score1
                new_score = score
                if new_score > best_score:
                    best_score = new_score
                    load_to_file_for_check(best_score)
                if zero_on_board(board) and board_move and f == 1:
                    list_of_index = get_list_of_index(board)
                    random.shuffle(list_of_index)
                    random_number = list_of_index.pop()
                    x, y = get_index_of_number(random_number)
                    board = add_2_or_4(board, x, y)
                    print(f'Мы заполнили элемент под номером {random_number}')
                interface(score)
                pg.display.update()

    new_score1 = score
    load_to_file_for_check1(new_score1)
    new_med_score = medium_score(count_of_games)
    new_money = count_of_money(score)
    have_bon_im = have_bon_improve1()
    have_bon_del = have_bon_del1()
    load_to_file(best_score, count_of_games, new_med_score, new_money, have_bon_im, have_bon_del)


while True:
    if home_page is None:
        start_game()
    game_loop()
    end_of_game()
