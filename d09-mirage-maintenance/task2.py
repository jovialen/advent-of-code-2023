from task1 import parse_input, derive
import sys


def extrapolate(derived_history):
    if type(derived_history[0]) is int:
        return derived_history[0]
    else:
        return derived_history[1] - extrapolate(derived_history[0])


def main(input):
    histories = parse_input(input)
    S = 0
    for history in histories:
        root = history
        while any(map(lambda v: v != 0, history)):
            history.insert(0, derive(history))
            history = history[0]
        S += extrapolate(root)
    print(S)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
