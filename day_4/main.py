import re
from dateutil.parser import parse


def get_id(l):
    return int(re.findall(r'\d+', l)[0])


def extract(i):
    r1 = re.match(r'\[([0-9-\ :]+)\]\ ([A-Za-z0-9#\ ]+)', i)
    return {'date': parse(r1.group(1)), 'log': r1.group(2)}


with open('data.txt') as fp:
    data = [extract(line.rstrip("\n\r")) for line in fp]
    data.sort(key=lambda x: x['date'])


def part_1():
    print("Running part 1")

    guard_map = dict()
    guard, sleep, wake = None, None, None
    for line in data:
        log = line.get('log')
        if 'begins' in log:
            guard = get_id(log)
            if guard not in guard_map:
                guard_map[guard] = [0 for x in range(60)]
        elif 'asleep' in log:
            sleep = line.get('date')
        elif 'wakes' in log:
            wake = line.get('date')
            for x in range(sleep.minute, wake.minute):
                guard_map[guard][x] = guard_map[guard][x] + 1

    sleepy_guard = max([(sum(guard_map[x]), x) for x in guard_map], key=lambda x: x[0])[1]
    print("Sleepy Guard: %d" % sleepy_guard)

    favorite_min_to_sleep = max([(v, idx) for idx, v in enumerate(guard_map[sleepy_guard])], key=lambda x: x[0])[1]
    print("Favorite minute to sleep: %d" % favorite_min_to_sleep)

    print("Answer 1: %d" % (sleepy_guard * favorite_min_to_sleep))


def part_2():
    print("Running part 2")


if __name__ == '__main__':
    part_1()
    part_2()
