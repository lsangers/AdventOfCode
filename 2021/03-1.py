import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(lambda s: s, f.read().splitlines()))

gamma_rate_string = ""
epsilon_rate_string = ""

for i in range(len(input_values[0])):

    count_0 = 0
    count_1 = 0
    for value in input_values:
        if value[i] == "0":
            count_0 += 1
        elif value[i] == "1":
            count_1 += 1

    gamma_rate_string += "0" if count_0 > count_1 else "1"
    epsilon_rate_string += "1" if count_0 > count_1 else "0"

print(int(gamma_rate_string, 2)* int(epsilon_rate_string, 2))