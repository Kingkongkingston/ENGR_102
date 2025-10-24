# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kingston Alexander
#               Maya Ayoubi
#               Divyamaukthika Challa
#               Gia Huynh
# Section:      509
# Assignment:   Go Moves
# Date:         08/10/2025

BOARD_SIZE = 9
BLACK_STONE = 'B'
WHITE_STONE = 'W'
EMPTY = '.'


def initialize_board():
    board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            row.append(EMPTY)
        board.append(row)
    return board


def display_board(board):
    for row in board:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)


def parse_move_input(s):
    parts = s.split(',')
    if len(parts) != 2:
        return None
    row = int(parts[0])
    col = int(parts[1])
    return row, col


def is_valid_placement(board, row, col):
    if row < 0 or row >= BOARD_SIZE:
        return False
    if col < 0 or col >= BOARD_SIZE:
        return False
    if board[row][col] != EMPTY:
        return False
    return True


def place_stone(board, row, col, player):
    if player == 'Black':
        board[row][col] = BLACK_STONE
    else:
        board[row][col] = WHITE_STONE


def switch_player(player):
    if player == 'Black':
        return 'White'
    else:
        return 'Black'


board = initialize_board()
current_player = 'Black'

while True:
    display_board(board)
    move_input = input(
        current_player + "'s turn. Enter move (row,column) or stop: ")
    if move_input == 'stop':
        break
    move = parse_move_input(move_input)
    if move == None:
        print("Invalid input. Try again.")
        continue
    row = move[0]
    col = move[1]
    if not is_valid_placement(board, row, col):
        print("Invalid move. Try again.")
        continue
    place_stone(board, row, col, current_player)
    current_player = switch_player(current_player)
