import os
import sys
from itertools import product

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()

    player_positions = list(map(lambda line: int(line[-1]), lines))

turn_rolls = product([1,2,3], repeat=3)

turn_sums = list(map(sum, turn_rolls))

turn_sum_set = set(turn_sums)

turn_sum_occurances = {
    s: turn_sums.count(s) for s in turn_sum_set
}

found_outcomes = {}

def player_turn(player_index, player_positions, player_scores):    
    outcome = [0, 0]
    if (player_index, tuple(player_positions), tuple(player_scores)) in found_outcomes:
        return found_outcomes[(player_index, tuple(player_positions), tuple(player_scores))]    
    for roll_sum in turn_sum_set:
        local_scores = player_scores[:]
        local_positions = player_positions[:]

        local_positions[player_index] = (local_positions[player_index] + roll_sum)%10
        local_scores[player_index] += local_positions[player_index] if local_positions[player_index] != 0 else 10

        local_outcome = [0, 0]

        if local_scores[player_index] > 20:
            local_outcome[player_index] = turn_sum_occurances[roll_sum]
        else:
            local_outcome = list(map(lambda out: out*turn_sum_occurances[roll_sum], player_turn((player_index+1)%2, local_positions, local_scores)))

        outcome[0] += local_outcome[0]
        outcome[1] += local_outcome[1]
    found_outcomes[(player_index, tuple(player_positions), tuple(player_scores))] = outcome
    return outcome
outcome = player_turn(0, player_positions[:], [0, 0])
print(max(outcome))

