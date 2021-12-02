#%%
# PART 1 ---------------------------------------------------------------------
import pandas as pd

data = pd.read_csv("../data/day_2_data.txt", header=None)
data.columns = ["direction"]

data["spaces"] = data.direction.apply(lambda x: int(x.split(" ")[1]))
data["direction"] = data.direction.apply(lambda x: x.split(" ")[0])

forward = data[data.direction == "forward"].spaces.sum()
down = data[data.direction == "down"].spaces.sum()
up = data[data.direction == "up"].spaces.sum()

height = down - up

print(f"Position is {height * forward}.")
# %%
# PART 2 ---------------------------------------------------------------------
data = pd.read_csv("../data/day_2_data.txt", header=None)
data.columns = ["direction"]
data["spaces"] = data.direction.apply(lambda x: int(x.split(" ")[1]))
data["direction"] = data.direction.apply(lambda x: x.split(" ")[0])

aim = 0
depth = 0
forward = 0

for row in data.index:
    direction = data.loc[row, "direction"]
    val = data.loc[row, "spaces"]
    if direction == "down":
        # depth += val
        aim += val
    elif direction == "up":
        # depth -= val
        aim -= val
    elif direction == "forward":
        forward += val
        depth = depth + (aim * val)

print(f"Position is {depth * forward}.")

# %%
