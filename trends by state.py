import pandas as pd

add = pd.read_csv("data/trends/adderall.csv")
fent = pd.read_csv("data/trends/fentanyl.csv")
oxy = pd.read_csv("data/trends/oxycodone.csv")
ket = pd.read_csv("data/trends/ketamine.csv")
pain = pd.read_csv("data/trends/pain relief.csv")
coke = pd.read_csv("data/trends/cocaine.csv")
drug = pd.read_csv("data/trends/drugs.csv")


#add["fentanyl"] = fent["Fentanyl: (3/27/20 - 3/27/21)"]

#print(add.head())

#df = pd.concat([add, fent], axis = 1).drop_duplicates()
df = add.merge(fent, left_on="Region", right_on="Region")
df = df.merge(oxy, left_on="Region", right_on="Region")
df = df.merge(ket, left_on="Region", right_on="Region")
df = df.merge(pain, left_on="Region", right_on="Region")
df = df.merge(coke, left_on="Region", right_on="Region")
df = df.merge(drug, left_on="Region", right_on="Region")

avgs = []
cols = ["Adderall", "Fentanyl", "Oxycodone", "ketamine", "Pain_relief", "Cocaine", "drugs"]

#print(df.iloc[5]["Adderall"])
for i in range(len(df)):
    sum = 0
    for j in cols:
        sum += df.iloc[i][j]
    avgs.append(sum/7)

df["average"] = avgs
#print(df.head())

#print(max(avgs), min(avgs))
avgs2 = [x - 56 for x in avgs]
avgs3 = [5.263*x for x in avgs2]

print(max(avgs3), min(avgs3))
df["scaled_avg"] = avgs3
#print(avgs3)

df.to_csv("data/trends/trends.csv")




