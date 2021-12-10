import os
import sys
from numpy import median

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(int, f.read().split(',')))

average = int(round(sum(input_values)/len(input_values)))

total_diff_1 = sum(map(lambda x: sum(range(abs(x - average - 1)+1)), input_values))
total_diff_2 = sum(map(lambda x: sum(range(abs(x - average)+1)), input_values))
total_diff_3 = sum(map(lambda x: sum(range(abs(x - average + 1)+1)), input_values))

print(min(total_diff_1, total_diff_2, total_diff_3))