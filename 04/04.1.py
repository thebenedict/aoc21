#!/usr/bin/env/python

BOARD_DIMENSION = 5
MARK = -1

def main():
    with open("input.txt") as infile:
        numbers_line = infile.readline()
        numbers = [int(n) for n in numbers_line.split(",")]

        boards = []
        board = []
        for line in infile.readlines():
            if line == "\n":
                if len(board):
                    boards.append(board)
                board = []
            else:
                board_row = [int(n) for n in line.split()]
                board.append(board_row)
        boards.append(board)

        for number in numbers:
            for board in boards:
               winner, last_called = mark_board(board, number)
               if winner:
                   pp(board)
                   print(score_board(board, last_called))
                   return

def mark_board(board, number):
    winner = False
    for i, row in enumerate(board):
        try:
            idx = row.index(number)
            row[idx] = MARK
            winner = check_for_win(board, i, idx)
        except ValueError:
            pass
    return winner, number

def check_for_win(board, row, col):
    row_win = True
    col_win = True

    for i in range(BOARD_DIMENSION):
        if board[i][col] != MARK:
            row_win = False
    
    for i in range(BOARD_DIMENSION):
        if board[row][i] != MARK:
            col_win = False

    return row_win or col_win

def score_board(board, last_called):
    score = 0
    for row in board:
        for num in row:
            score += num if num != -1 else 0
    return score * last_called

def pp(board):
    for row in board:
        print(row)
        
if __name__ == "__main__":
    main()
