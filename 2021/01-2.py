import os

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(int, f.read().splitlines()))

curr_depth = 999999

count = 0

for i in range(len(input_values) - 2):
    depth = input_values[i] + input_values[i + 1] + input_values[i + 2]
    if depth > curr_depth:
        count += 1
    curr_depth = depth

print(count)

