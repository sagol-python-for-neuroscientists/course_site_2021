import pandas as pd
import numpy as np


# data is taken
data = pd.read_clipboard()

data.head()

# Assume I want to see the mean protein values per technician

# Perhaps we need to find all Tech names, and then iterate over them
all_techs = data["Tech"].unique()
means = []

for tech in all_techs:
    current_data = data.query("Tech == @tech")
    means.append((tech, current_data["Protein"].mean()))

print(means)

# In MATLAB we might've not stored both techs in the same table - we could use
# a struct for example. But it's definitely easier to have them in the same
# table together.

# Let's solve it with groupby
means = data.groupby("Tech").mean()
print(means)
# 🤯
# We can also plot it quite easily
means = data.groupby("Tech").boxplot()

# We can also iterate through the groups if we wish to do so
for name, grp in data.groupby("Tech"):
    print(name)
    print(grp)

# More complicated data can be grouped as well
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]


index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])

df = pd.DataFrame({"A": [1, 1, 1, 1, 2, 2, 3, 3], "B": np.arange(8)}, index=index)

df.head()

# We can also do groupby by index names
grouped = df.groupby(["second", "A"]).sum()
print(grouped)

# Let's look at a bit more advanced group-by operations - transformations
index = pd.date_range("10/1/1999", periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = ts.rolling(window=100, min_periods=100).mean().dropna()
print(ts.head())
print(ts.tail())

# For each year standardize the measurements to have the same mean and STD
transformed = ts.groupby(lambda x: x.year).transform(lambda x: (x - x.mean()) / x.std())

# And there are many more examples here - https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#transformation
