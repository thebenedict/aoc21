#!/usr/bin/env python3
import math;

def main():
    heightmap = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            heightmap.append([int(n) for n in list(line.strip())])

    rows = len(heightmap)
    cols = len(heightmap[0])

    global explored
    global basin_sizes
    global cur_size
    explored = [[0] * cols for r in range(rows)]
    basin_sizes = []
    cur_size = 0

    for r in range(rows):
        for c in range(cols):
            if not explored[r][c]:
                explore_basin_at(heightmap, r, c)
                basin_sizes.append(cur_size)
                cur_size = 0
    print(math.prod(sorted(basin_sizes)[-3:]))


def explore_basin_at(heightmap, r, c):
    explored[r][c] = 1
    if heightmap[r][c] == 9:
        return
    global cur_size
    cur_size += 1
    for nr, nc in get_neighbors(heightmap, r, c):
        if not explored[nr][nc]:
            explore_basin_at(heightmap, nr, nc)

def get_neighbors(heightmap, r, c):
    neighbors = []
    if r + 1 < len(heightmap):
        neighbors.append((r + 1, c))
    if r - 1 >= 0:
        neighbors.append((r - 1, c))
    if c + 1 < len(heightmap[0]):
        neighbors.append((r, c + 1))
    if c - 1 >= 0:
        neighbors.append((r, c - 1))
    return neighbors

if __name__ == "__main__":
    main()