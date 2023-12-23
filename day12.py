


def possibilities(line: str) -> int:
    tiles, numbers = line.split()
    numbers = list(map(int, numbers.split()))
    


def part1(lines):
    return sum(map(possibilities, lines))
