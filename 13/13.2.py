#!/usr/bin/env python3

def main():
    dots = set()
    folds = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            if line[0].isdigit():
                x, y = [int(p) for p in line.strip().split(",")]
                dots.add((x, y))
            elif line.startswith("fold"):
                axis = line[11]
                val = int(line.split("=")[1])
                folds.append((axis, val))

    for f in folds:
        dots = fold(dots, *f)

    x_max = sorted(dots)[-1][0]
    y_max = sorted(dots, key = lambda x: x[1])[-1][1]
    for y in range(y_max + 1):
        line = []
        for x in range(x_max + 1):
            if (x, y) in dots:
                line.append("##")
            else:
                line.append("  ")
        print("".join(line))

def fold(dots, axis, val):
    new_dots = set()
    
    if axis == "x":
        for d in dots:
            if d[0] > val:
                new_dots.add((2 * val - d[0], d[1]))
            else:
                new_dots.add(d)
    else:
        for d in dots:
            if d[1] > val:
                new_dots.add((d[0], 2 * val - d[1]))
            else:
                new_dots.add(d)
    return new_dots

if __name__ == "__main__":
    main()