from typing import Iterable
from bisect import bisect_left
import itertools

def part1(lines: Iterable[str]) -> int:
    sky = [[c == "#" for c in row.strip()] for row in lines]
    empty_rows = [i for i, row in enumerate(sky) if not any(row)]
    transposed = list(zip(*sky))
    empty_cols = [i for i, col in enumerate(transposed) if not any(col)]
    galaxies: set[tuple[int, int]] = set()
    for i, row in enumerate(sky):
        for j, c in enumerate(row):
            if c:
                galaxies.add((i + bisect_left(empty_rows, i), j + bisect_left(empty_cols, j)))
    return sum(abs(x0-x1) + abs(y0-y1) for ((x0, y0), (x1, y1)) in itertools.combinations(galaxies, 2))