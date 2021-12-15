# %% PART 1 --------------------------------------------------------------------
def get_input(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
        data = data[0].split(",")
        data = [int(x) for x in data]
    return data


def optimal_move(data):
    movements = {}
    for position in range(min(data), max(data) + 1):
        fuel_needed = 0
        for crab in data:
            fuel_needed += abs(crab - position)
        movements[fuel_needed] = position
    return movements


def main():
    data = get_input("../data/day_7_data.txt")
    movements = optimal_move(data)
    print(f"Best move is {movements[min(movements)]} and costs {min(movements)}.")


if __name__ == "__main__":
    main()

# %% PART 2 --------------------------------------------------------------------
def get_input(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
        data = data[0].split(",")
        data = [int(x) for x in data]
    return data


def optimal_move(data):
    movements = {}
    for position in range(min(data), max(data) + 1):
        fuel_needed = 0
        for crab in data:
            fuel_needed += (abs(crab - position) * (abs(crab - position) + 1)) / 2
        movements[fuel_needed] = position
    return movements


def main():
    data = get_input("../data/day_7_data.txt")
    movements = optimal_move(data)
    print(f"Best move is {movements[min(movements)]} and costs {min(movements)}.")


if __name__ == "__main__":
    main()

# %%
