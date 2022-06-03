import sys
import copy
import collections
import pprint

pp = pprint.PrettyPrinter(indent=4)

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

def main():
    print('first')
    first()
    print('-------')
    # print('second')
    # second()
    # print('-------')


def load_data():
    with open(sys.argv[1]) as f:
        data = f.read().rstrip().split('\n')

    return data

def first():
    data = load_data()
    out = []
    for line in data:
        start = line.split(' ')[0]
        end = line.split(' ')[2]
        out.append(create_line(start, end))

    cnt = collections.Counter()
    for line in out:
        for point in line:
            cnt[point] += 1

    p = {key:value for key, value in cnt.items() if value > 1}
    print(len(p))

# def second():
#     data = load_data()
#     out = []
#     for line in data:
#         start = line.split(' ')[0]
#         end = line.split(' ')[2]
#         out.append(create_line(start, end, diag=True))
#         print(start, end, out[-1])

#     cnt = collections.Counter()
#     for line in out:
#         for point in line:
#             cnt[point] += 1

#     p = {key:value for key, value in cnt.items() if value > 1}
#     print(len(p))

def create_line(start, end, diag=False):
    start = start.split(',')
    end = end.split(',')
    start = Coordinate(int(start[0]), int(start[1]))
    end = Coordinate(int(end[0]), int(end[1]))

    if start.x == end.x:
        return [Coordinate(start.x, i) for i in range(min(start.y,end.y), max(start.y,end.y)+1)]
    if start.y == end.y:
        return [Coordinate(i, start.y) for i in range(min(start.x,end.x), max(start.x,end.x)+1)]
    if diag:
        mulx = 1 if start.x < end.x else -1
        muly = 1 if start.y < end.y else -1

        return [Coordinate(start.x + (mulx*i), start.y + (muly*i)) for i in range( abs(start.x - end.x)+1)]

    return []

if __name__ == '__main__':
    main()