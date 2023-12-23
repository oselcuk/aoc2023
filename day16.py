from copy import deepcopy
from itertools import chain
from typing import Iterable

LEFT = 1
DOWN = 2
RIGHT = 4
UP = 8


def move_beam(x: int, y: int, dir: int) -> tuple[int, int]:
    if dir == LEFT:
        return x, y - 1
    if dir == RIGHT:
        return x, y + 1
    if dir == UP:
        return x - 1, y
    if dir == DOWN:
        return x + 1, y
    return x, y


REFLECTIONS = {
    "/": {
        LEFT: DOWN,
        DOWN: LEFT,
        RIGHT: UP,
        UP: RIGHT,
    },
    "\\": {
        LEFT: UP,
        UP: LEFT,
        RIGHT: DOWN,
        DOWN: RIGHT,
    }
}


def propagate(
    light: list[list[int]],
    grid: list[str],
    dir: int,
    x: int,
    y: int,
) -> list[tuple[int, int, int]]:
    x, y = move_beam(x, y, dir)
    if x < 0 or x >= len(light) or y < 0 or y >= len(light[x]):
        return []
    if light[x][y] & dir:
        return []
    light[x][y] |= dir
    match grid[x][y]:
        case c if c in REFLECTIONS:
            return [(REFLECTIONS[c][dir], x, y)]
        case "|" if dir in [LEFT, RIGHT]:
            return [(UP, x, y), (DOWN, x, y)]
        case "-" if dir in [UP, DOWN]:
            return [(LEFT, x, y), (RIGHT, x, y)]
        case _:
            return [(dir, x, y)]


def part1(lines):
    grid: list[str] = [line.strip() for line in lines]
    light: list[list[int]] = [[0] * len(row) for row in grid]
    stack = [(RIGHT, 0, -1)]
    while stack:
        stack += propagate(light, grid, *stack.pop())
    # for row in light:
    #     print("".join(map(str, row)))
    return sum(map(bool, chain(*light)))