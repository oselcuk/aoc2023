from collections import Counter
from functools import reduce
from operator import mul
from typing import Tuple


def parse_line(line: str) -> Tuple[int, Counter]:
    game_id, plays = line.strip().split(": ")
    game_id = int(game_id.removeprefix("Game "))
    plays = plays.split("; ")
    results = []
    for play in plays:
        cubes = (cube.split() for cube in play.split(", "))
        result = Counter({cube[1]: int(cube[0]) for cube in cubes})
        results.append(result)
    return game_id, reduce(Counter.__or__, results, Counter())


def part1(lines):
    limits = Counter(red=12, green=13, blue=14)
    return sum(game_id for game_id, counts in map(parse_line, lines) if counts <= limits)


def part2(lines):
    keys = ["red", "green", "blue"]
    return sum(reduce(mul, (cubes[key] for key in keys), 1) for _, cubes in map(parse_line, lines))