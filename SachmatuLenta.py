# Susikuriam lenta

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def display_board(board):
    print("   a b c d e f g h")
    print("   ----------------")
    for i, row in enumerate(board, start=1):
        print(f"{i} |{' '.join(row)}|")
    print("  ----------------")

def is_valid_move(board, start, end):
    piece = board[start[0]][start[1]]
    if piece == ' ':
        return False
    if start == end:
        return False
    if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] <8 and 0 <= end[1] < 8):
        return False
    return True

def make_move(board, start, end):
    piece = board[start[0]][start[1]]
    board[start[0]][start[1]] = " "
    board[end[0]][end[1]] = piece #atrinks figura kuri bus nurodyta pradineje padetyje, jeugu irasysim A2 --> pajudes i A2

def is_game_over(board):
    return False

while True:
    display_board(board)
    start = input("Enter start position (i.g.: 'a2'): ")
    end = input("Enter end position (i.g.: 'c4'): ")
    start = (int(start[1]) - 1, ord(start[0]) - ord('a')) #ord yra ascii reiksmes somboliai
    end = (int(end[1]) - 1, ord(end[0]) - ord('a'))

    if is_valid_move(board, start, end):
        make_move(board, start, end)
        if is_game_over(board):
            display_board(board)
            print("GAME OVER")
            break
    else:
        print("\n Invalid move, please try again!")
