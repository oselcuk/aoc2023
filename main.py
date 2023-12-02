import sys
import importlib

day, part = sys.argv[1:3]
day = f"day{int(day):02d}"
suffix = ""
if len(sys.argv) > 3 and sys.argv[3].startswith("s"):
    suffix = "_sample"

with open(f"{day}{suffix}.txt") as input:
    module = importlib.import_module(day)
    result = getattr(module, f"part{part}")(input)
    print(result)