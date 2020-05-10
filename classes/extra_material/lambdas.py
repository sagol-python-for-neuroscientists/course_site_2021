import pandas as pd

# Lambda functions are anonymous functions (MATLAB's @)
def ret(x):
    return x
# ==
ret = lambda x: x

# We can define it and then use it
(lambda x: x + 1)(2)  # prints 3

# They're useful when we want to do some quick operation with a function
df = pd.DataFrame({'a': [1, 2, 3]})
df['a'].apply(lambda x: print(x))
