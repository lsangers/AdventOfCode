import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()

    start_seq = lines[0]

    pairs = {}
    for line in lines[2:]:
        pair, inp = line.split(' -> ')
        pairs[pair] = inp

counts = {}
def add_count(c):
    if c not in counts:
        counts[c] = 1
    else:
        counts[c] += 1

for c in start_seq:
    add_count(c)

tmp_seq = list(start_seq)

for _ in range(10):
    seq = tmp_seq[:]
    tmp_seq.clear()
    for i in range(len(seq)-1):
        p = seq[i] + seq[i+1]
        tmp_seq.append(seq[i])
        tmp_seq.append(pairs[p])
        add_count(pairs[p])

    tmp_seq.append(seq[-1])

print(max(counts.values()) - min(counts.values()))
