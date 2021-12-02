#%%
# To do this, count the number of times a depth measurement increases from the
# previous measurement.

# Imports and Data
import pandas as pd

data = pd.read_csv("../data/day_1_data.txt", header=0, names=["depth"])

# Shift values and determine if it increased
data["shifted"] = data.shift(1)
data["increase"] = data.depth > data.shifted

# Print number of depth increases
print(f"The depth increased {data.increase.sum()} times.")

# %%
# Considering every single measurement isn't as useful as you expected: there's
# just too much noise in the data. Instead, consider sums of a three-measurement
# sliding window.

# Imports and Data
import pandas as pd

data = pd.read_csv("../data/day_1_data.txt", header=0, names=["depth"])

# Calc rolling window and shift for comparison
data["rolling_3"] = data.depth.rolling(3, min_periods=3).sum()
data["shifted"] = data.rolling_3.shift(1)

# Determine if rolling depth increased and print the total increase
data["increase"] = data.rolling_3 > data.shifted
print(f"The depth increased {data.increase.sum()} times.")

# %%
