# Крестики-нолики
# Компьютер играет против пользователя
# Глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    """Вывод на экран инструкции для игрока."""
    print(
    """
    Добро пожаловать в игру!
    Ты и компьютер сыграете в крестики-нолики.
    Чтобы сделать ход, введи число от 0 до 8. Числа соответствуют полям, как показано ниже:

    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    
    Готов сразиться с искусственным интеллектом?\n    """
    )

def ask_yes_no(question):
    """Задает вопрос с ответом 'Да' или 'Нет'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Определяет очередность ходов."""
    go_first = ask_yes_no("Хочешь ходить первым? (y/n): ")
    if go_first == "y":
        print("\nЗначит играешь крестиками.")
        human = X
        computer = O
    else:
        print("\nИграешь ноликами.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Создает новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображает игровую доску на экране."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Создает список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5 ,8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Получает ход человека."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей.", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято, выбери другое.\n")
    return move

def computer_move(board, computer, human):
    """Делает ход компьютерного противника."""
    # Создадим рабочую копию доски, потому что функция будет менять некоторые значения в списке
    board = board[:]
    # Поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")

    for move in legal_moves(board):
        board[move] = computer
    # Если следующим ходом может победить компьютер, выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
    # Выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
    # Если следующим ходом может победить человек, блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
    # Выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY

    # Поскольку следующим ходом ни одна из сторон не победит, выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя."""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победа за ИИ!\n")
    elif the_winner == human:
        print("Победа за человеком!\n")
    elif the_winner == TIE:
        print("Ничья!\n")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# Запуск программы
main()
input("\n\nНажмите Enter, чтобы выйти.")
