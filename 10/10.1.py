#!/usr/bin/env python3

OPENS = ["(", "{", "[", "<"]
CLOSES = [")", "}", "]", ">"]
SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def main():
    nav_lines = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            nav_lines.append(line.strip())

    score = 0
    for line in nav_lines:
        illegal_char = is_corrupt(line)
        if illegal_char:
            score += SCORES[illegal_char]
    print(score)

def is_corrupt(line):
    stack = []
    for c in line:
        if c in OPENS:
            stack.append(c)
        else:
            o = stack.pop()
            if OPENS.index(o) != CLOSES.index(c):
                return c
    return None

if __name__ == "__main__":
    main()