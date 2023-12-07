import sys


def parse_input(input):
	_, time = input[0].split(":")
	_, distance = input[1].split(":")
	time = int(time.replace(" ", ""))
	distance = int(distance.replace(" ", ""))
	return time, distance


def search(time, distance, low, high):
	while high > low:
		mid = (high + low) // 2

		if mid * (time - mid) > distance:
			return search(time, distance, mid + 1, high)
		else:
			return search(time, distance, low, mid - 1)
	return low


def main(input):
	time, distance = parse_input(input)
	first = 0
	while first * (time - first) < distance:
		first += 1

	last = search(time, distance, first, time - 1)

	count = last - first
	print(count)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
