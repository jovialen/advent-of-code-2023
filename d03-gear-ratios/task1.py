import sys


def main(input):
    input.insert(0, "." * len(input[0]))
    input.append("." * len(input[0]))

    sum = 0
    for i, line in enumerate(input[1:-1]):
        over = input[i]
        under = input[i + 2]

        value = 0
        flush = False

        prev_symbol = False
        for j, c in enumerate(line.strip()):
            symbol = (not over[j].isdigit() and over[j] != '.') or\
                     (not under[j].isdigit() and under[j] != '.') or\
                     (c != '.' and not c.isdigit())

            if c.isdigit():
                value = value * 10 + int(c)
                flush = flush or symbol or prev_symbol
            elif flush or (value > 0 and symbol):
                sum += value
                value = 0
                flush = False
            else:
                value = 0

            prev_symbol = symbol

        if flush:
            sum += value

    print(sum)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
