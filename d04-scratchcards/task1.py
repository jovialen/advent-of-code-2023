import sys


def parse_input(input):
    out = []
    for line in input:
        id, nums = line.split(":")
        winning, actual = nums.split("|")
        winning = [int(num) for num in winning.split()]
        actual  = [int(num) for num in  actual.split()]
        out.append({ "winning": winning, "actual": actual })
    return out


def main(input):
    cards = parse_input(input)
    sum = 0
    for card in cards:
        overlap = len(list(filter(lambda v: v in card["winning"], card["actual"])))
        if overlap > 0:
            sum += 2 ** (overlap - 1)
    print(sum)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)
    
    with open(sys.argv[1], "r") as f:
        main(f.readlines())