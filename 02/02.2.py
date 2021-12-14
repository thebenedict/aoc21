#!/usr/bin/env/python

def main():
    vals = []
    with open("input.txt") as infile:
        for line in infile:
            dir, val = line.strip().split(" ")
            vals.append((dir, int(val)))
    
    aim = 0
    depth = 0
    hpos = 0
    for dir, val in vals:
        if dir == "forward":
            hpos += val
            depth += aim * val
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
        else:
            print("Invalid direction!")
    
    print(depth * hpos)

        

if __name__ == "__main__":
    main()