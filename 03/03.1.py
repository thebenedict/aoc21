#!/usr/bin/env/python

def main():
    lines = []
    with open("input.txt") as infile:
        for line in infile:
            lines.append(line.strip())

    sums = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in lines:
        for i, c in enumerate(line):
            sums[i] += int(c)
    gamma = []
    epsilon = []
    for s in sums:
        if s > (len(lines) / 2):
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")
    
    gamma_bin = "".join(gamma)
    epsilon_bin = "".join(epsilon)

    gamma_rate = int(gamma_bin, 2)
    epsilon_rate = int(epsilon_bin, 2)

    print(gamma_rate * epsilon_rate)

if __name__ == "__main__":
    main()