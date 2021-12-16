#!/usr/bin/env python3

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

LITERAL_VALUE_TYPE = 4


def main():
    transmission = "D2FE28"
    transmission_b = htob(transmission)
    cursor = 0
    while cursor <= len(transmission_b):
        version, cursor = get_bin_field(transmission_b, cursor, 3)
        type_id, cursor = get_bin_field(transmission_b, cursor, 3)
        if type_id == LITERAL_VALUE_TYPE:
            literal, cursor = read_literal(transmission_b, cursor)
            print(literal)
        else:
            length_type_id = transmission_b[cursor]
            cursor += 1
            if length_type_id == 1:
                pass #TODO
            elif length_type_id == 0:
                pass #TODO

def get_bin_field(bin, cursor, field_length):
    val_b = bin[cursor:cursor + field_length]
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

    # pad char_count + 6 (version, typeid) to a multiple of 4   
    len_padding = 4 - (char_count + 6) % 4
    cursor = consume_padding(bin, cursor, len_padding) 

    literal_s = "".join(literal_b)
    return int(literal_s, 2), cursor

def consume_padding(bin, cursor, len_padding):
    if "1" in bin[cursor:cursor + len_padding]:
        print("Error padding is not all 0")
    else:
        return cursor + len_padding
    

def htob(hstr):
    out = []
    for char in hstr:
        out.append(HEX_VALS[char])
    return "".join(out)

if __name__ == "__main__":
    main()