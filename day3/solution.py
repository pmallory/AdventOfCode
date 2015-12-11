from collections import defaultdict

def move(coords, direction):
    if direction == "^":
        return (coords[0], coords[1]-1)
    if direction == ">":
        return (coords[0]+1, coords[1])
    if direction == "v":
        return (coords[0], coords[1]+1)
    if direction == "<":
        return (coords[0]-1, coords[1])

def process_input(infile):
    coords = (0,0)

    houses = defaultdict(int)
    houses[(0,0)] = 1

    with open(infile) as f:
        s = f.read()

    for c in s:
        coords = move(coords, c)
        houses[coords] += 1

    print("part 1: {}".format(len(houses)))

    santa_coords = (0,0)
    robosanta_coords = (0,0)

    houses = defaultdict(int)
    houses[(0,0)] = 2

    for santa, robosanta in zip(s[0::2], s[1::2]):
        santa_coords = move(santa_coords, santa)
        robosanta_coords = move(robosanta_coords, robosanta)
        houses[santa_coords] += 1
        houses[robosanta_coords] += 1

    print("part 2: {}".format(len(houses)))

if __name__ == "__main__":
    process_input("input")
