import sys
from functools import reduce


def parse_sample(sample):
    red = 0
    green = 0
    blue = 0
    for cubes in sample.split(","):
        count, color = cubes.strip().split(" ")
        if color == "red":
            red = max(red, int(count))
        elif color == "green":
            green = max(green, int(count))
        else:
            blue = max(blue, int(count))
    return (red, green, blue)


def parse_game(game):
    game, samples = game.split(":")
    id = int(game[5:])
    red = 0
    green = 0
    blue = 0
    for sample in samples.split(";"):
        r, g, b = parse_sample(sample)
        red = max(red, r)
        green = max(green, g)
        blue = max(blue, b)
    return (id, red, green, blue)


def playable_with_cubes(game, red, green, blue):
    id, r, g, b = game
    return red >= r and green >= g and blue >= b


def main(input):
    def game_value(acc, game):
        return acc + (game[0] if playable_with_cubes(game, 12, 13, 14) else 0)

    games = [parse_game(line) for line in input]
    sum = reduce(game_value, games, 0)
    print(sum)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
