import os

filename = __file__[:-5] + '-input'


class Scanner:
    def __init__(self, scanner_id, beacons):
        self.scanner_id = scanner_id
        self.beacons = beacons

with open(filename) as f:
    lines = f.read().splitlines()

    scanners = []
    start_index = 0
    while start_index < len(lines):
        scanners.append(Scanner(lines[start_index][13:-3], lines[start_index+1:start_index+28]))
