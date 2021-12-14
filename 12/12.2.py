#!/usr/bin/env python3

from typing import DefaultDict

paths = []
g = DefaultDict(list)

def main():
    global g
    with open("input.txt") as infile:
        for line in infile.readlines():
            caves = line.strip().split("-")
            g[caves[0]].append(caves[1])
            g[caves[1]].append(caves[0])

    global paths
    dfs(["start"])
    print(len(paths))

def dfs(path):
    global paths
    source = path[-1]
    if source == "end":
        paths.append(path)
        return

    for n in g[source]:
        if is_allowed(n, path):
            dfs(path[:] + [n])

def is_allowed(n, path):
    if n.isupper() or n not in path:
        return True
    lowers = [l for l in path if l.islower()]
    if n.islower() and n!= "start" and len(lowers) == len(set(lowers)):
        return True
    return False

if __name__ == "__main__":
    main()