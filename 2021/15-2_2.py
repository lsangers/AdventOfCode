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

def get_neighbors(node, d):
    (row, col) = node
    n = []

    if(row > 0) and (row-1,col) not in d:
        n.append((row-1,col))
    if(row+1 < max_row) and (row+1,col) not in d:
        n.append((row+1,col))

    if(col > 0) and (row,col-1) not in d:
        n.append((row,col-1))
    if(col+1 < max_col) and (row,col+1) not in d:
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
    
    fScore = {}
    fScore[start] = heuristic(start)

    while len(openSet) > 0:
        print(len(fScore))
        curr = min(openSet, key=lambda n: fScore[n])
        if curr == goal:
            return calc_score(cameFrom, curr)

        openSet.remove(curr)
        for n in get_neighbors(curr, fScore):
            cameFrom[n] = curr
            fScore[n] = fScore[curr] + heuristic(n)
            if n not in openSet:
                openSet.add(n)
    
    return -1

start = timeit.default_timer()
print(dijkstra((max_row-1, max_col-1), (0, 0), score))
stop = timeit.default_timer()

print('Time: ', stop - start)  