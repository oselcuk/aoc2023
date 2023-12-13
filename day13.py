from itertools import chain, takewhile
from typing import Iterable

def get_axis(pic: list[list[bool]]) -> set[int]:
    def get_x(pic: list[list[bool]]) -> Iterable[int]:
        for i in range(1, len(pic)):
            if all(l == r for l, r in zip(pic[i-1::-1], pic[i:])):
                yield i
    return set(chain(get_x(list(zip(*pic))), (100 * axis for axis in get_x(pic))))


def part1(lines):
    result = 0
    while pic := list(map(str.strip, takewhile(lambda c: c != "\n", lines))):
        result += next(iter(get_axis([[c == "." for c in row] for row in pic])))
    return result


def part2(lines):
    t = 0
    def find_new(pic: list[list[bool]]) -> int:
        wrong = get_axis(pic)
        print(wrong)
        for i, row in enumerate(pic):
            for j, c in enumerate(row):
                pic[i][j] = not c
                new = get_axis(pic) - wrong
                if new:
                    return next(iter(new))
                pic[i][j] = c
        assert False
    result = 0
    while pic := list(map(str.strip, takewhile(lambda c: c != "\n", lines))):
        print(t)
        t += 1 
        result += find_new([[c == "." for c in row] for row in pic])
    return result