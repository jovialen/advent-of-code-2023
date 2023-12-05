import sys


def parse_seeds(line):
    _, seeds = line.split(":")
    return [int(seed) for seed in seeds.strip().split()]


def parse_map(input):
    name, _ = input[0].strip().split()
    input = input[1:]
    data = []
    while len(input) > 0:
        split = input[0].strip().split()
        input = input[1:]
        if len(split) != 3:
            break
        data.append({ "start_dst": int(split[0]), "start_src": int(split[1]), "len": int(split[2]) })
    return (input, name, data)


def parse_input(input):
    seeds = parse_seeds(input[0])
    input = input[2:]

    maps = {}    
    while len(input) > 0:
        input, name, data = parse_map(input)
        maps[name] = data
    
    return (seeds, maps)


def poll_map(value, map):
    for mapping in map:
        offset = value - mapping["start_src"]
        if offset <= mapping["len"] and offset >= 0:
            return mapping["start_dst"] + offset
    return value


def process_seed(seed, maps):
    value = seed
    for name, map in maps.items():
        value = poll_map(value, map)
    return value


def main(input):
    seeds, maps = parse_input(input)
    smallest = 100_000_000_000
    for seed in seeds:
        value = process_seed(seed, maps)
        smallest = min(smallest, value)
    print(smallest)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)
    
    with open(sys.argv[1], "r") as f:
        main(f.readlines())