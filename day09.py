from itertools import pairwise

def part1(lines):
    seqs = (list(map(int, line.split())) for line in lines)
    return sum(map(extrapolate, seqs))

def extrapolate(seq: list[int]) -> int:
    if not any(seq):
        return 0
    diffs = list(map(lambda pair: pair[1] - pair[0], pairwise(seq)))
    return seq[-1] + extrapolate(diffs)
    