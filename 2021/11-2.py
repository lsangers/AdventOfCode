import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(lambda s: list(map(lambda elem: int(elem), list(s))), lines))


board = lines[:]

done = False
step_count = 0

while not done:
    step_count += 1
    flashed = []

    for r, row in enumerate(board):
        for c, elem in enumerate(row):
            board[r][c] += 1
            if board[r][c] > 9:
                flashed.append((r, c))

    for location in flashed:
        neighbors = [(r,c) for r in range(max(location[0]-1, 0), min(location[0]+2, 10)) for c in range(max(location[1]-1, 0), min(location[1]+2, 10))]

        for loc in neighbors:
            board[loc[0]][loc[1]] += 1
            if loc not in flashed and board[loc[0]][loc[1]] > 9:
                flashed.append(loc)
    
    for location in flashed:
        board[location[0]][location[1]] = 0

    if len(flashed) == 100:
        done = True







print(step_count)