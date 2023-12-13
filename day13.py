from itertools import takewhile

def get_axis(pic: list[str]) -> int:
    def get_x(pic: list[str]) -> int:
        for i in range(1, len(pic)):
            if all(l == r for l, r in zip(pic[i-1::-1], pic[i:])):
                return i
        return 0
    return 100 * get_x(pic) or get_x(list(zip(*pic)))


def part1(lines):
    result = 0
    while pic := list(map(str.strip, takewhile(lambda c: c != "\n", lines))):
        result += get_axis(pic)
    return result