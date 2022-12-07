# https://adventofcode.com/2022/day/7
# By Mikkel Tolstrup Jensen

# 115060550
# 13700


def puzzle1(data):
    folders = []
    for command in data:
        if command[1] == "cd" and command[2] != "..":
            folders.append({"name": command[2]})
        elif command[0].isnumeric():
            folder = folders[-1]
            folder[command[1]] = int(command[0])
        elif command[0] == "dir":
            folder = folders[-1]
            if "dir" in folder:
                folder["dir"].append(command[1])
            else:
                folder["dir"] = [command[1]]
    return folders


def subfolder_total(folders, subfolders):
    total = 0
    for folder in folders:
        accum = 0
        if folder["name"] in subfolders:
            for key in folder:
                if key == "dir":
                    accum += subfolder_total(folders, folder["dir"])
                elif key != "name":
                    accum += folder[key]
        total += accum
    return total


def folder_total(folders):
    total = 0
    for folder in folders:
        accum = 0
        for key in folder:
            if key == "dir":
                accum += subfolder_total(folders, folder["dir"])
            elif key != "name":
                accum += folder[key]
        if accum <= 10_000:
            total += accum
    return total


def puzzle2(data):
    pass


if __name__ == '__main__':
    # Actually parsing
    data = []
    with open("data/day7.txt") as f:
        for line in f:
            line = line[:len(line)-1]
            temp = line.split(" ")
            data.append(temp)

    folders = puzzle1(data)
    print(folder_total(folders))
    #print(puzzle2(data))
