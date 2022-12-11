# https://adventofcode.com/2022/day/11
# By Mikkel Tolstrup Jensen
import math


class Monkey:
    def __init__(self, items, op, op_num, divisor, true, false):
        self.items = items
        self.divisor = divisor
        self.op = op
        self.op_num = op_num
        self.true = true
        self.false = false
        self.inspected_items = 0

    def inspect_and_throw(self, item):
        # Count
        self.inspected_items += 1

        # Monkey inspects
        if self.op_num == "old":
            new_item = item * item
        else:
            if self.op == "*":
                new_item = item * self.op_num
            else:
                new_item = item + self.op_num

        # Monkey gets bored
        new_item = new_item / 3
        new_item = int(math.floor(new_item))

        # Test and throw
        test = new_item % self.divisor
        if test == 0: # Silly check, but makes the code readable :)
            return self.true, new_item
        else:
            return self.false, new_item


def puzzle1(monkeys):
    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                new_monkey, item = monkey.inspect_and_throw(item)
                monkeys[new_monkey].items.append(item)
            monkey.items.clear()


def puzzle2(data):
    pass


if __name__ == '__main__':
    monkeys = []
    items = []
    op = None
    op_num = None
    divisor = None
    true = None
    false = None
    with open("data/day11.txt") as f:
        for line in f:
            line = line[:len(line)-1]
            l = line.split(" ")
            l = [ele for ele in l if ele != ""]
            if len(l) >= 1:
                if l[0] == "Starting":
                    for num in range(2, len(l)):
                        ele = l[num]
                        if ele[-1] == ",":
                            ele = ele[:-1]
                        items.append(int(ele))
                elif l[0] == "Operation:":
                    if l[5].isnumeric():
                        op = l[4]
                        op_num = int(l[5])
                    else:
                        op = l[4]
                        op_num = l[5]
                elif l[0] == "Test:":
                    divisor = int(l[3])
                elif l[1] == "true:":
                    true = int(l[5])
                elif l[1] == "false:":
                    false = int(l[5])
            else:
                monkey = Monkey(items, op, op_num, divisor, true, false)
                monkeys.append(monkey)
                items = []

    for m in monkeys:
        print(m.items, m.op, m.op_num, m.divisor, m.true, m.false)

    puzzle1(monkeys)
    # low 63500
    count = []
    for monkey in monkeys:
        count.append(monkey.inspected_items)
    print(count)
