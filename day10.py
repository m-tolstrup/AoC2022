# https://adventofcode.com/2022/day/10
# By Mikkel Tolstrup Jensen
from data.day10 import data


def puzzle1(data):
    interesting = [20, 60, 100, 140, 180, 220]
    observations = []
    cycle = 1
    X = 1
    for operation in data:
        if operation[0] == "noop":
            if cycle in interesting:
                observations.append(cycle * X)
            cycle += 1
        if operation[0] == "addx":
            if cycle in interesting:
                observations.append(cycle * X)
            cycle += 1
            if cycle in interesting:
                observations.append(cycle * X)
            cycle += 1
            X += operation[1]
    return sum(observations)


def puzzle2(data):
    screen = []
    for i in range(6):
        screen.append("."*40)

    cycle = 0
    line = 0
    X = 1

    for operation in data:
        if operation[0] == "noop":
            if X-1 <= cycle <= X+1:
                sl = screen[line]
                sl = sl[:cycle] + "#" + sl[cycle+1:]
                screen[line] = sl
            cycle += 1
            if cycle == 40:
                cycle -= 40
                line += 1
        if operation[0] == "addx":
            if X-1 <= cycle <= X+1:
                sl = screen[line]
                sl = sl[:cycle] + "#" + sl[cycle+1:]
                screen[line] = sl
            cycle += 1
            if cycle == 40:
                cycle -= 40
                line += 1
            if X-1 <= cycle <= X+1:
                sl = screen[line]
                sl = sl[:cycle] + "#" + sl[cycle+1:]
                screen[line] = sl
            cycle += 1
            if cycle == 40:
                cycle -= 40
                line += 1
            X += operation[1]

    for line in screen:
        print(line)


if __name__ == '__main__':
    print(puzzle1(data))
    puzzle2(data)
