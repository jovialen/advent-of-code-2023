from task1 import parse_input
import sys
from math import prod


def find_shared(frequencies):
    if len(frequencies) == 0: 
        return 0
    elif len(frequencies) == 1:
        return frequencies[0]
    
    f_left = frequencies[0]
    f_right = frequencies[1]

    n_left = 1
    n_right = 1

    while True:
        left = f_left * n_left + (n_left - 1)
        right = f_right * n_right + (n_right - 1)

        if left == right:
            return find_shared([left] + frequencies[2:])

        if left > right:
            n_right += 1
        else:
            n_left += 1


def main(input):
    steps, map = parse_input(input)
    frequencies = []
    nodes = list(filter(lambda k: k.endswith("A"), map.keys()))
    i = 0
    while len(nodes) > 0:
        left = steps[i % len(steps)] == "L"
        next_nodes = []
        for node in nodes:
            next_node = map[node][0 if left else 1]
            if next_node.endswith("Z"):
                frequencies.append(i)
            else:
                next_nodes.append(next_node)
        nodes = next_nodes
        i += 1

    i = find_shared(frequencies) + 1
    print(i)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
