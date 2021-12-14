#!/usr/bin/env python3

GRID_SIZE = 10
NUM_STEPS = 100

flashes = 0
flashed = []
octos = []

def main():
    global octos
    with open("input.txt") as infile:
        for line in infile.readlines():
            octos.append([int(o) for o in line.strip()])

    for i in range(NUM_STEPS):
        step()
        if i < 10 or i % 10 == 0:
            print("After step {}".format(i+1))
            for row in octos:
                print("".join([str(o) for o in row]))
            print("-------")
    print(flashes)

def step():
    global octos
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            octos[r][c] += 1

    global flashed
    flashed = [[0] * GRID_SIZE for i in range(GRID_SIZE)]
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if not flashed[r][c] and octos[r][c] >= 10:
                print("root flashing {},{}".format(r,c))
                flash([(r, c)])

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if octos[r][c] >= 10:
                octos[r][c] = 0

def flash(to_flash):
    global flashes
    global flashed
    global octos
    
    while to_flash:
        flashes += 1
        r, c = to_flash.pop()
        flashed[r][c] = 1
        for nr, nc in [(r+1, c), (r+1, c+1), (r+1, c-1), (r-1, c), (r-1, c+1), (r-1, c-1), (r, c+1), (r, c-1)]:
            if nr >= 0 and nr < GRID_SIZE and nc >= 0 and nc < GRID_SIZE:
                octos[nr][nc] += 1
                if not flashed[nr][nc] and octos[nr][nc] >= 10:
                    print("\tappending {},{}".format(r,c))
                    flashed[nr][nc] = 1
                    to_flash.append((nr, nc))

if __name__ == "__main__":
    main()