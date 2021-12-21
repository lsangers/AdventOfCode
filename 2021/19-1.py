import os
from itertools import combinations

filename = __file__[:-5] + '-input'

rotations = {
        #rotating around z first
        '(x, y, z)': lambda t: (t[0], t[1], t[2]),
        '(y, -x, z)': lambda t: (t[1], -t[0], t[2]),
        '(-x, -y, z)': lambda t: (-t[0], -t[1], t[2]),
        '(-y, x, z)': lambda t: (-t[1], t[0], t[2]),

        #rotating around y for (x, y, z)
        '(z, y, -x)': lambda t: (t[2], t[1], -t[0]),
        '(-x, y, -z)': lambda t: (-t[0], t[1], -t[2]),
        '(-z, y, x)': lambda t: (-t[2], t[1], t[0]),

        #rotating around y for (y, -x, z)
        '(z, -x, -y)': lambda t: (t[2], -t[0], -t[1]),
        '(-y, -x, -z)': lambda t: (-t[1], -t[0], -t[2]),
        '(-z, -x, y)': lambda t: (-t[2], -t[0], t[1]),

        #rotating around y for (-x, -y, z)
        '(z, -y, x)': lambda t: (t[2], -t[1], t[0]),
        '(x, -y, -z)': lambda t: (t[0], -t[1], -t[2]),
        '(-z, -y, -x)': lambda t: (-t[2], -t[1], -t[0]),

        #rotating around y for (-y, x, z)
        '(z, x, y)': lambda t: (t[2], t[0], t[1]),
        '(y, x, -z)': lambda t: (t[1], t[0], -t[2]),
        '(-z, x, -y)': lambda t: (-t[2], t[0], -t[1]),

        #rotating around x for(x, y, z) (only z as y interesting the other option we already have)
        '(x, z, -y)': lambda t: (t[0], t[2], -t[1]),
        '(x, -z, y)': lambda t: (t[0], -t[2], t[1]),

        #rotating around x for(y, -x, z) (only z as y interesting the other option we already have)
        '(y, z, x)': lambda t: (t[1], t[2], t[0]),
        '(y, -z, -x)': lambda t: (t[1], -t[2], -t[0]),

        #rotating around x for(-x, y, -z) (only z as y interesting the other option we already have)
        '(-x, -z, -y)': lambda t: (-t[0], -t[2], -t[1]),
        '(-x, z, y)': lambda t: (-t[0], t[2], t[1]),

        #rotating around x for(-y, x, z) (only z as y interesting the other option we already have)
        '(-y, z, -x)': lambda t: (-t[1], t[2], -t[0]),
        '(-y, -z, x)': lambda t: (-t[1], -t[2], t[0]),
    }

class Scanner: 
    def __init__(self, lines):
        self.scanner_id = lines[0][12:-4]
        self.beacons = list(map(lambda line: tuple(map(int, line.split(','))), lines[1:]))

        self.vect = [[self.vec(beacon, beacon2) for beacon2 in self.beacons] for beacon in self.beacons]
        self.dist = list(map(lambda l: list(map(lambda v: sum([abs(v[0]), abs(v[1]), abs(v[2])]), l)) , self.vect))

        self.rotated_vecs = {
            k: [list(map(v, row)) for row in self.vect] for k, v in rotations.items()
        }

    def vec(self, b1, b2):
        return ((b2[0] - b1[0]), (b2[1] - b1[1]) , (b2[2] - b1[2]))


with open(filename) as f:
    lines = f.read().splitlines()

    scanners = []
    
    beacons = []
    for line in lines:
        if line == '':
            scanners.append(Scanner(beacons))
            beacons.clear()
        else:
            beacons.append(line)

operations = {
    scanner.scanner_id: [] for scanner in scanners
}

matched = {
    scanner.scanner_id: [] for scanner in scanners
}
    
for scanner in scanners:
    for beacon_index, beacon in enumerate(scanner.vect):
        for other_scanner in scanners:
            if scanner.scanner_id == other_scanner.scanner_id or scanner.scanner_id in matched[other_scanner.scanner_id]:
                continue
            
            done = False
            for k, v in other_scanner.rotated_vecs.items():
                for i, r_v in enumerate(v):
                    set1 = set(beacon)
                    set2 = set(r_v)
                    set3 = set1.intersection(set2)
                    if(len(set3) > 11):
                        translation = tuple(map(lambda i, j: i - j, scanner.beacons[beacon_index], rotations[k](other_scanner.beacons[i])))
                        operations[other_scanner.scanner_id].append({ 'id': scanner.scanner_id, 'rotation': k, 'translation': translation})
                        matched[other_scanner.scanner_id].append(scanner.scanner_id)
                        done = True
                        break
                if done:
                    break

world_beacons = set()

to_place = ['0']
placed = []

steps = {}

while len(to_place) > 0:
    for oper in operations[to_place[0]]:
        if oper['id'] not in placed and oper['id'] not in to_place:
            to_place.append(oper['id'])
            placed.append(to_place[0])
            steps[oper['id']] = to_place[0]
    to_place = to_place[1:]

for scanner in scanners:
    
    local_space_id = scanner.scanner_id
    local_beacons = scanner.beacons
    while local_space_id != '0':
        for d in operations[local_space_id]:
            if d['id'] == steps[local_space_id]:
                rot_local = list(map(rotations[d['rotation']], local_beacons))
                local_beacons = list(map(lambda t: tuple(map(lambda i, j: i + j, t, d['translation'])), rot_local))
                #local_beacons = list(map(rotations[d['rotation']], move_local))

        local_space_id = steps[local_space_id]

    for beacon in local_beacons:
        world_beacons.add(beacon)
print(len(world_beacons))
world_scanners = []

for scanner in scanners:
    
    local_space_id = scanner.scanner_id
    local_scanner = [(0, 0, 0)]
    while local_space_id != '0':
        for d in operations[local_space_id]:
            if d['id'] == steps[local_space_id]:
                rot_scanner = list(map(rotations[d['rotation']], local_scanner))
                local_scanner = list(map(lambda t: tuple(map(lambda i, j: i + j, t, d['translation'])), rot_scanner))

        local_space_id = steps[local_space_id]

    for s in local_scanner:
        world_scanners.append(s)


distances = [abs(scanner_1[0] - scanner_2[0]) + abs(scanner_1[1] - scanner_2[1]) + abs(scanner_1[2] - scanner_2[2]) for (scanner_1, scanner_2) in combinations(world_scanners, 2)]

print(max(distances))
