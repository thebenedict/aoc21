#!/usr/bin/env python3
from heapq import heappush, heappop
import sys

def main():
    cave = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            cave.append([int(r) for r in line.strip()])

    risks = [[sys.maxsize] * len(cave) for c in range(len(cave))]
    visited = set()
    q = [(0, 0, 0)]
    cave_size = len(cave)
    while q:
        risk, y, x = heappop(q)
        if y == cave_size - 1 and x == cave_size - 1:
            print(risk)
            return

        visited.add((y, x))
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if ny >= 0 and ny < cave_size and nx >= 0 and nx < cave_size:
                new_risk = risk + cave[ny][nx]
                if (ny, nx) not in visited and new_risk < risks[ny][nx]:
                    risks[ny][nx] = new_risk
                    heappush(q, (new_risk, ny, nx))

if __name__ == "__main__":
    main()