# https://adventofcode.com/2022/day/4
# By Mikkel Tolstrup Jensen
from data.day4 import data


def puzzle1(data):
    count = 0
    for ranges in data:
        # Does one contain the other
        if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
            count += 1
            continue
        # Or does the second contain the first
        if ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
            count += 1
    return count


def puzzle2(data):
    count = 0
    for ranges in data:
        if ranges[2] <= ranges[0] <= ranges[3] or ranges[2] <= ranges[1] <= ranges[3]:
            count += 1
            continue
        if ranges[0] <= ranges[2] <= ranges[1] or ranges[0] <= ranges[3] <= ranges[1]:
            count += 1
    return count


if __name__ == "__main__":
    print(puzzle1(data))
    print(puzzle2(data))
