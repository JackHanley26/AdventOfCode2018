import re
from collections import defaultdict

with open('data.txt') as fp:
    data = [line.rstrip("\n\r") for line in fp]
grid_size = 1000

overlaps = {}


def part_1():
    print("Running part 1")

    def extraction(line):
        r = re.match(r'#([0-9]+)\ @\ ([0-9]+),([0-9]+):\ ([0-9]+)x([0-9]+)', line)
        return {'id': int(r.group(1)), 'x': int(r.group(2)), 'y': int(r.group(3)), 'w': int(r.group(4)),
                'h': int(r.group(5))}

    claims = [extraction(line) for line in data]

    fabric = defaultdict(list)
    global overlaps

    for c in claims:
        overlaps[c['id']] = set()
        for y in range(c['y'], c['y'] + c['h']):
            for x in range(c['x'], c['x'] + c['w']):

                if fabric[(x, y)]:
                    for number in fabric[(x, y)]:
                        overlaps[number].add(c['id'])
                        overlaps[c['id']].add(number)
                fabric[(x, y)].append(c['id'])

    print(len([b for b in fabric if len(fabric[b]) > 1]))


def part_2():
    print("Running part 2")
    global overlaps
    print([b for b in overlaps if len(overlaps[b]) == 0][0])


if __name__ == '__main__':
    part_1()
    part_2()
