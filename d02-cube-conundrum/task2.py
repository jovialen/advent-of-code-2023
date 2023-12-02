import sys
from task1 import parse_game


def main(input):
	games = [parse_game(line) for line in input]
	S = 0
	for (_, r, g, b) in games:
		power = r * g * b
		S += power
	print(S)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: {sys.argv[0]} <input file>")
		sys.exit(0)

	with open(sys.argv[1], "r") as f:
		main(f.readlines())
