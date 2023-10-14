import pandas as pd

df = pd.DataFrame()
df["c"] = [10, 20, 30]
df["a"] = ['one', 12, 13]
df["a"] = [1, 12, 13]
df["b"] = ['one', 1, 'three']
df.index = ["лох", "b", "c"]
print(df)

df

