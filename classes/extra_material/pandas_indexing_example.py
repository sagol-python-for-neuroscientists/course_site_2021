"""
This demo uses a DF that was "pasted" from some online data, like this one:
https://rcompanion.org/rcompanion/d_07.html
"""


df = pd.read_clipboard()
df.head()

# MATLAB-style indexing

df.loc[df.loc[:, "Tech"] == "Janet", :]


# query
df.query('Tech == "Janet"').query('Rat > 2')
df.query("Tech == 'Janet' & Rat > 2")


# where
df.where(df.loc[:, "Tech"] == "Janet")
df.where(df.loc[:, "Tech"] == "Janet", "Brad")
