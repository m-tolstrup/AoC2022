# https://adventofcode.com/2022/day/7
# By Mikkel Tolstrup Jensen

# 13700 low
# 1627406 high


def puzzle1(commands, folder):
    nested_cd_seen = False
    root_set = False
    layer = 0
    for indx, command in enumerate(commands):
        if "cd" in command and ".." not in command:
            if not root_set:
                folder["name"] = command[2]
                root_set = True
            elif layer == 0:
                nested_cd_seen = True
                if "dir" in folder:
                    folder["dir"].append(puzzle1(commands[indx:], {}))
                    layer += 1
                else:
                    folder["dir"] = [puzzle1(commands[indx:], {})]
                    layer += 1
            else:
                layer += 1
        elif command[0].isnumeric() and not nested_cd_seen:
            if "total" in folder:
                folder["total"] += int(command[0])
            else:
                folder["total"] = int(command[0])
        elif ".." in command:
            if layer != 0:
                layer -= 1
            else:
                return folder
    return folder


def puzzle1_count(folder):
    local = 0
    subfolders = 0

    for key in folder:
        if key == "total":
            local += folder[key]
        elif key == "dir":
            subfolders = sum([puzzle1_count(f) for f in folder["dir"]])

    total = local + subfolders * 2
    print(folder, local, total)

    if total <= 100_000:
        return total
    else:
        return subfolders


if __name__ == '__main__':
    # Actually parsing
    data = []
    with open("data/day7.txt") as f:
        for line in f:
            line = line[:len(line)-1]
            temp = line.split(" ")
            data.append(temp)

    root_folder = puzzle1(data, {})
    print(puzzle1_count(root_folder))
