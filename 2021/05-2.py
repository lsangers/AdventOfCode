import os
import sys

filename = __file__[:-5] + '-input'

def points_list(lines):
    res = {}
    for points in lines:
        x1, y1 = map(int, points[0].split(','))
        x2, y2 = map(int, points[1].split(','))

        #probably can clean this up with calculating a slope first and then stepping through the values
        # then I do not need this if else, but this works as well :)
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
        else:
            x_step = 1 if x1 < x2 else -1
            y_step = 1 if y1 < y2 else -1
            options = [(x1+x_step*i, y1+y_step*i) for i in range(abs(x1-x2)+1)]
            for key in options:
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

# for y in range(10):
#     for x in range(10):
#         print(dict_values[(x,y)] if (x,y) in dict_values else '.', end=' ')

#     print()
