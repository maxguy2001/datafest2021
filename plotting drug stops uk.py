import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("data/drugstops_uk.csv")

plt.plot(df["Longitude"], df["Latitude"], "o")
plt.show()