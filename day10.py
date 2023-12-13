from dataclasses import dataclass
from typing import Iterable
from itertools import chain

shape_to_delta: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {
    "-": ((0, -1), (0, +1)),
    "|": ((-1, 0), (+1, 0)),
    "J": ((-1, 0), (0, -1)),
    "L": ((-1, 0), (0, +1)),
    "7": ((0, -1), (+1, 0)),
    "F": ((0, +1), (+1, 0)),
}

@dataclass
class Point:
    x: int
    y: int

    def valid(self, tiles: list[str]) -> bool:
        return 0 <= self.x < len(tiles) or 0 <= self.y < len(tiles[self.x])
    
    def delta(self, dx, dy) -> "Point":
        return Point(self.x + dx, self.y + dy)

    def get_legs(self, tiles: list[str]) -> list["Point"]:
        if (deltas := shape_to_delta.get(tiles[self.x][self.y])) is None:
            return [Point(-1, -1)]
        return [self.delta(*delta) for delta in deltas]


def loop(tiles: list[str], prev: Point, pos: Point) -> list[list[bool]] | None:
    start_deltas = [(pos.x - prev.x, pos.y - prev.y)]
    owned = [[False] * len(row) for row in tiles]
    owned[pos.x][pos.y] = True
    def get_next(prev: Point, pos: Point) -> Point | None:
        if not pos.valid(tiles):
            return None
        legs = pos.get_legs(tiles)
        if prev not in legs:
            return None
        legs.remove(prev)
        return legs[0]
    while (nxt := get_next(prev, pos)):
        owned[nxt.x][nxt.y] = True
        if tiles[nxt.x][nxt.y] == "S":
            start_deltas.append((pos.x - nxt.x, pos.y - nxt.y))
            start = next(key for key, value in shape_to_delta.items() if set(value) == set(start_deltas))
            tiles[nxt.x] = tiles[nxt.x].replace("S", start)
            return owned
        prev, pos = pos, nxt
    return None

def get_maps(lines: Iterable[str]) -> tuple[list[list[bool]], list[str]]:
    tiles: list[str] = [line.strip() for line in lines]
    x: int = 0
    y: int = 0
    for x, row in enumerate(tiles):
        if (y := row.find("S")) != -1:
            break
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in deltas:
        if owned := loop(tiles, Point(x, y), Point(x + dx, y + dy)):
            return owned, tiles
    assert False


def part1(lines):
    return list(chain(*get_maps(lines)[0])).count(True) / 2


def part2(lines):
    downward_tiles = "|F7"
    owned, tiles = get_maps(lines)
    owned_count = 0
    for owned_row, tile_row in zip(owned, tiles):
        inside = False
        for owned, tile in zip(owned_row, tile_row):
            if tile in downward_tiles and owned:
                inside = not inside
            if inside and not owned:
                owned_count += 1
    return owned_count