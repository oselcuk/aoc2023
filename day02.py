from collections import Counter
from functools import reduce
from typing import Tuple


def part1(lines):
    def parse(line: str) -> Tuple[int, Counter]:
        game_id, plays = line.strip().split(": ")
        game_id = int(game_id.removeprefix("Game "))
        plays = plays.split("; ")
        results = []
        for play in plays:
            cubes = (cube.split() for cube in play.split(", "))
            result = Counter({cube[1]: int(cube[0]) for cube in cubes})
            results.append(result)
        return game_id, reduce(Counter.__or__, results, Counter())
    limits = Counter(red=12, green=13, blue=14)
    return sum(game_id for game_id, counts in map(parse, lines) if counts <= limits)