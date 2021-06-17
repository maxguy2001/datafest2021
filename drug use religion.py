import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/uk.csv")

relnums = []
drugnums = []
proportions = []
religions = ["None", "Christian", "Buddhist", "Hindu", "Jewish", "Muslim", "Sikh", "Other"]

for i in range(8):
    relnum_df = df[df["DEM_RELIGION"].isin([i])]
    relnum = len(relnum_df)
    relnums.append(relnum)
    drugnum_df = relnum_df[relnum_df["ILL_USE"].isin([1])]
    drugnum = len(drugnum_df)
    drugnums.append(drugnum)

#proportion = drugnums / relnums
for i in range(8):
    if relnums[i] == 0:
        frac = 0
    else:
        frac = drugnums[i] / relnums[i]
    proportions.append(frac)

ones = np.ones(8).tolist()


fig = plt.figure()
ax1 = plt.bar(religions, ones)
ax2 = plt.bar(religions, proportions)
plt.xticks(rotation = "45")
plt.show()



