#%% Part 1 ---------------------------------------------------------------------
def get_file(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
    return data


def get_gamma_epsilon(data):
    ind_list = []
    for i in range(len(data[0])):
        ind = []
        for d in data:
            ind.append(d[i])
        ind_list.append(ind)

    gamma = str()
    epsilon = str()
    for l in ind_list:
        gamma += max(set(l), key=l.count)
        epsilon += min(set(l), key=l.count)

    return gamma, epsilon


def binary_multiply(first, second):
    first_dec = int(first, 2)
    second_dec = int(second, 2)
    result = first_dec * second_dec
    return result


def main():
    data = get_file("../data/day_3_data.txt")
    gam, eps = get_gamma_epsilon(data)
    result = binary_multiply(gam, eps)
    print(f"Result is {result}")


if __name__ == "__main__":
    main()


# %% Part 2 --------------------------------------------------------------------
import collections


def get_file(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
    return data


def get_oxygen_co2_level(data, molecule):
    # list to edit and return at the end, will be overwritten multiple times
    master_list = data

    # Loop over each position in the binary sequences
    for i in range(len(master_list[0])):
        keep_list = []
        ind_list = []
        # Loop and append lists of the digits in each position
        for d in master_list:
            ind = []
            ind.append(d[i])
            ind_list.extend(ind)
        # Determine counts of each digit in each item in ind_list
        freq = collections.Counter(ind_list)
        # Determine max value key based on molecule
        if molecule == "oxygen":
            if freq["0"] > freq["1"]:
                digit = "0"
            elif freq["1"] > freq["0"]:
                digit = "1"
            else:
                digit = "1"
        if molecule == "co2":
            if freq["0"] > freq["1"]:
                digit = "1"
            elif freq["1"] > freq["0"]:
                digit = "0"
            else:
                digit = "0"
        # if digit in position is correct, append to keep_list
        for d in master_list:
            if d[i] == digit:
                keep_list.append(d)
        master_list = keep_list
        if len(master_list) == 1:
            break
    return master_list[0]


def binary_multiply(first, second):
    first_dec = int(first, 2)
    second_dec = int(second, 2)
    result = first_dec * second_dec
    return result


def main():
    data = get_file("../data/day_3_data.txt")
    oxygen = get_oxygen_co2_level(data, "oxygen")
    co2 = get_oxygen_co2_level(data, "co2")
    result = binary_multiply(oxygen, co2)
    print(f"Result is {result}")


if __name__ == "__main__":
    main()

# %%
