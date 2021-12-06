import os
import sys

filename = __file__[:-5] + '-input'


with open(filename) as f:
    input_line = f.read()
    input_values = list(map(int, input_line.split(sep=',')))


for day_index in range(80):
    new_fish = []
    for fish in input_values:
        if fish == 0:
            new_fish.append(6)
            new_fish.append(8)
    input_values = list(map(lambda x: x - 1, filter( lambda x: x != 0, input_values)))
    input_values.extend(new_fish)
        

print(len(input_values))

