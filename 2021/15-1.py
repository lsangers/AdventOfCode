import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(lambda s: list(map(lambda elem: int(elem), list(s))), lines))

board = lines[:]


max_row = len(board)
max_col = len(board[0])

def get_neighbors(node):
    (row, col) = node
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

def heuristic(node):
    return board[node[0]][node[1]]

def calc_score(cameFrom, curr):
    path = [curr]
    while curr in cameFrom:
        curr = cameFrom[curr]
        path.append(curr)
    return sum([heuristic(n) for n in path]) - heuristic((0, 0))

def get_Score(d, n):
    if n in d:
        return d[n]
    else:
        return 9999999

def A_star(start, goal, heuristic):
    openSet = set()
    openSet.add(start)

    cameFrom = {}
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = heuristic(start)

    while len(openSet) > 0:
        curr = min(fScore.keys() & openSet, key=fScore.get)
        if curr == goal:
            return calc_score(cameFrom, curr)

        openSet.remove(curr)
        for n in get_neighbors(curr):
            tentative_score = gScore[curr] + heuristic(n)
            if tentative_score < get_Score(gScore, n):
                cameFrom[n] = curr
                gScore[n] = tentative_score
                fScore[n] = tentative_score
                if n not in openSet:
                    openSet.add(n)
    
    return -1

print(A_star((0, 0), (max_row-1, max_col-1), heuristic))