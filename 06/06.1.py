#!/usr/bin/env/python

SIM_DURATION = 80
REPRO_INTERVAL = 6
INIT_INTERVAL = 8

def main():
    with open("input.txt") as infile:
        in_str = infile.readline()
        fish_timers = [int(t) for t in in_str.split(",")]

        for d in range(SIM_DURATION):
            fish_timers = run_day(fish_timers)
        print(len(fish_timers))

def run_day(fish_timers):
    new_timers = []
    for t in fish_timers:
        if t > 0:
            new_timers.append(t-1)
        elif t == 0:
            new_timers.append(REPRO_INTERVAL)
            new_timers.append(INIT_INTERVAL)
        else:
            print("ERROR: NEGATIVE TIMER")
    return new_timers


if __name__ == "__main__":
    main()