#!/usr/bin/env python3

X_MIN = 81
X_MAX = 129
Y_MIN = -150
Y_MAX = -108

def main():
    valid_velocities = set()
    for vxi in range(1, 130):
        for vyi in range(-150, 150):
            vx = vxi; vy = vyi
            x = 0; y = 0
            for i in range(300):
                x += vx; y += vy
                if vx > 0:
                    vx -= 1
                vy -= 1
                if x >= X_MIN and x <= X_MAX and y >= Y_MIN and y <= Y_MAX:
                    valid_velocities.add((vxi, vyi))
                    break
    print(len(valid_velocities))

if __name__ == "__main__":
    main()