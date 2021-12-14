#!/usr/bin/env python3

from collections import Counter
import sys

def main():
    with open("input.txt") as infile:
        in_str = infile.readline()
        pos = [int(p) for p in in_str.split(",")]
        counts = Counter(pos)
        
        fuel = 0
        min_fuel = sys.maxsize
        for i in range(max(pos) + 1):
            fuel = 0
            for p, c in counts.items():
                dist = abs(p - i)
                fuel += ((dist * (dist + 1)) / 2) * c
            if fuel < min_fuel:
                min_fuel = fuel
        print(min_fuel)

if __name__ == "__main__":
    main()