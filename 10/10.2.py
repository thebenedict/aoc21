#!/usr/bin/env python3

OPENS = ["(", "{", "[", "<"]
CLOSES = [")", "}", "]", ">"]
SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def main():
    nav_lines = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            nav_lines.append(line.strip())

    incomplete_lines = []
    for line in nav_lines:
        if not is_corrupt(line):
            incomplete_lines.append(line)

    scores = []
    for line in incomplete_lines:
        cs = get_completion_string(line)
        scores.append(score_completion_string(cs))
    print(sorted(scores)[len(scores) // 2])

def get_completion_string(line):
    stack = []
    for c in line:
        if c in OPENS:
            stack.append(c)
        else:
            stack.pop()
    
    completion_list = []
    while stack:
        o = stack.pop()
        completion_list.append(CLOSES[OPENS.index(o)])
    return "".join(completion_list)

def score_completion_string(cs):
    score = 0
    for c in cs:
        score = score * 5
        score = score + SCORES[c]
    return score

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