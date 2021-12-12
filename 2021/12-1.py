import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(lambda s: s.split('-'), lines))


connections = {}

for line in lines:
    if line[0] not in connections and line[1] != 'start' and line[0] != 'end':
        connections[line[0]] = [line[1]]
    elif line[1] != 'start' and line[0] != 'end':
        connections[line[0]].append(line[1])

    if line[1] not in connections and line[0] != 'start' and line[1] != 'end':
        connections[line[1]] = [line[0]]
    elif line[0] != 'start' and line[1] != 'end':
        connections[line[1]].append(line[0])


routes = []

def find_all_paths(start, end, path):
    path.append(start)

    if start == end:
        routes.append(path)
    else:
        for neighbor in connections[start]:
                if (neighbor in path and neighbor.isupper()) or neighbor not in path:
                    find_all_paths(neighbor, end, path[:])

find_all_paths('start', 'end', [])


print(len(routes))