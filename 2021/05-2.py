import os
import sys

filename = __file__[:-5] + '-input'


with open(filename) as f:
    input_values = list(map(int, map(lambda s: s.split(sep=','), f.read().splitlines())))


for day_index in range(80):
    pass

print()

# for y in range(10):
#     for x in range(10):
#         print(dict_values[(x,y)] if (x,y) in dict_values else '.', end=' ')

#     print()
