from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def valid(self, tiles: list[str]) -> bool:
        return 0 <= self.x < len(tiles) or 0 <= self.y < len(tiles[self.x])


    def get_legs(self, tiles: list[str]) -> list["Point"]:
        x, y = self.x, self.y
        match tiles[x][y]:
            case "-": return [Point(x, y - 1), Point(x, y + 1)]
            case "|": return [Point(x - 1, y), Point(x + 1, y)]
            case "J": return [Point(x - 1, y), Point(x, y - 1)]
            case "L": return [Point(x - 1, y), Point(x, y + 1)]
            case "7": return [Point(x + 1, y), Point(x, y - 1)]
            case "F": return [Point(x + 1, y), Point(x, y + 1)]
        return [Point(-1, -1)]


def loop(tiles: list[str], prev: Point, pos: Point) -> int | None:
    def get_next(prev: Point, pos: Point) -> Point | None:
        if not pos.valid(tiles):
            return None
        legs = pos.get_legs(tiles)
        if prev not in legs:
            return None
        legs.remove(prev)
        return legs[0]
    length = 0
    while (nxt := get_next(prev, pos)):
        length += 1
        if tiles[nxt.x][nxt.y] == "S":
            return length + 1
        prev, pos = pos, nxt



def part1(lines):
    tiles: list[str] = [line.strip() for line in lines]
    x: int = 0
    y: int = 0
    for x, row in enumerate(tiles):
        if (y := row.find("S")) != -1:
            break
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in deltas:
        if length := loop(tiles, Point(x, y), Point(x + dx, y + dy)):
            return length / 2