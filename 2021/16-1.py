import os
import sys
from functools import reduce

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

bits = ''
for ch in input_values[0]:
    bits += translation[ch]

class Packet:
    def __init__(self, bitstring):
        self.bitstring = bitstring
        self.version = int(bitstring[:3], 2)
        self.type = int(bitstring[3:6], 2)
        self.total_packet_length = 0
        self.subpackets = []

        # packet is a literal value
        if self.type == 4:
            potential_value_bits = bitstring[6:]
            start_index = 0
            getting_literal_value = True
            literal_value_bitstring = ''
            while getting_literal_value:
                lit = potential_value_bits[start_index:start_index+5]
                start_index += 5
                literal_value_bitstring += lit[1:]
                if lit[0] == '0':
                    getting_literal_value = False
            self.literal_value = int(literal_value_bitstring, 2)
            self.total_packet_length = 6 + start_index
        else:
            self.length_type = bitstring[6]
            # next 15 bits are number that represents total length in bits of sub-packets in this packet
            if self.length_type == '0':
                total_length = int(bitstring[7:22], 2)
                self.total_packet_length = 22 + total_length

                next_subpacket_start = 22

                while next_subpacket_start < self.total_packet_length:
                    next_subpacket = Packet(bitstring[next_subpacket_start:self.total_packet_length])
                    self.subpackets.append(next_subpacket)
                    next_subpacket_start += next_subpacket.total_packet_length
                
            # next 11 bits are number that represents number of sub-packets in this packet
            else:
                num_of_subpackets = int(bitstring[7:18], 2)

                next_subpacket_start = 18

                for _ in range(num_of_subpackets):
                    next_subpacket = Packet(bitstring[next_subpacket_start:])
                    self.subpackets.append(next_subpacket)
                    next_subpacket_start += next_subpacket.total_packet_length
                self.total_packet_length = next_subpacket_start
    
    def version_total(self):
        return self.version + sum(map(lambda p: p.version_total(), self.subpackets))

    def calc_value(self):
        if self.type == 0:
            return sum(map(lambda p: p.calc_value(), self.subpackets))
        elif self.type == 1:
            return reduce(lambda x, y: x*y, map(lambda p: p.calc_value(), self.subpackets), 1)
        elif self.type == 2:
            return min(map(lambda p: p.calc_value(), self.subpackets))
        elif self.type == 3:
            return max(map(lambda p: p.calc_value(), self.subpackets))
        elif self.type == 4:
            return self.literal_value
        elif self.type == 5:
            return 1 if self.subpackets[0].calc_value() > self.subpackets[1].calc_value() else 0
        elif self.type == 6:
            return 1 if self.subpackets[0].calc_value() < self.subpackets[1].calc_value() else 0
        elif self.type == 7:
            return 1 if self.subpackets[0].calc_value() == self.subpackets[1].calc_value() else 0



p = Packet(bits)

print(p.version_total())

