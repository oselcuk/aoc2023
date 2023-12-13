from typing import Iterable
from bisect import bisect_left
import itertools


def solve(lines: Iterable[str], expansion_factor: int) -> int:
    sky = [[c == "#" for c in row.strip()] for row in lines]
    empty_rows = [i for i, row in enumerate(sky) if not any(row)]
    transposed = list(zip(*sky))
    empty_cols = [i for i, col in enumerate(transposed) if not any(col)]
    galaxies: set[tuple[int, int]] = set()
    for i, row in enumerate(sky):
        for j, c in enumerate(row):
            if c:
                galaxies.add((i + bisect_left(empty_rows, i) * expansion_factor, j + bisect_left(empty_cols, j) * expansion_factor))
    return sum(abs(x0-x1) + abs(y0-y1) for ((x0, y0), (x1, y1)) in itertools.combinations(galaxies, 2))


def part1(lines):
    return solve(lines, 1)


def part2(lines):
    return solve(lines, 1000000 - 1)