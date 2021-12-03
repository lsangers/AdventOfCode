import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(lambda s: s, f.read().splitlines()))

gamma_rate_string = ""
epsilon_rate_string = ""

life_rating = ''
co2_rating = ''

for i in range(len(input_values[0])):

    count_0 = 0
    count_1 = 0
    list1 = [s for s in input_values if s.startswith(gamma_rate_string)]
    for value in list1:
        if value[i] == "0":
            count_0 += 1    
        elif value[i] == "1":
            count_1 += 1
    if len(list1) > 0:
        gamma_rate_string += "0" if count_0 > count_1 else "1"
    if len(list1) == 1:
        life_rating = list1[0]


    count_0 = 0
    count_1 = 0
    list2 = [s for s in input_values if s.startswith(epsilon_rate_string)]
    for value in list2:
        if value[i] == "0":
            count_0 += 1    
        elif value[i] == "1":
            count_1 += 1
    if len(list2) > 0:
        epsilon_rate_string += "1" if count_0 > count_1 else "0"
    if len(list2) == 1:
        co2_rating = list2[0]

if len(life_rating) == 0:
    life_rating = gamma_rate_string

if len(co2_rating) == 0:
    co2_rating = epsilon_rate_string

print(int(life_rating, 2)* int(co2_rating, 2))