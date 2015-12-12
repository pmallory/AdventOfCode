import re
from collections import defaultdict

def get_instr(line):
    if 'turn on' in line:
        return 'turn on'
    elif 'toggle' in line:
        return 'toggle'
    elif 'turn off' in line:
        return 'turn off'

def get_region(line):
    m = re.search(r"(\d+),(\d+) through (\d+),(\d+)", line)

    left_edge = int(m.group(1))
    top_edge = int(m.group(2))
    right_edge = int(m.group(3))
    bottom_edge = int(m.group(4))

    for i in range(left_edge, right_edge+1):
        for j in range(top_edge, bottom_edge+1):
            yield i, j

def turn_off(lights, region):
    for light in region:
        if lights[light] > 0:
            lights[light] -= 1


def toggle(lights, region):
    for light in region:
        lights[light] +=2

def turn_on(lights, region):
    for light in region:
        lights[light] += 1 

do = {'turn on': turn_on,
      'toggle': toggle,
      'turn off': turn_off}

def process(f):
    lights = defaultdict(int)

    for line in f:
        instruction = get_instr(line)
        region = get_region(line)

        do[instruction](lights, region)

    f.close()

    return sum(lights.values())

if __name__ == "__main__":
    with open("input") as f:
        print(process(f))
