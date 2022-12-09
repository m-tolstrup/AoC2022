# https://adventofcode.com/2022/day/7
# By Mikkel Tolstrup Jensen
def puzzle1(commands, folder):
    nested_cd_seen = False
    root_set = False
    level = 0
    # Have a bowl of spaghetti on me
    for indx, command in enumerate(commands):
        if "cd" in command and ".." not in command:
            if not root_set: # first cd seen becomes the directory we work on
                folder["name"] = command[2]
                folder["total"] = 0
                root_set = True
            elif level == 0: # future cds become subfolders, if they are on the correct subfolder level
                nested_cd_seen = True
                if "dir" in folder:
                    folder["dir"].append(puzzle1(commands[indx:], {}))
                    level += 1
                else:
                    folder["dir"] = [puzzle1(commands[indx:], {})]
                    level += 1
            else:
                level += 1
        elif command[0].isnumeric() and not nested_cd_seen: # all integers come before the forst nested cd
            folder["total"] += int(command[0])
        elif ".." in command: # count levels, if we return to zero, the folder we are working on is done
            if level != 0:
                level -= 1
            else:
                return folder
    return folder


results = []


def puzzle1_count(folder):
    local = 0
    subfolders = 0

    print(folder)
    for key in folder:
        if key == "total":
            local += folder[key]
        elif key == "dir":
            subfolders = sum([puzzle1_count(f) for f in folder["dir"]])

    if local + subfolders <= 100_000:
        results.append(local+subfolders)

    return local + subfolders


if __name__ == '__main__':
    # Actually parsing :)
    data = []
    with open("data/day7.txt") as f:
        for line in f:
            line = line[:len(line)-1]
            temp = line.split(" ")
            data.append(temp)

    # Puzzle 1
    root_folder = puzzle1(data, {})
    total = puzzle1_count(root_folder)
    print(sum(results))
