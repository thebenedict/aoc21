#!/usr/bin/env python3

from collections import Counter
import sys

# ['B', 'C', 'F', 'H', 'K', 'N', 'O', 'P', 'S', 'V']

STEPS = 40

def main():
    with open("input.txt") as infile:
        rules = {}
        poly = infile.readline().strip()
        infile.readline()
        for line in infile.readlines():
            pair, elt = line.strip().split(" -> ")
            rules[pair] = elt
    # print(poly)
    # print(rules)

    # sortedrules = [(k, v) for k, v in sorted(rules.items(), key=lambda x: x[1])]
    # for s in sortedrules:
    #     print(s)
    # print(len(sortedrules))

    cache = {}
    for s in range(STEPS):
        print(s)
        poly = step(poly, rules, cache)
        #print(poly)

    c = Counter(poly)
    most = c.most_common(1)[0][1]
    least = c.most_common()[-1][1]
    print(most - least)

def step(poly, rules, cache):
    if len(poly) < 2:
        return poly
    # if poly in cache:
    #     print("\tcache {}".format(poly))
    if poly not in cache:
        mid = len(poly) // 2
        lower = step(poly[0:mid], rules, cache)
        upper = step(poly[mid:len(poly)], rules, cache)
        new_poly = f'{lower}{replace_pair(lower[-1] + upper[0], rules)}{upper}'
        cache[poly] = new_poly
        sys.intern(cache[poly])
    return cache[poly]

def replace_pair(pair, rules):
    if pair in rules:
        return rules[pair]
    else:
        return("")

if __name__ == "__main__":
    main()

