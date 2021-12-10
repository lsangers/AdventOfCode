import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    board = list(map(lambda s: list(map(int, list(s))), f.read().splitlines()))

max_row = len(board)
max_col = len(board[0])

risk_level = 0

def get_neighbors(row, col):
    n = []

    if(row > 0):
        n.append((row-1,col))
    if(row+1 < max_row):
        n.append((row+1,col))

    if(col > 0):
        n.append((row,col-1))
    if(col+1 < max_col):
        n.append((row,col+1))


    return n

for i, row in enumerate(board):
    for j, val in enumerate(row):
        neighbors = [board[r][c] for r,c in get_neighbors(i,j)]

        if all([val < elem for elem in neighbors ]):
            risk_level += 1 + val

print(risk_level)