import random


X = 'X'
O = 'O'

board = [' ' for x in range(10)]

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#def printBoard(board):
#    print(board['1'] + '  |'+board['2']+'  |'+board['3'])
#   print('---|---|---')
#    print(board['4'] + '  |'+board['5']+'  |' + board['6'])
#    print('---|---|---')
#    print(board['7'] + '  |'+board['8']+'  |' + board['9'])

printBoard(board)

def locuri_libere(board):
    result = []
    for i, j in enumerate(board):
        if j == ' ':
            result.append(i)
    return result

def winner(state, player):
    win_state = [
        [state[1], state[2], state[3]]
        [state[4], state[5], state[6]]
        [state[7], state[8], state[9]]
        [state[1], state[4], state[7]]
        [state[2], state[5], state[8]]
        [state[3], state[6], state[9]]
        [state[1], state[5], state[9]]
        [state[3], state[5], state[7]]
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    return winner(state, "X") or winner(state, "0")


def human_turn(board):
    depth = len(locuri_libere(board))
    if depth == 0 or game_over(board):
        return
    move = -1
    while move < 1 or move > 9:
        print("Este tura ta")
        printBoard(board)
        move = int(input("Introdu numarul corespunzator pozitiei dorite (1-9): "))
        if move <= 9 and move >= 1:
            if board[move-1] == " ":
                move -= 1
                board[move] = "X"
                printBoard(board)
                return
            else:
                print("Pozitia aleasa este ocupata. Alege un alt numar: ")
                move = -1
        else:
            print("Pozitia aleasa nu exista. Alege un alt numar: ")
            move = -1


def alegere_mutare(board, depth, player):
        depth = len(locuri_libere(board))
        move = -1
        mutari_posibile = locuri_libere(board)
        alegere_colturi = []
        alegere_margini = []
        if player == "0":
            if 5 in mutari_posibile:
                move = 5
                return move
            for i in mutari_posibile:
                if i in [1, 3, 7, 9]:
                    alegere_colturi.append(i)
            if len(alegere_colturi) > 0:
                move = random.choice(alegere_colturi)
                return move
            for i in mutari_posibile:
                if i in [2, 4, 6, 8]:
                    alegere_margini.append(i)
            if len(alegere_margini) > 0:
                move = random.choice(alegere_margini)
            return move


def computer_trun(board):
    depth = len(locuri_libere(board))
    if depth == 0 or game_over(board):
        return
    print("Tura calculatorului: ")
    move = alegere_mutare(board, depth, '0')
    board[move[0]] = "0"
    printBoard(board)


def functie_main():
    while len(locuri_libere(board)>0) and not game_over(board):
        human_turn(board)
        computer_trun()
    if winner(board, "X"):
        print("Ai castigat!")
        return 0
    elif winner(board, "0"):
        print("Ai piedut!")
        return 0
    else:
        print("Remiza")
