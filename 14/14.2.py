#!/usr/bin/env python3

from collections import defaultdict

STEPS = 40

def main():
    with open("input.txt") as infile:
        rules = {}
        poly = infile.readline().strip()
        infile.readline()
        for line in infile.readlines():
            pair, elt = line.strip().split(" -> ")
            rules[pair] = elt
    
    pair_counts = defaultdict(int)
    for i in range(len(poly) - 1):
        pair_counts[poly[i:i+2]] += 1

    for s in range(STEPS):
        new_counts = defaultdict(int) 
        for pair, count in pair_counts.items():
            new_counts[pair[0] + rules[pair]] += count
            new_counts[rules[pair] + pair[1]] += count
        pair_counts = new_counts
    
    letter_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count
    letter_counts[poly[-1]] += 1
    print(max(letter_counts.values()) - min(letter_counts.values()))

if __name__ == "__main__":
    main()

