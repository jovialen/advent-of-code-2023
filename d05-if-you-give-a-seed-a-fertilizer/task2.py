from task1 import parse_input
import sys


def poll_map(value, map):
    for mapping in map:
        offset = value - mapping["start_dst"]
        if offset <= mapping["len"] and offset >= 0:
            return mapping["start_src"] + offset
    return value


def process_location(location, maps):
    value = location
    for name, map in reversed(maps.items()):
        value = poll_map(value, map)
    return value


def main(input):
    seeds, maps = parse_input(input)
    found = False
    location = 0
    while not found:
        location += 1
        seed = process_location(location, maps)
        for start_seed, length in zip(seeds[::2], seeds[1::2]):
            if seed >= start_seed and seed <= start_seed + length:
                found = True
    print(location)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)
    
    with open(sys.argv[1], "r") as f:
        main(f.readlines())