import os
import sys

filename = __file__[:-5] + '-input'

def points_list(lines):
    #map(lambda points: [(int(points[0].split(',')[0]), int(points[0].split(',')[1])), (int(points[1].split(',')[0]), int(points[0].split(',')[1]))],
    res = {}
    for points in lines:
        x1, y1 = map(int, points[0].split(','))
        x2, y2 = map(int, points[1].split(','))

        if x1 == x2 or y1 == y2:
            x_min = min(x1,x2)
            x_max = max(x1,x2)
            y_min = min(y1,y2)
            y_max = max(y1,y2)
            for x in range(x_min, x_max+1):
                for y in range(y_min, y_max+1):
                    key = (x, y)
                    if key not in res:
                        res[key] = 1
                    else:
                        res[key] += 1
                        
    return res


with open(filename) as f:
    input_values = list(map(lambda s: s.split(sep=' -> '), f.read().splitlines()))

    dict_values = points_list(input_values)

matching = dict(filter(lambda elem: elem[1] >= 2, dict_values.items()))

print(len(matching))
