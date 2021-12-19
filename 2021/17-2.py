import os
import sys

filename = __file__[:-5] + '-input'
filename2 = __file__[:-5] + '-input-2'

with open(filename) as f:
    input_values = f.read().splitlines()

    ((x_min, x_max),(y_min, y_max)) = tuple(map(lambda s: tuple(map(int, filter(lambda n: len(n)>0, s[2:].split('.')))), input_values[0][13:].split(', ')))

points = []

def in_range(x_vel, y_vel):
    x_start = y_start = 0
    while x_start <= x_max and y_start >= y_min:
        if x_start >= x_min and y_start <= y_max:
            return True
        x_start += x_vel
        y_start += y_vel

        if x_vel > 0:
            x_vel -= 1        
        y_vel -= 1

    return False

y_vel = -1*(y_min+1)

for x in range(0, x_max+1):
    for y in range(y_min, y_vel+1):
        if in_range(x, y):
            points.append((x, y))

with open(filename2) as f:
    input_values = f.read().splitlines()

    points_pattern = list(map(lambda s: tuple(map(int, s.split(','))), input_values))
    points_pattern.sort()

diff = list(set(points_pattern) - set(points))
print(len(points))