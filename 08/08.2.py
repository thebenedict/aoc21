#!/usr/bin/env python3

def main():
    output_values = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            patterns, output = line.split(" | ")
            patterns = ["".join(sorted(p)) for p in patterns.strip().split(" ")]
            output = ["".join(sorted(o)) for o in output.strip().split(" ")]
            output_values.append((patterns, output))

    output_sum = 0
    for patterns, outputs in output_values:
        decoder = [""] * 10
        patterns, decoder[1] = find_one(patterns)
        patterns, decoder[4] = find_four(patterns)
        patterns, decoder[7] = find_seven(patterns)
        patterns, decoder[8] = find_eight(patterns)
        patterns, decoder[9] = find_nine(patterns, decoder)
        patterns, decoder[0] = find_zero(patterns, decoder)
        patterns, decoder[6] = find_six(patterns)
        patterns, decoder[3] = find_three(patterns, decoder)
        patterns, decoder[5] = find_five(patterns, decoder)
        decoder[2] = patterns[0]

        decoded = []
        for num in outputs:
            decoded.append(str(decoder.index(num)))
        output_sum += int("".join(decoded))
    print(output_sum)

def find_one(patterns):
    for p in patterns:
        if len(p) == 2:
            patterns.remove(p)
            return(patterns, p)

def find_four(patterns):
    for p in patterns:
        if len(p) == 4:
            patterns.remove(p)
            return(patterns, p)

def find_seven(patterns):
    for p in patterns:
        if len(p) == 3:
            patterns.remove(p)
            return(patterns, p)

def find_eight(patterns):
    for p in patterns:
        if len(p) == 7:
            patterns.remove(p)
            return(patterns, p)

def find_nine(patterns, decoder):
    for p in patterns:
        if len(p) == 6 and set(decoder[4]) & set(p) == set(decoder[4]):
            patterns.remove(p)
            return(patterns, p)

def find_zero(patterns, decoder):
    for p in patterns:
        if len(p) == 6 and set(decoder[1]) & set(p) == set(decoder[1]):
            patterns.remove(p)
            return(patterns, p)

def find_six(patterns):
    for p in patterns:
        if len(p) == 6:
            patterns.remove(p)
            return(patterns, p)

def find_three(patterns, decoder):
    for p in patterns:
        if len(p) == 5 and set(decoder[1]) & set(p) == set(decoder[1]):
            patterns.remove(p)
            return(patterns, p)

def find_five(patterns, decoder):
    for p in patterns:
        if len(p) == 5 and len(set(decoder[6]) - set(p)) == 1:
            patterns.remove(p)
            return(patterns, p)

if __name__ == "__main__":
    main()
