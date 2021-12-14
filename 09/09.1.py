#!/usr/bin/env python3

def main():
    heightmap = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            heightmap.append([int(n) for n in list(line.strip())])
    total_risk = 0
    for i, row in enumerate(heightmap):
        for j, point in enumerate(row):
            if point < min(get_neighbor_vals(heightmap, i, j)):
                total_risk += (point + 1)

    print(total_risk)

def get_neighbor_vals(heightmap, i, j):
    neighbor_vals = []
    neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    for row, col in neighbors:
        if row >= 0 and col >=0:
            try:
                neighbor_vals.append(heightmap[row][col])
            except IndexError:
                pass
    return neighbor_vals

if __name__ == "__main__":
    main()