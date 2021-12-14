import os
import sys

filename = __file__[:-5] + '-input'

def add_count(c, d, am = 1):
    if c not in d:
        d[c] = am
    else:
        d[c] += am

with open(filename) as f:
    lines = f.read().splitlines()

    start_seq = lines[0]
    starting_pairs = {}
    for i in range(len(start_seq)-1):
        p = start_seq[i:i+2]
        add_count(p, starting_pairs)    

    pairs = {}
    for line in lines[2:]:
        pair, inp = line.split(' -> ')
        pairs[pair] = inp


counting_pairs = starting_pairs.copy()

for _ in range(40):
    tmp_pairs = counting_pairs.copy()
    counting_pairs.clear()
    for k,v in tmp_pairs.items():
        ins = pairs[k]
        new_pair1 = k[0] + ins
        new_pair2 = ins + k[1]
        add_count(new_pair1, counting_pairs, v)
        add_count(new_pair2, counting_pairs, v)


counts = {}

for k,v in counting_pairs.items():
    add_count(k[0], counts, v)
add_count(start_seq[-1], counts, 1)


print(max(counts.values()) - min(counts.values()))



