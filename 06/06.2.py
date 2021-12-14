#!/usr/bin/env/python

from collections import deque

SIM_DURATION = 256
REPRO_INTERVAL = 6
INIT_INTERVAL = 8

def main():
    with open("input.txt") as infile:
        in_str = infile.readline()
        fish_list = [int(t) for t in in_str.split(",")]
        fish_timers = deque([0] * (INIT_INTERVAL + 1))
        for t in fish_list:
            fish_timers[t] += 1

        for d in range(SIM_DURATION):
            fish_timers = run_day(fish_timers)
        print(sum(fish_timers))

def run_day(fish_timers):
    new_fish_count = fish_timers.popleft()
    fish_timers[REPRO_INTERVAL] += new_fish_count
    fish_timers.append(new_fish_count)
    return fish_timers

if __name__ == "__main__":
    main()