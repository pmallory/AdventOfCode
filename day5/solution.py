def is_nice(string):
    #check for >= 3 vowels
    if len([c for c in string if c in "aeiou"]) < 3:
        return False

    #check for double letters
    for i, char in enumerate(string):
        if i == len(string)-1:
            return False
        if char == string[i+1]:
            break

    #check for bad pairs
    bad_pairs = ['ab','cd','pq','xy']
    for pair in bad_pairs:
        if pair in string:
            return False

    return True


if __name__ == "__main__":
    counter = 0
    with open("input") as f:
        for line in f:
            if is_nice(line):
                counter += 1
    print(counter)
