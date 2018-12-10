with open('data.txt') as fp:
    data = [line.rstrip("\n\r") for line in fp]


def part_1():
    print("Running part 1")
    value = 0
    for line in data:
        if '-' in line:
            v = abs(int(line))
            value = value - v
        else:
            v = abs(int(line))
            value = value + v

    print("Answer: %d" % value)
    print("Finished part 1")
    print("---------------\n")


def part_2():
    # todo: make this efficient
    print("Running part 2")

    value = 0
    my_list = []
    run = True
    while run:
        for line in data:
            if '-' in line:
                v = abs(int(line))
                value = value - v
            else:
                v = abs(int(line))
                value = value + v

            if value in my_list:
                print("found it: %d" % value)
                run = False
                break
            my_list.append(value)
    print("Finished part 2")
    print("---------------\n")


if __name__ == '__main__':
    part_1()
    part_2()
