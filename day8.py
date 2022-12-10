# https://adventofcode.com/2022/day/8
# By Mikkel Tolstrup Jensen
from data.day8 import data, test


def puzzle1(data, marker_map):
    # Right
    for i in range(len(data)):
        tallest_seen = -1
        for j in range(len(data[i])):
            num = int(data[i][j])
            if tallest_seen < num:
                temp = marker_map[i]
                temp = temp[:j] + "x" + temp[j+1:]
                marker_map[i] = temp
                tallest_seen = num

    # Left
    for i in reversed(range(len(data))):
        tallest_seen = -1
        for j in reversed(range(len(data[i]))):
            num = int(data[i][j])
            if tallest_seen < num:
                temp = marker_map[i]
                temp = temp[:j] + "x" + temp[j+1:]
                marker_map[i] = temp
                tallest_seen = num

    # Down
    for i in range(len(data)):
        tallest_seen = -1
        for j in range(len(data[i])):
            num = int(data[j][i])
            if tallest_seen < num:
                temp = marker_map[j]
                temp = temp[:i] + "x" + temp[i+1:]
                marker_map[j] = temp
                tallest_seen = num

    # Up
    for i in reversed(range(len(data))):
        tallest_seen = -1
        for j in reversed(range(len(data[i]))):
            num = int(data[j][i])
            if tallest_seen < num:
                temp = marker_map[j]
                temp = temp[:i] + "x" + temp[i+1:]
                marker_map[j] = temp
                tallest_seen = num

    return sum([entry.count("x") for entry in marker_map])


def look_right(data, i, j):
    if j == len(data) - 1:
        return 0
    count = 0
    height = data[i][j]
    for k in range(j+1, len(data)):
        if data[i][k] < height:
            count += 1
        else:
            return count + 1
    return count


def look_left(data, i, j):
    if j == 0:
        return 0
    count = 0
    height = data[i][j]
    for k in range(j-1, -1, -1):
        if data[i][k] < height:
            count += 1
        else:
            return count + 1
    return count


def look_down(data, i, j):
    if i == len(data) - 1:
        return 0
    count = 0
    height = data[i][j]
    for k in range(len(data)-1, i, -1):
        if data[k][j] < height:
            count += 1
        else:
            return count + 1
    return count


def look_up(data, i, j):
    if i == 0:
        return 0
    count = 0
    height = data[i][j]
    for k in range(i-1, -1, -1):
        if data[k][j] < height:
            count += 1
        else:
            return count + 1
    return count


def puzzle2(data):
    length = len(data)
    best_view_score = 0
    for i in range(length):
        for j in range(length):
            r = look_right(data, i, j)
            l = look_left(data, i, j)
            d = look_down(data, i, j)
            u = look_up(data, i, j)
            score = r * l * d * u
            if score > best_view_score:
                best_view_score = score

    return best_view_score


if __name__ == '__main__':
    marker_map = []
    for entry in data:
        marker_map.append("#"*len(entry))
    print(puzzle1(data, marker_map))
    # low 1116
    # 28800
    # 321651
    # 1254528
    # 1254528
    # high 865592
    print(puzzle2(data))
