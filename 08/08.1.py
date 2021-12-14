#!/usr/bin/env python3

def main():
    output_values = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            output_values.extend(line.split(" | ")[1].strip().split(" "))

    count = 0
    for o in output_values:
        if len(o) in [2, 4, 3, 7]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()