import os
import sys
from numpy import median

filename = __file__[:-5] + '-input'
total = 0
with open(filename) as f:
    lines = f.read().splitlines()
    numbers_line = list(map(lambda l: l.split('|')[1].split(), lines))
    for line in numbers_line:
        filtered = list(filter(lambda x: len(x) in [2, 3, 4, 7], line))
        total += len(filtered)
    print(total)

