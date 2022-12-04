# https://adventofcode.com/2022/day/2
# By Mikkel Tolstrup Jensen
from data.day2 import data


def get_points1(match):
    # Bonus points for choosing rock, paper, or scissor
    bp = 1 if match[1] == "X" else 2 if match[1] == "Y" else 3
    # Turn match result into an integer (ASCII)
    match = [ord(match[0]), ord(match[1])]
    result = match[1] - match[0]
    # Give points for win, lose, or draw
    # Draw = 23, win = 21, or 24, else lose
    p = 3 if result == 23 else 6 if result == 21 or result == 24 else 0
    return p + bp


def puzzle1(data):
    return sum([get_points1(match) for match in data])


def get_points2(match):
    # Points for the match, whether we have to win, lose, or draw
    p = 0 if match[1] == "X" else 3 if match[1] == "Y" else 6
    # Map rock, paper, and scissor to 0, 1, and 2
    opp_choice = ord(match[0]) - 65
    # Modulo to determine own choice
    if match[1] == "X": # lose
        bp = (opp_choice + 2) % 3
    elif match[1] == "Y": # draw
        bp = opp_choice
    else: # win
        bp = (opp_choice + 1) % 3
    # add 1 to bp to match points given
    return p + bp + 1


def puzzle2(data):
    return sum([get_points2(match) for match in data])


if __name__ == "__main__":
    print(puzzle1(data))
    print(puzzle2(data))
