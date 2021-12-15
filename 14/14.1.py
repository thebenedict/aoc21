#!/usr/bin/env python3

from collections import Counter

STEPS = 10

def main():
    with open("input.txt") as infile:
        rules = {}
        poly = infile.readline().strip()
        infile.readline()
        for line in infile.readlines():
            pair, elt = line.strip().split(" -> ")
            rules[pair] = elt

    for s in range(STEPS):
        new_poly = []
        for i in range(len(poly) - 1):
            pair = poly[i:i+2]
            if pair in rules:
                new_poly.append(pair[0])
                new_poly.append(rules[pair])
            else:
                new_poly.append(pair)
        new_poly.append(pair[-1])
        poly = "".join(new_poly)

    c = Counter(poly)
    most = c.most_common(1)[0][1]
    least = c.most_common()[-1][1]
    print(most - least)

if __name__ == "__main__":
    main()