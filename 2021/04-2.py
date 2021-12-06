import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()

    draw_numbers = [int(s) for s in lines[0].split(sep=',')]

    board = []
    boards = []
    count = 0

    for line in lines[2:]:
        if len(line) == 0:
            boards.append(board[:])
            board = []
            count = 0
        else:
            board.append(list(map(int, line.split())))
            count += 1

    boards.append(board[:5])

def get_result(board, drawn_numbers_loc):
    sum = 0
    for row in board:
        for elem in row:
            if elem not in drawn_numbers_loc:
                sum += elem

    return str(sum*drawn_numbers_loc[-1])

drawn_numbers = []

def find_bingo():
    for number in draw_numbers:
        drawn_numbers.append(number)
        for board in boards:

            #rows
            for row in board:
                if all(elem in drawn_numbers for elem in row):
                    if len(boards) == 1:
                        print(get_result(boards[0], drawn_numbers))
                        return
                    boards.remove(board)                    
            for i in range(len(board[0])):
                col = [row[i] for row in board]
                if all(elem in drawn_numbers for elem in col):
                    if len(boards) == 1:
                        print(get_result(boards[0], drawn_numbers))
                        return
                    if board in boards:
                        boards.remove(board)

find_bingo()