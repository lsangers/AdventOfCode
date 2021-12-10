import os
import sys
from numpy import median

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(int, f.read().split(',')))

# numbers = {}

# for num in set(input_values):
#     numbers[num] = input_values.count(num)

# average = int(sum(input_values)/len(input_values))

m = median(input_values)

total_diff = sum(map(lambda x: abs(x - m), input_values))

print(total_diff)