#!/usr/bin/env python3

BOARD_SIZE = 10
ROLLS_PER_TURN = 3
WIN_SCORE = 1000

P1_START = 1
P2_START = 5

def main():
    die = 0
    turn_count = 0
    # board position and scores for [p1, p2]
    pos = [P1_START, P2_START] 
    score = [0, 0]

    while score[0] < WIN_SCORE and score[1] < WIN_SCORE:
        player = turn_count % 2
        spaces_to_move = 0
        for _ in range(ROLLS_PER_TURN):
            if die == 100:
                die = 1
            else:
                die += 1
            spaces_to_move += die
        pos[player] = (pos[player] + spaces_to_move) % BOARD_SIZE
        if pos[player] == 0:
            score[player] += 10
        else:
            score[player] += pos[player]
        turn_count += 1

    die_rolls = turn_count * ROLLS_PER_TURN
    print(min(score) * die_rolls)

if __name__ == "__main__":
    main()