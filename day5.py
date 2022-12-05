# https://adventofcode.com/2022/day/5
# By Mikkel Tolstrup Jensen
from data.day5 import crates, moves


def puzzle1(crates, moves):
    for move in moves:
        box_count = move[1]
        frm = move[3] - 1
        to = move[5] - 1
        for i in range(box_count):
            box = crates[frm].pop()
            crates[to].append(box)

    boxes = ""
    for stack in crates:
        boxes += stack.pop()
    return boxes


def puzzle2(crates, moves):
    for move in moves:
        box_count = move[1]
        frm = move[3] - 1
        to = move[5] - 1
        temp = []
        for i in range(box_count):
            box = crates[frm].pop()
            temp.append(box)
        for i in range(box_count):
            box = temp.pop()
            crates[to].append(box)

    boxes = ""
    for stack in crates:
        boxes += stack.pop()
    return boxes


if __name__ == '__main__':
    # print(puzzle1(crates, moves))
    print(puzzle2(crates, moves))
