# https://adventofcode.com/2022/day/9
# By Mikkel Tolstrup Jensen
from data.day9 import data


def puzzle(moves, rope):
    x = 0
    y = 1
    l = len(rope)
    tail_set = {(0,0)}
    for move in moves:
        for i in range(move[1]):
            if move[0] == "R":
                rope[0][x] += 1
            elif move[0] == "L":
                rope[0][x] -= 1
            elif move[0] == "U":
                rope[0][y] += 1
            else:
                rope[0][y] -= 1

            for r in range(1, l):
                px, py = rope[r-1][x], rope[r-1][y]
                cx, cy = rope[r][x], rope[r][y]
                dx, dy = px - cx, py - cy

                if dx == 2:
                    rope[r][x] += 1
                    if dy >= 1:
                        rope[r][y] += 1
                    elif dy <= -1:
                        rope[r][y] -= 1
                elif dx == -2:
                    rope[r][x] -= 1
                    if dy >= 1:
                        rope[r][y] += 1
                    elif dy <= -1:
                        rope[r][y] -= 1
                elif dy == 2:
                    rope[r][y] += 1
                    if dx >= 1:
                        rope[r][x] += 1
                    elif dx <= -1:
                        rope[r][x] -= 1
                elif dy == -2:
                    rope[r][y] -= 1
                    if dx >= 1:
                        rope[r][x] += 1
                    elif dx <= -1:
                        rope[r][x] -= 1
            print(rope)
            tail_set.add((rope[-1][x], rope[-1][y]))

    return len(tail_set)


if __name__ == '__main__':
    rope = []
    for i in range(10):
        rope.append([0,0])
    # low 337
    print(puzzle(data, rope))
