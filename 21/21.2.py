#!/usr/bin/env python3

from collections import defaultdict

BOARD_SIZE = 10
ROLLS_PER_TURN = 3
WIN_SCORE = 21

# All possible outcomes of three consecutive dice rolls as sum: number of universes
ROLLS = { 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }

# my input
P1_START = 1
P2_START = 5

# example
# P1_START = 4
# P2_START = 8

def main():
    turn_count = 0
    game_states = defaultdict(int, {(P1_START, 0, P2_START, 0): 1})

    p1_wins = p2_wins = 0
    while len(game_states.keys()) > 0:
        player = turn_count % 2
        new_states = defaultdict(int)
        for state, universe_count in game_states.items():
            p1_pos, p1_score, p2_pos, p2_score = state
            for spaces_to_move, move_frequency in ROLLS.items():
                if player == 0: # player 1
                    new_p1_pos = (p1_pos + spaces_to_move) % BOARD_SIZE
                    if new_p1_pos == 0:
                        new_p1_score = p1_score + 10
                    else:
                        new_p1_score = p1_score + new_p1_pos
                    new_states[(new_p1_pos, new_p1_score, p2_pos, p2_score)] += universe_count * move_frequency
                elif player == 1: # player 2
                    new_p2_pos = (p2_pos + spaces_to_move) % BOARD_SIZE
                    if new_p2_pos == 0:
                        new_p2_score = p2_score + 10
                    else:
                        new_p2_score = p2_score + new_p2_pos
                    new_states[(p1_pos, p1_score, new_p2_pos, new_p2_score)] += universe_count * move_frequency
        
        game_states = defaultdict(int, new_states)
        for state, game_count in new_states.items():
            p1_pos, p1_score, p2_pos, p2_score = state
            if p1_score >= WIN_SCORE:
                p1_wins += game_count
                del game_states[state]
            elif p2_score >= WIN_SCORE:    
                p2_wins += game_count
                del game_states[state]
        
        turn_count += 1 

    print(max((p1_wins, p2_wins)))

if __name__ == "__main__":
    main()