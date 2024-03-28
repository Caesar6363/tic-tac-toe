import random

# количество клеток
board_size = 3
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
steps = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


def play_board():
    # Игровое поле
    print('_' * 13)
    for i in range(len(board)):
        for j in range(len(board)):  # печать игрового поля
            print('|', board[i][j], end=' ')

        print("|\n" + '_' * 13)


def player_step(x: int, y: int) -> int | None:
    # Ход игрока
    if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == ' ':
        board[x - 1][y - 1] = 'X'
        steps.pop(steps.index((x - 1, y - 1)))
        return 1


def clean_last_step(x: int, y: int):
    steps.pop(steps.index((x, y)))  # удаление по индексу


def random_step_bot():
    # Ход бота
    coordinates = random.choice(steps)  # рандомные координаты
    board[coordinates[0]][coordinates[1]] = 'O'  # замена


def step_bot_line():
    # Проверка по строчкам
    for index, qwe in enumerate(board):
        if str(qwe).count('X') == 2 and not ''.join(qwe).isalpha():
            qwe[qwe.index(' ')] = 'O'
            clean_last_step(index, qwe.index('O'))
            return 1


def step_bot_columns():
    # Проверка по столбцам
    for i in range(len(board)):
        new = board[0][i] + board[1][i] + board[2][i]  # Объединяет все в одну строку
        if new.count('X') == 2 and not ''.join(new).isalpha():
            board[new.find(' ')][i] = 'O'  # Поиск пустой строки. [i] номер столбца
            clean_last_step(new.find(' '), i)
            return 1


def step_bot_diagonal():
    # Проверка на диагональ

    diagonal1 = ''
    diagonal2 = ''

    for i in range(len(board)):
        diagonal1 += board[i][i]
        diagonal2 += board[i][2 - i]
    if diagonal1.count('X') == 2 and not ''.join(diagonal1).isalpha():
        gh = diagonal1.index(' ')
        board[gh][gh] = 'O'
        clean_last_step(gh, gh)
        return 1

    if diagonal2.count('X') == 2 and not ''.join(diagonal2).isalpha():
        gh = diagonal2.index(' ')
        board[gh][2 - gh] = 'O'
        clean_last_step(gh, 2 - gh)
        return 1


def step_bot():
    if step_bot_line():
        return 1
    if step_bot_columns():
        return 1
    if step_bot_diagonal():
        return 1
    random_step_bot()


def check_win(symbol: str):
    for check in board:  # строки
        if str(check).count(symbol) == 3:
            return symbol

    for check in range(len(board)):  # столбцы
        new = board[0][check] + board[1][check] + board[2][check]  # Объединяет все в одну строку
        if new.count(symbol) == 3:
            return symbol

    diagonal1 = ''  # диагонали
    diagonal2 = ''

    for check in range(len(board)):
        diagonal1 += board[check][check]
        diagonal2 += board[check][2 - check]
    if diagonal1.count(symbol) == 3:
        return symbol

    if diagonal2.count(symbol) == 3:
        return symbol


def block():
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]  # углы

    if board[1][1] == 'X':
        block_bot = random.choice(corners)
        board[block_bot[0]][block_bot[1]] = 'O'
        steps.pop(steps.index((block_bot[0], block_bot[1])))

        return 1

    for corner in corners:
        if board[corner[0]][corner[1]] == 'X':
            board[1][1] = 'O'
            steps.pop(steps.index((1, 1)))

            return 1

    random_step_bot()


def start_game():
    # Вызов игры

    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 0

    while step < 5:

        if step < 5:

            index_line = input('Ход игрока ' + current_player + '. Выберите строку(стоп - выход с игры):')
            index_columns = input('Ход игрока ' + current_player + '. Выберите столбец(стоп - выход с игры):')

            if index_line == 'стоп' and index_columns == 'стоп':
                break

            if player_step(int(index_line), int(index_columns)):
                print("Вы сделали ход")
                play_board()
                step += 1

                if step == 1:
                    block()
                else:
                    step_bot()
                play_board()
            else:
                print("Не верный ход. Попробуй еще раз")

            if check_win('X'):
                print('Победитель - игрок Х')
                break
            elif check_win('O'):
                print('Победитель - игрок О')
                break
        if step >= 5:
            print('Ничья')
            break


print(f'Игра началась')
start_game()
