import sys


def calibration_value(line):
    digits = list(filter(lambda c: c.isdigit(), line))
    return int(digits[0]) * 10 + int(digits[-1])


def main(input):
    values = map(calibration_value, input)
    S = sum(values)
    print(S)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./task1 <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        input = f.readlines()
        main(input)
