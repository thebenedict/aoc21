#!/usr/bin/env python3
from heapq import heappush, heappop
import sys

CAVE_TILE_COUNT = 5

def main():
    cave = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            cave.append([int(r) for r in line.strip()])

    cave_size = len(cave) * CAVE_TILE_COUNT
    risks = [[sys.maxsize] * cave_size for c in range(cave_size)]
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
                new_risk = risk + get_risk(cave, ny, nx)
                if (ny, nx) not in visited and new_risk < risks[ny][nx]:
                    risks[ny][nx] = new_risk
                    heappush(q, (new_risk, ny, nx))

def get_risk(cave, ny, nx):
    y = ny % len(cave)
    y_tile = ny // len(cave)
    x = nx % len(cave)
    x_tile = nx // len(cave)

    base_risk = cave[y][x]
    tiled_risk = base_risk + y_tile + x_tile
    if tiled_risk > 9:
        return tiled_risk % 10 + 1
    else:
        return tiled_risk

if __name__ == "__main__":
    main()