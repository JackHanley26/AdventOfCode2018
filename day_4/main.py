import re
from dateutil.parser import parse
from collections import defaultdict


def get_id(l):
    return int(re.findall(r'\d+', l)[0])


def extract(i):
    r1 = re.match(r'\[([0-9-\ :]+)\]\ ([A-Za-z0-9#\ ]+)', i)
    return {'date': parse(r1.group(1)), 'log': r1.group(2)}


with open('data.txt') as fp:
    data = [extract(line.rstrip("\n\r")) for line in fp]
    data.sort(key=lambda x: x['date'])


def make_map():
    g_map = defaultdict(lambda: [0 for x in range(60)])
    guard, sleep, wake = None, None, None
    for line in data:
        log = line.get('log')
        if 'begins' in log:
            guard = get_id(log)
        elif 'asleep' in log:
            sleep = line.get('date')
        elif 'wakes' in log:
            wake = line.get('date')
            for x in range(sleep.minute, wake.minute):
                g_map[guard][x] = g_map[guard][x] + 1
    return g_map


guard_map = make_map()


def part_1(m):
    print("\nRunning part 1")

    sleepy_guard = max([(sum(m[x]), x) for x in m], key=lambda x: x[0])[1]
    print("Sleepy Guard: %d" % sleepy_guard)

    favorite_min_to_sleep = max([(v, idx) for idx, v in enumerate(m[sleepy_guard])], key=lambda x: x[0])[1]
    print("Favorite minute to sleep: %d" % favorite_min_to_sleep)

    print("Answer 1: %d" % (sleepy_guard * favorite_min_to_sleep))


def part_2(m):
    print("\nRunning part 2")

    gid = max([(k, max(m[k])) for k in m], key=lambda x: x[1])[0]
    minute = max([(idx, v) for idx, v in enumerate(m[gid])], key=lambda x: x[1])[0]
    print("Answer part 2: %d" % (minute * gid))


if __name__ == '__main__':
    part_1(guard_map)
    part_2(guard_map)
