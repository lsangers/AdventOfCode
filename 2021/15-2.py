import os
import sys
import timeit

filename = __file__[:-5] + '-input'

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

def get_neighbors(node):
    (row, col) = node
    n = []

    if(row > 0):
        n.append((row-1,col))
    if(row+1 < max_row):
        n.append((row+1,col))

    if(col > 0) :
        n.append((row,col-1))
    if(col+1 < max_col):
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

def get_val(d, n):
    if n in d:
        return d[n]
    else:
        return 999999999

fScore = {}

def a_star(start, goal, heuristic):
    openSet = set()
    openSet.add(start)

    cameFrom = {}
    gScore = {}
    gScore[start] = 0
    
    fScore[start] = heuristic(start)

    while len(openSet) > 0:
        #print(len(fScore))
        curr = min(openSet, key=lambda n: fScore[n])
        if curr == goal:
            return gScore[goal]#calc_score(cameFrom, curr)

        if goal in openSet:
            print("found goal at len:", len(gScore))

        openSet.remove(curr)
        for n in get_neighbors(curr):
            tentative_gScore = gScore[curr] + score(n)
            if tentative_gScore < get_val(gScore, n):
                cameFrom[n] = curr
                gScore[n] = tentative_gScore
                fScore[n] = tentative_gScore + heuristic(n)
                if n not in openSet:
                    openSet.add(n)
    
    return -1

start = timeit.default_timer()
print(a_star((0, 0), (max_row-1, max_col-1), lambda node: score(node)))
stop = timeit.default_timer()

print('Time: ', stop - start)