import pandas as pd, numpy as np
test = pd.read_csv("data/test.csv")
ideal = pd.read_csv("data/ideal.csv")
no_x = sum(not np.isclose(ideal["x"], row["x"]).any() for _, row in test.iterrows())
print("test points:", len(test))
print("no matching x in ideal:", no_x)
print("x matched but tolerance failed:", len(test) - no_x - 34)