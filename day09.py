from itertools import pairwise

def part1(lines):
    seqs = (list(map(int, line.split())) for line in lines)
    return sum(map(extrapolate_next, seqs))


def part2(lines):
    seqs = (list(map(int, line.split())) for line in lines)
    return sum(map(extrapolate_prev, seqs))


def diffs(seq: list[int]) -> list[int]:
    return list(map(lambda pair: pair[1] - pair[0], pairwise(seq)))


def extrapolate_next(seq: list[int]) -> int:
    if not any(seq):
        return 0
    return seq[-1] + extrapolate_next(diffs(seq))


def extrapolate_prev(seq: list[int]) -> int:
    if not any(seq):
        return 0
    return seq[0] - extrapolate_prev(diffs(seq))