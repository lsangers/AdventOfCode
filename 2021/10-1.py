import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = list(map(lambda s: s, f.read().splitlines()))

illegal_score = {
    ')': 3,
    ']': 57,
    '}':1197,
    '>':25137,
}

points = 0

for line in lines:
    tmp = line
    for _ in range(len(line)):
        tmp = tmp.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')

    if len(tmp) > 0:
        print(tmp)
        for c in tmp:
            if c in illegal_score:
                points += illegal_score[c]
                break
print(points)

