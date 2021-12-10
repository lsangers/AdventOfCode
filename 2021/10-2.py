import os
import sys
from numpy import median

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = list(map(lambda s: s, f.read().splitlines()))

illegal_score = {
    ')': 3,
    ']': 57,
    '}':1197,
    '>':25137,
}

complete_score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

points = []

for line in lines:
    tmp = line
    for _ in range(len(line)):
        tmp = tmp.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')

    if len(tmp) > 0:
        print(tmp)
        if not any([c in illegal_score for c in tmp]):
            score = 0
            for c in tmp[::-1]:
                score *= 5
                score += complete_score[c]

            points.append(score)


print(median(points))

