import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()
    enhancement_alg = list(lines[0])

    image = [list(line) for line in lines[2:]]
    print()


def get_buffer(im, use_period):
    image_width = len(im[0])
    scale = 4
    buffer_width = image_width + scale*2 # adding 2 to both sides as that accounts for infinitely growing ?? -> how can 0 be # ??
    
    sym = '.' if use_period else '#'

    tmp = [list(sym*(buffer_width))]*scale

    for row in im:
        tmp.append([sym]*scale + row + [sym]*scale)

    tmp.extend([list(sym*(buffer_width))]*scale)

    return tmp

def flatten(t):
    return [item for sublist in t for item in sublist]

def get_enhanced_value(area):
    key = 0
    for i, c in enumerate(area):
        key += (0 if c == '.' else 1) * (2**(8-i))
    return enhancement_alg[key]

def enhance(buffer):
    enhanced_buffer = []

    for y in range(len(buffer) - 2):
        enhanced_row = []
        for x in range(len(buffer[0]) - 2):
            area = flatten([row[x:x+3] for row in buffer[y:y+3]])
            enhanced_row.append(get_enhanced_value(area))
        enhanced_buffer.append(enhanced_row)
    return [line[2:-2] for line in enhanced_buffer[2:-2]]


for line in image:
    for c in line:
        print(c, end='')
    print()

print('---')
for i in range(50):
    buffer = get_buffer(image, i%2 == 0)
    image = enhance(buffer)

for line in image:
    for c in line:
        print(c, end='')
    print()


print(sum(map(lambda l: l.count('#'), image)))