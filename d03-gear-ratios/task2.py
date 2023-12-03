import sys


def parse_num(line, col):
	if not line[col].isdigit():
		return 0
	
	start = col
	value = 0
	
	while line[start - 1].isdigit():
		start -= 1

	while line[start].isdigit():
		value = value * 10 + int(line[start])
		start += 1

	return value


def line_nums(line, col):
	if line[col].isdigit():
		return [parse_num(line, col)]
	else:
		possible = [parse_num(line, col - 1), parse_num(line, col + 1)]
		return list(filter(lambda x: x != 0, possible))


def surrounding_nums(input, row, col):
	nums = []
	nums += line_nums(input[row - 1], col)
	nums += line_nums(input[row], col)
	nums += line_nums(input[row + 1], col)
	return nums


def main(input):
	input.insert(0, "." * len(input[0]))
	input.append("." * len(input[0]))

	sum = 0
	for row, line in enumerate(input[1:-1]):
		for col, c in enumerate(line.strip()):
			if c == '*':
				nums = surrounding_nums(input, row + 1, col)
				if len(nums) == 2:
					sum += nums[0] * nums[1]

	print(sum)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
