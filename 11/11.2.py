#!/usr/bin/env python3

GRID_SIZE = 10
NUM_STEPS = 100

num_flashes = 0
flashed = []
octos = []

def main():
    global octos
    global num_flashes
    with open("example.txt") as infile:
        for line in infile.readlines():
            octos.append([int(o) for o in line.strip()])

    steps = 0
    while num_flashes < GRID_SIZE**2: 
        num_flashes = 0
        step()
        steps += 1
    print(steps)

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
                flashed[r][c] = 1
                flash(r, c)

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if octos[r][c] >= 10:
                octos[r][c] = 0

def flash(r, c):
    global num_flashes
    global flashed
    global octos
    
    num_flashes += 1
    for nr, nc in [(r+1, c), (r+1, c+1), (r+1, c-1), (r-1, c), (r-1, c+1), (r-1, c-1), (r, c+1), (r, c-1)]:
        if nr >= 0 and nr < GRID_SIZE and nc >= 0 and nc < GRID_SIZE:
            octos[nr][nc] += 1
            if not flashed[nr][nc] and octos[nr][nc] >= 10:
                flashed[nr][nc] = 1
                flash(nr, nc)

if __name__ == "__main__":
    main()