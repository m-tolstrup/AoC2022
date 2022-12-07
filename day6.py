# https://adventofcode.com/2022/day/6
# By Mikkel Tolstrup Jensen
from data.day6 import data


def puzzle(data):
    for indx, letter in enumerate(data):
        if indx >= 13: # 3 or 13 depending on puzzle 1 or 2
            count = 0
            for c in data[indx-13:indx+1]: # slice of current letter and the 3 behind it
                if data[indx-13:indx+1].count(c) == 1:
                    count += 1
            if count == 14: # 4 or 14 depending on puzzle 1 or 2
                return indx + 1


if __name__ == '__main__':
    print(puzzle(data))
