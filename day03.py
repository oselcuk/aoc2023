from collections import defaultdict
from typing import List, Optional, Set, Tuple
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


def parse_number2(schematic: list[str], x: int, y: int) -> Tuple[int, int, Set[Tuple[int, int]]]:
    """Returns (parsed number, next y coord, list of adjacent gear coords.)"""
    n, m = len(schematic), len(schematic[0])
    deltas = list(product([-1,0,1], repeat=2))
    number = "0"
    adj_gears = set()
    for i in range(y, m):
        if not schematic[x][i].isdigit():
            return int(number), i + 1, adj_gears
        number += schematic[x][i]
        for dx, dy in deltas:
            xp, yp = x + dx, i + dy
            if 0 <= xp < n and 0 <= yp < m and schematic[xp][yp] == "*":
                adj_gears.add((xp, yp))
    return int(number), m, adj_gears

def part2(lines):
    schematic = list(map(str.strip, lines))
    gears_to_nums = defaultdict(list)
    for i in range(len(schematic)):
        j = 0
        while j < len(schematic[i]):
            number, j, gears = parse_number2(schematic, i, j)
            # print(f"{number}: {gears}")
            for gear in gears:
                gears_to_nums[gear].append(number)
    # print(gears_to_nums)
    result = 0
    for nums in gears_to_nums.values():
        if len(nums) == 2:
            result += nums[0] * nums[1]
    return result
