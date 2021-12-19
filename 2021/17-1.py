import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = f.read().splitlines()

    ((x_min, x_max),(y_min, y_max)) = tuple(map(lambda s: tuple(map(int, filter(lambda n: len(n)>0, s[2:].split('.')))), input_values[0][13:].split(', ')))


points = []
x_start, y_start = 0, 0
points.append((x_start, y_start))

y_vel = -1*(y_min+1)
print(sum(range(y_vel+1)))

x_candidates = []
x_sum = 0

for x in range(1, x_min):
    x_sum += x
    if x_sum > x_max:
        break
    if x_sum > x_min:
        x_candidates.append(x)


x_vel = x_candidates[0]
while x_start <= x_max and y_start >= y_min:
    x_start += x_vel
    y_start += y_vel
    points.append((x_start, y_start))

    if x_vel > 0:
        x_vel -= 1
    
    y_vel -= 1