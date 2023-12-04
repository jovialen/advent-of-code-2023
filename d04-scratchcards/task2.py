import sys
from functools import reduce


def parse_input(input):
    out = []
    for line in input:
        id, nums = line.split(":")
        winning, actual = nums.split("|")
        winning = [int(num) for num in winning.split()]
        actual  = [int(num) for num in  actual.split()]
        out.append({ "winning": winning, "actual": actual, "count": 1 })
    return out


def main(input):
    cards = parse_input(input)
    for i, card in enumerate(cards):
        overlap = len(list(filter(lambda v: v in card["winning"], card["actual"])))
        for copy in cards[i + 1:i + 1 + overlap]:
            copy["count"] += 1 * card["count"]
    num_of_cards = reduce(lambda acc, card: acc + card["count"], cards, 0)
    print(num_of_cards)
    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)
    
    with open(sys.argv[1], "r") as f:
        main(f.readlines())