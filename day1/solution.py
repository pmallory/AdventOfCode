with open("input") as f:
    floor = 0
    s = f.read()
    for step, c in enumerate(s):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

        if floor == -1:
            print("step: {}".format(step+1))

    print(floor)
