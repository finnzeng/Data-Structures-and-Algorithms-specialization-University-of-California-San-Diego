# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter


Segment = namedtuple('Segment', 'start end')


def optimal_point_naive(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

def optimal_points(segments):
#     print(segments)
    points = []
    segments = sorted(segments, key=attrgetter('end'))
    curr_right_end = segments[0].end
    points.append(curr_right_end)
    i = 1
    while i < len(segments):
        if curr_right_end < segments[i].start:
            curr_right_end = segments[i].end
            points.append(curr_right_end)
        i += 1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
