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

        grid = defaultdict(lambda: defaultdict(int))
        for start_point, end_point in vent_lines:
            points = get_points(start_point, end_point)
            for x, y in points:
                grid[x][y] += 1

        overlap_count = 0
        for x, row in grid.items():
            counts = row.values()
            overlap_count += len([c for c in counts if c >= 2])
        print(overlap_count)

def get_points(start_point, end_point):
    points = []
    if start_point[0] == end_point[0]:
        start_y, end_y = sorted([start_point[1], end_point[1]])
        for y in range(start_y, end_y + 1):
            points.append((start_point[0], y))
    elif start_point[1] == end_point[1]:
        start_x, end_x = sorted([start_point[0], end_point[0]])
        for x in range(start_x, end_x + 1):
            points.append((x, start_point[1]))
    return points
    
if __name__ == "__main__":
    main()
