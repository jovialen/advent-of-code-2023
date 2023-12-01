import sys


def parse_line(line):
	for k, v in map.items():
		line = line.replace(k, v)
	return line


def calibration_value(line):
	map = {
		"zero": 0,
		"one": 1,
		"two": 2,
		"three": 3,
		"four": 4,
		"five": 5,
		"six": 6,
		"seven": 7,
		"eight": 8,
		"nine": 9
	}

	digits = []
	for i in range(len(line)):
		for k, v in map.items():
			if line.startswith(k, i):
				digits.append(v)
				break
		else:
			if line[i].isdigit():
				digits.append(int(line[i]))

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
