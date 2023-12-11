import sys


def parse_input(input):
    result = {}
    steps = input[0].strip()
    nodes = input[2:]
    for node in nodes:
        name, dirs = node.split(" = ")
        left, right = dirs.split()
        result[name] = (left[1:4], right[:3])
    return steps, result


def main(input):
    steps, map = parse_input(input)
    node = "AAA"
    i = 0
    while node != "ZZZ":
        left = steps[i % len(steps)] == "L"
        if left:
            node = map[node][0]
        else:
            node = map[node][1]
        i += 1
    print(i)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
