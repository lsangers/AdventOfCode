import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(int, f.read().splitlines()))

curr_depth = max(input_values) + 1

count = 0

for depth in input_values:
    if depth > curr_depth:
        count += 1
    curr_depth = depth

print(count)

