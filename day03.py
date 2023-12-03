from typing import Optional, Tuple
from itertools import product


def parse_number1(schematic: list[str], x: int, y: int) -> Tuple[Optional[int], int]:
    n, m = len(schematic), len(schematic[0])
    deltas = list(product([-1,0,1], repeat=2))
    adjacent = False
    number = "0"
    def is_symbol(c):
        return not c.isdigit() and c != "."
    for i in range(y, m):
        if not schematic[x][i].isdigit():
            return int(number) if adjacent else None, i + 1
        number += schematic[x][i]
        for dx, dy in deltas:
            if 0 <= x + dx < n and 0 <= i + dy < m:
                adjacent = adjacent or is_symbol(schematic[x+dx][i+dy])
    return int(number) if adjacent else None, m


def part1(lines):
    schematic = list(map(str.strip, lines))
    result = 0
    for i in range(len(schematic)):
        j = 0
        while j < len(schematic[i]):
            parsed, j = parse_number1(schematic, i, j)
            if parsed:
                result += parsed
    return result
