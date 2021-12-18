import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    input_values = list(map(lambda h: list(h), f.read().splitlines()))

translation = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

hex_chars = input_values[0]
bits = ''
for ch in hex_chars:
    bits += translation[ch]



def get_literals(bitstring):
    res = ''
    start_index = 0
    getting_literals = True
    while getting_literals:
        lit = bitstring[start_index:start_index+5]
        res += lit[1:]
        if lit[0] == '0':
            getting_literals = False
            start_index += 5
        else:
            start_index += 5
    return str(int(res, 2)), start_index

def get_packets(bitstring):
    version = int(bitstring[:3], 2)
    type = int(bitstring[3:6], 2)
    versions = []     
    processed_till = 0     

    if type == 4:
        lit, start_index = get_literals(bitstring[6:])
        processed_till = 6+start_index
    else:
        length_type = bitstring[6]
        if length_type == '0':
            total_bits = int(bitstring[7:22], 2)
            bitstring = bitstring[22:22+total_bits]  
            while len(bitstring) > 0:
                tmp_version, tmp_type, processed_till_local = get_packets(bitstring)
                versions.append(tmp_version)
                bitstring = bitstring[processed_till_local:] 
                processed_till += processed_till_local
        else:
            sub_parts = int(bitstring[7:18], 2)
            bitstring = bitstring[18:] 
            for _ in range(sub_parts):
                tmp_version, tmp_type, processed_till_local = get_packets(bitstring)
                versions.append(tmp_version)
                bitstring = bitstring[processed_till_local:] 
                processed_till += processed_till_local

    return (version+sum(versions), type, processed_till)
                



version, type, processed_till = get_packets(bits)    

print(str(version))