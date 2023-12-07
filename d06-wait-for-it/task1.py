import sys


def parse_input(input):
    _, times = input[0].split(":")
    _, distances = input[1].split(":")
    times = [int(time) for time in times.strip().split()]
    distances = [int(distance) for distance in distances.strip().split()]
    return (times, distances)


def main(input):
    times, distances = parse_input(input)
    S = 1
    for time, distance in zip(times, distances):
        count = 0
        for i in range(time):
            i_distance = i * (time - i)
            if i_distance > distance:
                count += 1
        if count != 0:
            S *= count
    print(S)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(0)

    with open(sys.argv[1], "r") as f:
        main(f.readlines())
