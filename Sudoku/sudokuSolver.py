"""
Solving Sudoku

Possibly solve other than 9x9 matrix, but it takes too long for solving 16x16 matrix

Maybe there are better algorithms for solving larger than 9x9 matrix
"""

import numpy as np
from math import sqrt

# board = [[10, 0, 14, 0, 15, 0, 0, 0, 0, 0, 0, 0, 3, 0, 15, 8],
#          [15, 3, 8, 11, 2, 5, 10, 15, 0, 0, 6, 0, 0, 0, 9, 13],
#          [5, 13, 15, 12, 0, 1, 14, 0, 3, 0, 0, 10, 0, 0, 0, 0],
#          [0, 7, 0, 6, 8, 11, 0, 12, 0, 15, 13, 4, 14, 0, 0, 0],
#          [0, 0, 0, 0, 0, 14, 0, 13, 0, 8, 3, 6, 0, 14, 0, 0],
#          [15, 4, 0, 7, 1, 3, 10, 0, 12, 9, 0, 0, 6, 16, 0, 0],
#          [0, 0, 3, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0],
#          [6, 10, 2, 0, 0, 7, 15, 8, 1, 4, 14, 13, 0, 0, 0, 9],
#          [0, 0, 7, 0, 0, 0, 0, 0, 12, 0, 0, 0, 15, 9, 4, 3],
#          [0, 16, 4, 8, 3, 0, 6, 0, 0, 0, 7, 0, 1, 2, 0, 13],
#          [0, 0, 6, 0, 15, 0, 0, 7, 2, 0, 0, 0, 0, 14, 0, 0],
#          [13, 15, 10, 5, 11, 0, 0, 0, 0, 0, 9, 1, 0, 8, 0, 0],
#          [7, 6, 0, 0, 0, 15, 0, 0, 8, 0, 0, 0, 9, 5, 2, 11],
#          [4, 0, 5, 0, 14, 10, 0, 0, 0, 13, 0, 0, 0, 0, 16, 0],
#          [3, 0, 0, 15, 0, 8, 9, 0, 0, 5, 0, 16, 10, 0, 14, 1],
#          [14, 2, 0, 13, 6, 12, 5, 0, 0, 0, 0, 11, 0, 0, 0, 7]]

board = [[0, 0, 1, 0, 0, 5, 0, 0, 0],
         [8, 0, 0, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 1, 0, 9],
         [0, 5, 0, 0, 0, 0, 0, 0, 3],
         [0, 4, 0, 0, 0, 0, 0, 2, 5],
         [7, 6, 8, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 8, 0, 0, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 0],
         [0, 0, 0, 0, 6, 7, 5, 0, 0]]


def solver(board):
    sz = len(board)
    for row in range(sz):
        for col in range(sz):
            if (board[row][col] == 0):
                for i in range(1, sz+1):
                    if (validation(board, i, row, col)):
                        board[row][col] = i
                        solver(board)
                        board[row][col] = 0
                return
    print(np.matrix(board))


def validation(board, i, row, col):
    sz = len(board)
    for check in range(sz):
        if (board[check][col] == i or board[row][check] == i):
            return False

    b_sz = int(sqrt(sz))
    box_num_x = col // b_sz
    box_num_y = row // b_sz

    for y in range(b_sz * box_num_x, b_sz * box_num_x + b_sz):
        for x in range(b_sz * box_num_y, b_sz * box_num_y + b_sz):
            if (i == board[x][y]):
                return False
    return True


if (__name__ == "__main__"):
    solver(board)
