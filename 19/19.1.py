#!/usr/bin/env python3

from collections import Counter, defaultdict
from typing import Iterable

global all_beacons

ROTATIONS = [
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, -1]], [[1, 0, 0], [0, 0, 1], [0, -1, -0]],
    [[0, -1, 0], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
    [[0, 1, 0], [1, 0, 0], [0, 0, -1]], [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
    [[-1, 0, 0], [0, -1, 0], [0, 0, 1]], [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
    [[-1, 0, 0], [0, 1, 0], [0, 0, -1]], [[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
    [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
    [[0, 0, -1], [0, 1, 0], [1, 0, 0]], [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
    [[0, 0, 1], [0, -1, 0], [1, 0, 0]], [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
    [[0, 0, -1], [0, -1, 0], [-1, 0, -0]], [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
    [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], [[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
]

def main():
    scanners = []
    with open("input.txt") as infile:
        for line in infile.readlines():
            if "scanner" in line:
                beacons = []
            elif len(line.strip()) == 0:
                scanners.append(beacons)
            else:
                beacon = [int(b) for b in line.strip().split(",")]
                beacons.append(tuple(beacon))
    
    transformations = defaultdict(lambda: defaultdict(list))
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i != j:
                rotation_id, translation = check_overlap(i, j, scanners)
                if rotation_id:
                    transformations[j][i] = (rotation_id, translation)

    global all_beacons
    all_beacons = set(scanners[0])
    for s, beacons in enumerate(scanners):
        transform_to_zero(beacons, s, [], transformations)
    print(len(all_beacons))

def transform_to_zero(beacons, sensor, visited, transformations):
    visited.append(sensor)
    if sensor == 0:
        global all_beacons
        all_beacons.update(beacons)
        return
    else:
        for neighbor in transformations[sensor]:
            if neighbor not in visited:
                rotation_id, translation = transformations[sensor][neighbor]
                beacons = rotate_beacons(rotation_id, beacons)
                beacons = translate_beacons(translation, beacons)            
                transform_to_zero(beacons, neighbor, visited, transformations)

def check_overlap(scanner_a_id:int, scanner_b_id:int, scanners:list):
    all_orientations_b = all_orientations_for(scanner_b_id, scanners)
    for o, ob in enumerate(all_orientations_b):
        deltas = []
        for beacon_b in ob:
            for beacon_a in scanners[scanner_a_id]:
                deltas.append(delta(beacon_a, beacon_b))
        if Counter(deltas).most_common(1)[0][1] >= 6:
            return o, tuple(Counter(deltas).most_common(1)[0][0])
    return None, None

def rotate_beacons(rotation_id:int, beacons:Iterable) -> list:
    rotated = []
    for b in beacons:
        rotated.append(apply_rotation(b, ROTATIONS[rotation_id]))
    return rotated

def translate_beacons(v:tuple, beacons:Iterable) -> list:
    translated = []
    for b in beacons:
        translated.append((
            b[0] - v[0],
            b[1] - v[1],
            b[2] - v[2]
        ))
    return translated

# returns the full list of beacons from a scanner in each of the 24 possible orientations
def all_orientations_for(scanner_id:int, scanners:list) -> list:
    all_orientations = []
    for beacon in scanners[scanner_id]:
        tmp = []
        for r in ROTATIONS:
            tmp.append(apply_rotation(beacon, r))
        all_orientations.append(tmp)
    return list(zip(*all_orientations))

def apply_rotation(b:tuple, r:list):
    x = b[0] * r[0][0] + b[1] * r[1][0] + b[2] * r[2][0]
    y = b[0] * r[0][1] + b[1] * r[1][1] + b[2] * r[2][1]
    z = b[0] * r[0][2] + b[1] * r[1][2] + b[2] * r[2][2]
    return (x, y, z)

def delta(b1, b2):
    return(
        b2[0] - b1[0], 
        b2[1] - b1[1], 
        b2[2] - b1[2], 
    )

if __name__ == "__main__":
    main()