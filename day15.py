

def hash(s: str) -> int:
    h: int = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h


def part1(lines):
    params: list[str] = next(lines).split(",")
    return sum(map(hash, params))


def part2(lines):
    params: list[str] = next(lines).split(",")
    boxes = [{} for _ in range(256)]
    for param in params:
        if "-" in param:
            label = param[:-1]
            boxes[hash(label)].pop(label, None)
        else:
            label, foc = param.split("=")
            boxes[hash(label)][label] = int(foc)
    power = 0
    for i, box in enumerate(boxes):
        for j, foc in enumerate(box.values()):
            power += (i + 1) * (j + 1) * foc
    return power