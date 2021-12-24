#!/usr/bin/env python3

import math
from sys import version

HEX_VALS = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

OPERATORS = {
    0: "sum",
    1: "product",
    2: "min",
    3: "max",
    5: "gt",
    6: "lt",
    7: "eq",
}

LITERAL_VALUE_TYPE = 4

version_sum = 0
cursor = 0

def main():
    with open("input.txt") as infile:
        transmission = infile.readline().strip()
    transmission_b = htob(transmission)

    while cursor < len(transmission_b):
        if "1" in transmission_b[cursor:]:
            result = read_packets(transmission_b)
        else:
            break
    print(f'result: {result}')

def read_packets(str_b):
    global cursor
    version, cursor = get_bin_field(str_b, cursor, 3)
    global version_sum
    version_sum += version
    print(f'version: {version}')
    
    type_id, cursor = get_bin_field(str_b, cursor, 3)
    print(f'type_id: {type_id}')
    if type_id == LITERAL_VALUE_TYPE:
        literal, cursor = read_literal(str_b, cursor)
        print(f'\tliteral: {literal}')
        return literal
    else:
        operator = OPERATORS[type_id]
        length_type_id = str_b[cursor]
        print(f'length_type_id: {length_type_id}')
        cursor += 1
        if length_type_id == "0":
            sub_packet_length, cursor = get_bin_field(str_b, cursor, 15)
            print(f'sub_packet_length: {sub_packet_length}')
            end = cursor + sub_packet_length 
            vals = []
            while cursor < end:
               vals.append(read_packets(str_b))
        elif length_type_id == "1":
            sub_packet_count, cursor = get_bin_field(str_b, cursor, 11)
            print(f'sub_packet_count: {sub_packet_count}')
            vals = []
            for p in range(sub_packet_count, 0, -1):
                vals.append(read_packets(str_b))
        if operator == "sum":
            return sum(vals)
        elif operator == "product":
            return math.prod(vals)
        elif operator == "min":
            return min(vals)
        elif operator == "max":
            return max(vals)
        elif operator == "gt":
            if len(vals) != 2:
                print("error wrong number of vals in gt")
            return 1 if vals[0] > vals[1] else 0
        elif operator == "lt":
            if len(vals) != 2:
                print("error wrong number of vals in lt")
            return 1 if vals[0] < vals[1] else 0
        elif operator == "eq":
            if len(vals) != 2:
                print("error wrong number of vals in eq")
            return 1 if vals[0] == vals[1] else 0
        else:
            print("error unrecognized operator")

def show(str_b, cursor):
    print(f'{str_b[:cursor]}|{str_b[cursor:]}')

def get_bin_field(str_b, cursor, field_length):
    val_b = str_b[cursor:cursor + field_length]
    return int(val_b, 2), cursor + field_length

def read_literal(bin, cursor):
    literal_b = []
    char_count = 0
    while bin[cursor] == "1":
        literal_b.append(bin[cursor + 1:cursor + 5])
        cursor += 5
        char_count += 5
    literal_b.append(bin[cursor + 1:cursor + 5])
    cursor += 5
    char_count += 5

    literal_s = "".join(literal_b)
    return int(literal_s, 2), cursor
    
def htob(hstr):
    out = []
    for char in hstr:
        out.append(HEX_VALS[char])
    return "".join(out)

if __name__ == "__main__":
    main()