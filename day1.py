# https://adventofcode.com/2022/day/1
# By Mikkel Tolstrup Jensen
from data.day1 import data


def puzzle1(data):
    return max([sum(l) for l in data])


def puzzle2(data):
    calorie_sums = [sum(l) for l in data]
    total = 0
    for _ in range(3):
        temp = max(calorie_sums)
        total += temp
        calorie_sums.remove(temp)
    return total


if __name__ == '__main__':
    print(puzzle1(data))
    print(puzzle2(data))
