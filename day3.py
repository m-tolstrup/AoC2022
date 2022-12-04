# https://adventofcode.com/2022/day/3
# By Mikkel Tolstrup Jensen
from data.day3 import data

# To subtract from ASCCI characters, s.t. the correct ammount of points is given
ASCII_CapA = 38
ASCII_LowA = 96


def puzzle1(data):
    accum = 0
    for rucksack in data:
        rl = len(rucksack)
        first = rucksack[:int(rl/2)]
        second = rucksack[int(rl/2):]
        for letter in first:
            if letter in second:
                ascii = ord(letter)
                accum += ascii - ASCII_CapA if ascii <= 90 else ascii - ASCII_LowA
                break
    return accum


def puzzle2(data):
    accum = 0
    for i in range(len(data)):
        if i % 3 == 0:
            for letter in data[i]:
                if letter in data[i+1] and letter in data[i+2]:
                    ascii = ord(letter)
                    accum += ascii - ASCII_CapA if ascii <= 90 else ascii - ASCII_LowA
                    break
    return accum


if __name__ == "__main__":
    print(puzzle1(data))
    print(puzzle2(data))
