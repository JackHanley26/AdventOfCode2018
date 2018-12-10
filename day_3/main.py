import re
from collections import defaultdict

with open('data.txt') as fp:
    data = [line.rstrip("\n\r") for line in fp]
grid_size = 1000


def part_1():
    print("Running part 1")

    def extraction(line):
        result = re.match(r'#([0-9]+)\ @\ ([0-9]+),([0-9]+):\ ([0-9]+)x([0-9]+)', line)
        return {'id': int(result.group(1)),
                'x': int(result.group(2)),
                'y': int(result.group(3)),
                'w': int(result.group(4)),
                'h': int(result.group(5))}

    def write_claim(c, fab):
        # writing top down
        start_across = c['x']
        start_down = c['y']
        width = c['w']
        height = c['h']

        # writing down
        for y in range(start_down, start_down + height):
            # writing across
            for x in range(start_across, start_across + width):
                fab[y][x].append(c['id'])


    # todo: fix this code

    fabric = [[[] for x in range(grid_size)] for x in range(grid_size)]

    claims = [extraction(line) for line in data]

    for claim in claims:
        write_claim(claim, fabric)

    print('Doing calc')
    overused = 0
    for line in fabric:
        for x in line:
            if len(x) >= 2:
                overused = overused + 1
    print(overused)

    return fabric

def part_2():
    print("Running part 2")

    fabric = part_1()
    not_used = set()
    for line in fabric:
        for x in line:
            if len(x) == 0:
                not_used.add(x['id'])

    print(not_used)


if __name__ == '__main__':
    part_1()
    part_2()
