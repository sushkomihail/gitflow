import random
import copy
import datetime

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
time_bon_im = 0
time_bon_del = 0


def load_time_to_open(hour_to, minut_to):
    f = open('time_to_open.txt', 'w')
    f.write(hour_to + '\n')
    f.write(minut_to + '\n')


def get_time_to_open():
    f = open('time_to_open.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    hour_to = s[0]
    minut_to = s[1]
    return hour_to, minut_to


def new_time():
    time_now = datetime.datetime.now().time()
    time = str(time_now)
    list1 = time.split(':')
    hour1 = list1[0]
    minut1 = list1[1]
    return hour1, minut1


def get_time():
    f = open('time.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    hour = s[0]
    minut = s[1]
    return hour, minut


def time():
    time_now = datetime.datetime.now().time()
    time = str(time_now)
    list1 = time.split(':')
    hour = list1[0]
    hour1 = int(hour) + 2
    minut = list1[1]
    f = open('time.txt', 'w')
    f.write(str(hour1) + '\n')
    f.write(minut + '\n')


def have_fon():
    f = open('have_fon.txt', 'r').readlines()
    return f[0][0]


def new_fon():
    c = ['1', '2', '3', '4', '5', '6', '7']
    n = random.choice(c)
    f = open('have_fon.txt', 'w')
    f.write(n)
    return n


def prize():
    variant = ('fon', 'im', 'im', 'im', 'del', 'del', 'del')
    gain = random.choice(variant)
    count = random.randint(1, 10)
    return gain, count


def max_value(board):
    max = 0
    for i in board:
        for g in i:
            if g > max:
                max = g
    return max


def ne_0(board):
    kol = 0
    for i in board:
        for g in i:
            if g != 0:
                kol += 1
    return kol


def print_board(board):
    for cell in board:
        print(*cell)
    print('-' * 10)


def get_list_of_index(board):
    numbers = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                num = get_number_of_index(i, j)
                numbers.append(num)
    return numbers


def get_index_of_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def get_number_of_index(i, j):
    return i * 4 + j + 1


def add_2_or_4(board, x, y):
    if random.random() <= 0.75:
        board[x][y] = 2
    else:
        board[x][y] = 4
    return board


def zero_on_board(board):
    for row in board:
        if 0 in row:
            return True
    return False


def can_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[i][j] == board[i + 1][j]:
                return True
    return board[3][3] == board[2][3] or board[3][3] == board[3][2]


def load_to_file(best_score, count_of_games, new_med_score, new_money, have_bon_im, have_bon_del):
    f = open('stat.txt', 'w')
    f.write(f'Лучший результат: {best_score}' + '\n')
    f.write(f'Количество игр: {count_of_games}' + '\n')
    f.write(f'Средний результат: {new_med_score}' + '\n')
    f.write(f'Количество монет: {new_money}' + '\n')
    f.write(f'Бонусов улучшения: {have_bon_im}' + '\n')
    f.write(f'Бонусов удаления: {have_bon_del}' + '\n')
    f.close()


def load_to_file_for_check(best_score):
    f = open('best_score.txt', 'w')
    f.write(str(best_score))


def load_to_file_for_check1(new_score1):
    score_for_check = score_for_check1()
    score_for_check += new_score1
    f = open('all_score.txt', 'w')
    f.write(str(score_for_check))


def reset_stat():
    f = open('stat.txt', 'w')
    f.write(f'Лучший результат: {0}' + '\n')
    f.write(f'Количество игр: {0}' + '\n')
    f.write(f'Средний результат: {0}' + '\n')
    f.write(f'Количество монет: {0}' + '\n')
    f.write(f'Бонусов улучшения: {0}' + '\n')
    f.write(f'Бонусов удаления: {0}' + '\n')
    f.close()


def reset_stat1():
    f = open('best_score.txt', 'w')
    f.write(str(0))


def reset_stat2():
    f = open('all_score.txt', 'w')
    f.write(str(0))


def best_score1():
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[0].split(' ')
    best_score = int(n[-1])
    return best_score


def best_score_for_check1():
    f = open('best_score.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    best_score_for_check = int(s[0])
    return best_score_for_check


def score_for_check1():
    f = open('all_score.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    score_for_check = int(s[0])
    return score_for_check


def medium_score(count_of_games):
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[2].split(' ')
    med_score = int(n[-1])
    best_score_for_check = best_score_for_check1()
    score_for_check = score_for_check1()
    if med_score == 0:
        new_med_score = best_score_for_check
    else:
        new_med_score = score_for_check // count_of_games
    return new_med_score


def count_of_money(score):
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[3].split(' ')
    money = int(n[-1])
    new_money = money + score // 100
    return new_money


def count_of_games1():
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[1].split(' ')
    count_of_games = int(n[-1])
    return count_of_games


def have_bon_improve1():
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[4].split(' ')
    have_bon_im = int(n[-1])
    return have_bon_im


def have_bon_del1():
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[5].split(' ')
    have_bon_del = int(n[-1])
    return have_bon_del


def stat1():
    f = open('stat.txt')
    s = []
    for i in f:
        s.append(i.rstrip('\n'))
    n = s[1].split(' ')
    n1 = s[2].split(' ')
    n2 = s[3].split(' ')
    games = int(n[-1])
    med_score = int(n1[-1])
    money = int(n2[-1])
    return games, med_score, money


def buy_bon_improve(best_score, count_of_games, new_med_score, new_money, have_bon_im, have_bon_del):
    if new_money >= 20:
        f = open('stat.txt', 'w')
        new_b_im = have_bon_im + 1
        new_m = new_money - 20
        f.write(f'Лучший результат: {best_score}' + '\n')
        f.write(f'Количество игр: {count_of_games}' + '\n')
        f.write(f'Средний результат: {new_med_score}' + '\n')
        f.write(f'Количество монет: {new_m}' + '\n')
        f.write(f'Бонусов улучшения: {new_b_im}' + '\n')
        f.write(f'Бонусов удаления: {have_bon_del}' + '\n')
        f.close()
    else:
        pass


def buy_bon_del(best_score, count_of_games, new_med_score, new_money, have_bon_im, have_bon_del):
    if new_money >= 10:
        f = open('stat.txt', 'w')
        new_b_del = have_bon_del + 1
        new_m = new_money - 10
        f.write(f'Лучший результат: {best_score}' + '\n')
        f.write(f'Количество игр: {count_of_games}' + '\n')
        f.write(f'Средний результат: {new_med_score}' + '\n')
        f.write(f'Количество монет: {new_m}' + '\n')
        f.write(f'Бонусов улучшения: {have_bon_im}' + '\n')
        f.write(f'Бонусов удаления: {new_b_del}' + '\n')
        f.close()
    else:
        pass


def use_bon_improve(x, y, board, k_x, k_y):
    y -= (150 + k_y)
    x -= k_x
    a = False
    if x % 110 > 10 and y % 110 > 10:
        c_x = ((x - 1) // 110)
        c_y = ((y - 1) // 110)
        m = max_value(board)
        if board[c_y][c_x] != 0 and board[c_y][c_x] < m:
            board[c_y][c_x] = board[c_y][c_x] * 2
            print(c_y, c_x)
            print(board)
            a = True
    return board, a


def use_bon_del(x, y, board, k_x, k_y):
    y -= (150 + k_y)
    x -= k_x
    a = False
    if x % 110 > 10 and y % 110 > 10:
        c_x = ((x - 1) // 110)
        c_y = ((y - 1) // 110)
        k = ne_0(board)
        if board[c_y][c_x] != 0 and k > 1:
            board[c_y][c_x] = 0
            print(c_y, c_x)
            print(board)
            a = True
    return board, a


def check_win(board):
    for row in board:
        if 2048 in row:
            return 1
    return 0


def move_left(board):
    old_board = copy.deepcopy(board)
    score1 = 0
    for row in board:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j + 1] != 0:
                board[i][j] *= 2
                score1 += board[i][j]
                board[i].pop(j + 1)
                board[i].append(0)
    return board, score1, not old_board == board


def move_right(board):
    old_board = copy.deepcopy(board)
    score1 = 0
    for row in board:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if board[i][j] == board[i][j - 1] and board[i][j - 1] != 0:
                board[i][j] *= 2
                score1 += board[i][j]
                board[i].pop(j - 1)
                board[i].insert(0, 0)
    return board, score1, not old_board == board


def move_top(board):
    old_board = copy.deepcopy(board)
    score1 = 0
    board2 = []
    board3 = []
    mass2 = []
    mass = []
    s = 0
    n = 0
    for _ in range(4):
        for row in board:
            mass.append(row[s])
        board2.append(mass)
        mass = []
        s += 1
    for row in board2:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if board2[i][j] == board2[i][j + 1] and board2[i][j + 1] != 0:
                board2[i][j] *= 2
                score1 += board2[i][j]
                board2[i].pop(j + 1)
                board2[i].append(0)
    for _ in range(4):
        for row in board2:
            mass2.append(row[n])
        board3.append(mass2)
        mass2 = []
        n += 1
    return board3, score1, not old_board == board3


def move_down(board):
    old_board = copy.deepcopy(board)
    score1 = 0
    board2 = []
    board3 = []
    mass2 = []
    mass = []
    s = 0
    n = 0
    for _ in range(4):
        for row in board:
            mass.append(row[s])
        board2.append(mass)
        mass = []
        s += 1
    for row in board2:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if board2[i][j] == board2[i][j - 1] and board2[i][j - 1] != 0:
                board2[i][j] *= 2
                score1 += board2[i][j]
                board2[i].pop(j - 1)
                board2[i].insert(0, 0)
    for _ in range(4):
        for row in board2:
            mass2.append(row[n])
        board3.append(mass2)
        mass2 = []
        n += 1
    return board3, score1, not old_board == board3