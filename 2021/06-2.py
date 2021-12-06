import os
import sys

filename = __file__[:-5] + '-input'


with open(filename) as f:
    input_line = f.read()
    input_values = list(map(int, input_line.split(sep=',')))

total = 0

current_fish = {}

for start in range(0,9):
    current_fish[start] = input_values.count(start)

for day in range(256):
    curr = current_fish[0]
    for i in range(0,8):
        current_fish[i] = current_fish[i+1]

    current_fish[6] += curr
    current_fish[8] = curr
        
for key,value in current_fish.items():
    total += value
print(total)

