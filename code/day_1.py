#%%
# PART 1 ---------------------------------------------------------------------
import pandas as pd

data = pd.read_csv("../data/day_1_data.txt", header=0, names=["depth"])

# Shift values and determine if it increased
data["shifted"] = data.shift(1)
data["increase"] = data.depth > data.shifted

# Print number of depth increases
print(f"The depth increased {data.increase.sum()} times.")

# PART 2 ---------------------------------------------------------------------
import pandas as pd

data = pd.read_csv("../data/day_1_data.txt", header=0, names=["depth"])

# Calc rolling window and shift for comparison
data["rolling_3"] = data.depth.rolling(3, min_periods=3).sum()
data["shifted"] = data.rolling_3.shift(1)

# Determine if rolling depth increased and print the total increase
data["increase"] = data.rolling_3 > data.shifted
print(f"The depth increased {data.increase.sum()} times.")
