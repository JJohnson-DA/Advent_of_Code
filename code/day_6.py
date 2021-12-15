# %% PART 1 --------------------------------------------------------------------
def get_input(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
        data = data[0].split(",")
        data = [int(x) for x in data]
    return data


def starting_count(data):
    school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in data:
        school[fish] += 1
    return school


def population_simulation(school, days):
    for day in range(0, int(days)):
        school = {
            0: school[1],
            1: school[2],
            2: school[3],
            3: school[4],
            4: school[5],
            5: school[6],
            6: school[7] + school[0],
            7: school[8],
            8: school[0],
        }
    # return sum(school[0] + school[1] + school[2] + school[3] + school[4])
    total_fish = 0
    for key, value in school.items():
        total_fish += value
    return total_fish


def main():
    data = get_input("../data/day_6_data.txt")
    school = starting_count(data)
    total_fish = population_simulation(school, 256)
    print(f"Total Fish: {total_fish}.")


if __name__ == "__main__":
    main()
# %%
