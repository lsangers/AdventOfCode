import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(lambda s: s.split(), f.read().splitlines()))

total_forward = 0
total_depth = 0

for direction, distance in input_values:
    if direction == 'forward':
        total_forward += int(distance)
    elif direction == 'up':
        total_depth -= int(distance)
    elif direction == 'down':
        total_depth += int(distance)
    

print(total_forward*total_depth)