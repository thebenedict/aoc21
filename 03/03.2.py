#!/usr/bin/env/python

def main():
    lines = []
    with open("input.txt") as infile:
        for line in infile:
            lines.append(line.strip())

    i = 0
    tmp = lines
    while len(tmp) > 1:
        most_common = most_common_at(i, tmp)
        tmp = [val for val in tmp if val[i] == most_common]
        i += 1
    oxygen_generator = int(tmp[0], 2)

    i = 0
    tmp = lines
    while len(tmp) > 1:
        least_common = least_common_at(i, tmp)
        tmp = [val for val in tmp if val[i] == least_common]
        i += 1
    co2_scrubber = int(tmp[0], 2)

    print(oxygen_generator * co2_scrubber)

def most_common_at(i, lines):
    zeroes = 0
    ones = 0
    for line in lines:
        if line[i] == "0":
            zeroes += 1
        else:
            ones += 1
    if ones >= zeroes:
        return "1"
    else:
        return "0"

def least_common_at(i, lines):
    zeroes = 0
    ones = 0
    for line in lines:
        if line[i] == "0":
            zeroes += 1
        else:
            ones += 1
    if zeroes <= ones:
        return "0"
    else:
        return "1"

if __name__ == "__main__":
    main()