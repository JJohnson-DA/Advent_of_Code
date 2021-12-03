#%%
# PART 1 ---------------------------------------------------------------------
def get_file(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
    return data


def get_position(data):
    depth = 0
    position = 0

    for d in data:
        direction = d.split()[0]
        val = int(d.split()[1])
        if direction == "forward":
            position += val
        elif direction == "up":
            depth -= val
        elif direction == "down":
            depth += val

    return depth, position


def main():
    directions = get_file("../data/day_2_data.txt")
    depth, position = get_position(directions)
    print(f"Position (depth*forward) is {depth*position}")


if __name__ == "__main__":
    main()

# %%
# PART 2 -----------------------------------------------------------------------
def get_file(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
    return data


def get_position(data):
    aim = 0
    depth = 0
    forward = 0

    for d in data:
        direction = d.split()[0]
        val = int(d.split()[1])
        if direction == "down":
            aim += val
        elif direction == "up":
            aim -= val
        elif direction == "forward":
            forward += val
            depth = depth + (aim * val)
    return depth, forward


def main():
    directions = read_data("../data/day_2_data.txt")
    depth, position = get_position(directions)
    print(f"Position (depth*forward) is {depth*position}")


if __name__ == "__main__":
    main()
