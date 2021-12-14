#!/usr/bin/env/python

from collections import defaultdict

def main():
    with open("input.txt") as infile:
        # list of start and endpoints as nested tuple: ((x_start, y_start), (x_end, y_end))
        vent_lines = []
        
        for line in infile.readlines():
            start, end = line.strip().split(" -> ")
            x_start, y_start = start.split(",")
            x_end, y_end = end.split(",")
            vent_lines.append(
                (
                    (int(x_start), int(y_start)),
                    (int(x_end), int(y_end))
                )
            )

        grid = defaultdict(int)
        for start_point, end_point in vent_lines:
            points = get_points(start_point, end_point)
            for p in points:
                grid[p] += 1

        overlap_count = len([c for c in grid.values() if c >= 2])
        print(overlap_count)

def get_points(start_point, end_point):
    points = []
    if start_point[0] == end_point[0]:
        start_y, end_y = sorted([start_point[1], end_point[1]])
        for y in range(start_y, end_y + 1):
            points.append((start_point[0], y))
        return points
    elif start_point[1] == end_point[1]:
        start_x, end_x = sorted([start_point[0], end_point[0]])
        for x in range(start_x, end_x + 1):
            points.append((x, start_point[1]))
        return points

    #diagnonal line
    x_start, y_start = start_point
    x_end, y_end = end_point

    x_sign = 1
    if x_end - x_start < 0:
        x_sign = -1
    x_vals = range(x_start, x_end + x_sign, x_sign)

    y_sign = 1
    if y_end - y_start < 0:
        y_sign = -1
    y_vals = range(y_start, y_end + y_sign, y_sign)

    return(zip(x_vals, y_vals))
if __name__ == "__main__":
    main()
