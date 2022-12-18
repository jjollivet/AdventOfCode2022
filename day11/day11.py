import re

class Monkey:
    def __init__(self, operation, divisible_by, if_true, if_false, num_inspections):
        self.num_inspections = num_inspections
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false

    def inspect_and_throw(self, object):
        self.num_inspections += 1
        old = object
        new = eval(self.operation)
        new = new // 3
        if new % self.divisible_by == 0:
            return (self.if_true, new)
        else:
            return (self.if_false, new)

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    num_monkeys = int(len(data)/6)
    num_rounds = 20
    list_of_items = []
    list_of_monkeys = []

    for i in range(num_monkeys):
        # create list of worry items
        items = re.findall('\d+', data[i*6+1])
        for item in range(len(items)):
            items[item] = int(items[item])
        list_of_items.append(items)

        # create list of monkeys
        div_by = re.findall('\d+', data[i*6+3])
        iftrue = re.findall('\d+', data[i*6+4])
        iffalse = re.findall('\d+', data[i*6+5])
        list_of_monkeys.append(Monkey(data[i*6+2][19:], int(div_by[0]), int(iftrue[0]), int(iffalse[0]),0))

    # Part 1
    for round in range(num_rounds):
        for monkey in range(num_monkeys):
            temp_list_of_items = list_of_items[monkey].copy()
            #print(temp_list_of_items)
            for item in temp_list_of_items:
                # Each monkey evaluates, gets bored, and throws each item
                throw_to, worry_level = list_of_monkeys[monkey].inspect_and_throw(item)
                list_of_items[monkey].pop(0)
                list_of_items[throw_to].append(worry_level)

    # Retreive all inspection numbers and find maximum two
    num_inspects = []
    for monkey in range(num_monkeys):
        num_inspects.append(list_of_monkeys[monkey].num_inspections)
    max_inspect = max(num_inspects)
    num_inspects.remove(max_inspect)
    max_inspect_2 = max(num_inspects)
    print(f'Part 1 Monkey business is {max_inspect * max_inspect_2}')

main()
