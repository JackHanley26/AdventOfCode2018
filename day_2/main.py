from copy import deepcopy

with open('data.txt') as fp:
    data = [line.rstrip("\n\r") for line in fp]

two = 0
three = 0


def part_1():
    print("Running part 1")

    def count(s, map):
        c = s[:1]
        if c:
            if c not in map:
                map[c] = 0
            map[c] = map[c] + 1
            return count(s[1:], map)
        else:
            return map

    def find(map):
        found_two = False
        found_three = False
        for k in map:
            if not found_two and map[k] == 2:
                found_two = True
                global two
                two = two + 1

            elif not found_three and map[k] == 3:
                found_three = True
                global three
                three = three + 1
            if found_two and found_three:
                break

    for line in data:
        find(count(line, {}))

    value = two * three
    print("Answer: %d" % value)
    print("Finished part 1")
    print("---------------")


def part_2():
    print("Running part 2")

    my_data = [{'id': d, 'count': 0} for d in data]

    def check(i, s, d):
        if i < len(s):
            for line in d:
                if s[i] != line['id'][i]:
                    line['count'] = line['count'] + 1
            # filter. there is no need to return data that has already been disqualified
            return check(i + 1, s, list(filter(lambda x: x['count'] < 2, d)))
        else:
            return d

    def get_clean(x, y):
        for i in range(len(x)):
            if x[i] != y[i]:
                return x[:i] + x[i + 1:]

    for idx, row in enumerate(my_data):
        d = deepcopy(my_data)
        results = check(0, row['id'], d[idx:])
        results = list(filter(lambda x: x['count'] == 1, results))
        if len(results) > 0:
            print('Found it: this is the clean string')
            print(get_clean(row['id'], results[0]['id']))
    print("Finished part 2")
    print("---------------")


if __name__ == '__main__':
    part_1()
    part_2()
