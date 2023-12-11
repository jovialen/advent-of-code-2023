import sys


def parse_input(input):
    return [[int(x) for x in line.strip().split()] for line in input]


def derive(history):
    derived = []
    for a, b in zip(history, history[1:]):
        derived.append(b - a)
    return derived if len(derived) > 0 else [0]


def extrapolate(derived_history):
    if type(derived_history[-1]) is int:
        return derived_history[-1]
    else:
        return extrapolate(derived_history[-1]) + derived_history[-2]


def main(input):
    histories = parse_input(input)
    S = 0
    for history in histories:
        root = history
        while any(map(lambda v: v != 0, history)):
            history.append(derive(history))
            history = history[-1]
        S += extrapolate(root)
    print(S)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
