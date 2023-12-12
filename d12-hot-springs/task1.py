import sys


def count_arrangements(pattern, counts):
    if "?" in pattern:
        a = count_arrangements(pattern.replace("?", "#", 1), counts)
        b = count_arrangements(pattern.replace("?", ".", 1), counts)
        return a + b
    else:
        segments = pattern.split(".")
        segments = filter(lambda x: x != "", segments)
        segments = map(lambda x: len(x), segments)
        segments = list(segments)
        return segments == counts


def main(input):
    S = 0
    for line in input:
        pattern, counts = line.strip().split()
        counts = [int(x) for x in counts.split(",")]
        S += count_arrangements(pattern, counts)
    print(S)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
