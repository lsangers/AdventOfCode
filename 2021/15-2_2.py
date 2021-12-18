import os
import sys
import timeit

filename = __file__[:-7] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(lambda s: list(map(lambda elem: int(elem), list(s))), lines))

small_board = lines[:]

def get_val(elem, i):
    while elem + i > 9:
        i -= 9
    return elem+i

tmp_board = []
for line in small_board:
    new_row = []
    for i in range(5):
        for elem in line:
            new_row.append(get_val(elem, i))
    tmp_board.append(new_row)


board = []

for i in range(5):
    board.extend(
        list(map(lambda row: 
            list(map(
                lambda x: get_val(x, i)
                , row))
            , tmp_board[:])))



max_row = len(board)
max_col = len(board[0])

fScore = [[99999999 for _ in range(max_col)] for _ in range(max_row)]

def get_neighbors(node, score):
    (row, col) = node
    n = []    

    if(row > 0) and fScore[row-1][col] > score + board[row-1][col]:
        n.append((row-1,col))
    if(row+1 < max_row) and fScore[row+1][col] > score + board[row+1][col]:
        n.append((row+1,col))

    if(col > 0) and fScore[row][col-1] > score + board[row][col-1]:
        n.append((row,col-1))
    if(col+1 < max_col) and fScore[row][col+1] > score + board[row][col+1]:
        n.append((row,col+1))

    return n

def score(node):
    return board[node[0]][node[1]]

def calc_score(cameFrom, curr):
    path = [curr]
    while curr in cameFrom:
        curr = cameFrom[curr]
        path.append(curr)
    return sum([score(n) for n in path]) - score((0, 0))

def dijkstra(start, goal, heuristic):
    openSet = set()
    openSet.add(start)

    cameFrom = {}
    
    fScore[start[0]][start[1]] = heuristic(start)

    while len(openSet) > 0:
        curr = min(openSet, key=lambda n: fScore[n[0]][n[1]])
        if curr == goal:
            return calc_score(cameFrom, curr)

        openSet.remove(curr)
        for n in get_neighbors(curr, fScore[curr[0]][curr[1]]):
            cameFrom[n] = curr
            fScore[n[0]][n[1]] = fScore[curr[0]][curr[1]] + heuristic(n)
            if n not in openSet:
                openSet.add(n)
    
    return -1

start = timeit.default_timer()
print(dijkstra((0, 0), (max_row-1, max_col-1), score))
stop = timeit.default_timer()

print('Time: ', stop - start)  