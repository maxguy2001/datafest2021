import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

df = pd.read_csv("data/uk.csv")

single = df[df["DEM_MARITAL"].isin([1])]
numsingle = len(single)
single_drug = single[single["ILL_MNTH"].isin([1])]
numsingle_drug = len(single_drug)

hetero = df[df["DEM_MARITAL"].isin([2, 3, 4])]
numhetero = len(hetero)
hetero_drug = hetero[hetero["ILL_MNTH"].isin([1])]
numhetero_drug = len(hetero_drug)

homosex = df[df["DEM_MARITAL"].isin([6, 7, 8, 9])]
numhomosex = len(homosex)
homosex_drug = homosex[homosex["ILL_MNTH"].isin([1])]
numhomosex_drug = len(homosex_drug)

sexualities = ["Single", "Heterosexual", "Homosexual"]
num_sexualities = [numsingle, numhetero, numhomosex]
num_sexualities_drug = [numsingle_drug, numhetero_drug, numhomosex_drug]

proportions = []
ones = np.ones(3).tolist()

for i in range(3):
    frac = num_sexualities_drug[i] / num_sexualities[i]
    proportions.append(frac)


#proportion plot
fig = plt.figure(figsize=(10, 4))
ax1 = plt.bar(sexualities, ones)
ax2 = plt.bar(sexualities, proportions)
plt.show()

"""
#regular plot
fig = plt.figure(figsize=(10, 4))
ax1 = plt.bar(sexualities, num_sexualities)
ax2 = plt.bar(sexualities, num_sexualities_drug)
plt.show()
"""

