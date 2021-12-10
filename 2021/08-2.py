import os
import sys
from numpy import median

filename = __file__[:-5] + '-input'
total = 0

with open(filename) as f:
    lines = f.read().splitlines()
    
    for line in lines:
        inp,res = line.split('|')

        inp = list(map(lambda s: str(''.join(sorted(s))), inp.split()))
        res = list(map(lambda s: str(''.join(sorted(s))), res.split()))

        str_to_num = {}
        num_to_str = {}

        for num in list(filter(lambda x: len(x) in [2, 3, 4, 7], inp)):
            if len(num) == 2:
                str_to_num[num] = 1
                num_to_str[1] = num
            elif len(num) == 3:
                str_to_num[num] = 7
                num_to_str[7] = num
            elif len(num) == 4:
                str_to_num[num] = 4
                num_to_str[4] = num
            elif len(num) == 7:
                str_to_num[num] = 8
                num_to_str[8] = num

        for num in list(filter(lambda x: len(x) in [5,6], inp)):
            if len(num) == 5:
                gc = list(set(num_to_str[8]) - set(num_to_str[4]) - set(num_to_str[7]))
                if all(elem in num for elem in gc):
                    str_to_num[num] = 2
                    num_to_str[2] = num

                ef = list(set(num_to_str[4]) - set(num_to_str[7]) )
                test_5 = [elem for elem in num if elem in ef]
                if len(test_5) == 2:
                    str_to_num[num] = 5
                    num_to_str[5] = num

                
            elif len(num) == 6:
                gc = list(set(num_to_str[8]) - set(num_to_str[4]) - set(num_to_str[7]))
                test_9 = [elem for elem in num if elem in gc]
                if len(test_9) == 1:
                    str_to_num[num] = 9
                    num_to_str[9] = num

                ef = list(set(num_to_str[4]) - set(num_to_str[7]) )
                test_0 = [elem for elem in num if elem in ef]
                if len(test_0) == 1:
                    str_to_num[num] = 0
                    num_to_str[0] = num
    

        for num in list(filter(lambda x: len(x) in [5,6] and x not in str_to_num, inp)):
            if len(num) == 5:
                    str_to_num[num] = 3
                    num_to_str[3] = num
            elif len(num) == 6:
                    str_to_num[num] = 6
                    num_to_str[6] = num

    
        res_str = ''

        for num in res:
            res_str += str(str_to_num[num])

        total += int(res_str)
print(total)

