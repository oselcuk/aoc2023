from operator import itemgetter

def part1(lines):
    def process(line: str) -> int:
        nums = list(filter(str.isdigit, line))
        return int(nums[0] + nums[-1])
    return sum(process(line) for line in lines)

def part2(lines):
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    numbers_mapping: dict = {name: str(number + 1) for number, name in enumerate(numbers)}
    numbers_mapping.update({str(i): str(i) for i in range(1, 10)})
    
    def process(line: str) -> int:
        indices = [(number, line.find(name), line.rfind(name)) for name, number in numbers_mapping.items() if name in line]
        return int(min(indices, key=itemgetter(1))[0] + max(indices, key=itemgetter(2))[0])
    return sum(process(line) for line in lines)