import os
import sys

filename = __file__[:-5] + '-input'

with open(filename) as f:
    lines = f.read().splitlines()

    player_positions = list(map(lambda line: int(line[-1]), lines))

def roll_dice(dice_rolls, curr_dice_val):
    dice_rolls += 1
    curr_dice_val += 1
    return (dice_rolls, curr_dice_val)

player_index = 1
player_scores = [0, 0]

dice_rolls, curr_dice_val = 0, 0
while player_scores[player_index] < 1000:
    player_index = (player_index + 1) % 2

    for _ in range(3):
        dice_rolls, curr_dice_val = roll_dice(dice_rolls, curr_dice_val)
        player_positions[player_index] = (player_positions[player_index] + curr_dice_val)%10
    
    player_scores[player_index] += player_positions[player_index] if player_positions[player_index] != 0 else 10

print(dice_rolls * player_scores[(player_index+1)%2])




