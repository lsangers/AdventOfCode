import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()

    find_points = True

    points = set()
    folds = []

    for line in lines:
        if len(line) == 0:
            find_points = False
            continue

        if find_points:
            points.add(tuple(map(int, line.split(','))))
        else:
            folds.append(line.split()[-1].split('='))

max_x = 0
max_y = 0

for axis,val in folds:
    tmp = set()
    val = int(val)
    if axis == 'y':
        max_y = val
        for (x, y) in points:
            if y > val:
                y = val - (y - val)
                tmp.add((x, y))
            else:
                tmp.add((x, y))

    else:
        max_x = val
        for (x, y) in points:
            if x > val:
                x = val - (x - val)
                tmp.add((x, y))
            else:
                tmp.add((x, y))
    points = tmp.copy()


for y in range(max_y):
    output_line = ''
    for x in range(max_x):
        output_line += '.' if (x, y) not in points else '#'
    print(output_line)




