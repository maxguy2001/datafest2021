import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/uk.csv")

cols_drug_use = [
    'CAN_USE',
    'COKE_USE',
    'CRACK_USE',
    'MDMA_USE',
    'GHB_USE',
    'SPEED_USE',
    'NPFENT_USE',
    'HEROIN_USE',
    'KET_USE',
    'MEPH_USE',
    'METHAM_USE',
    'LSD_USE',
    'MUSH_USE',
    'POP_USE',
    'STER_USE',
    'KHAT_USE',
    'SPICE_USE',
    'SAL_USE'
]

drug_names = [
    'Cannabis',
    'Cocaine Powder',
    'Crack Cocaine',
    'Ecstasy',
    'GHB/GBL',
    'N-P amphetamine',
    'N-P Fentanyl',
    'Heroin',
    'Ketamine',
    'Mephedrone',
    'Methamphetamine',
    'LSD',
    'Magic Mushrooms',
    'Poppers',
    'Anabolic Steroids',
    'Khat',
    'SCRAs',
    'Salvia'
]

print(len(drug_names) == len(cols_drug_use))

df = df[cols_drug_use]
df.columns = drug_names

df_last_week = df.loc[df.values == 2]
df_last_month = df.loc[df.values == 3]
df_last_year = df.loc[df.values == 4]
df_alltime = df.loc[df.values == 5]

for col in df_last_week.columns:
    df_last_week[col] = np.where(df_last_week[col] == 2, 1, 0)
for col in df_last_month.columns:
    df_last_month[col] = np.where(df_last_month[col] == 2, 1, 0)
for col in df_last_year.columns:
    df_last_year[col] = np.where(df_last_year[col] == 2, 1, 0)
for col in df_alltime.columns:
    df_alltime[col] = np.where(df_alltime[col] == 1, 0, 1)

week_corr = df_last_week.corr()
month_corr = df_last_month.corr()
year_corr = df_last_year.corr()

fig, ax = plt.subplots(2, 2, figsize=(30, 30))

mask = np.zeros_like(week_corr)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(week_corr, annot=True, mask=mask, linewidths=.5, cmap="YlGnBu", square=True, ax=ax[0][0])
ax[0][0].set_title('Relationships with recreational \ndrug usage within a week of survey', fontsize=35)

mask = np.zeros_like(month_corr)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(month_corr, annot=True, mask=mask, linewidths=.5, cmap="YlGnBu", square=True, ax=ax[0][1])
ax[0][1].set_title('Relationships with recreational \ndrug usage within a month of survey', fontsize=35)

mask = np.zeros_like(year_corr)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(year_corr, annot=True, mask=mask, linewidths=.5, cmap="YlGnBu", square=True, ax=ax[1][0])
ax[1][0].set_title('Relationships with recreational \ndrug usage within a year of survey', fontsize=35)

corr = df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corr, annot=True, mask=mask, linewidths=.5, cmap="YlGnBu", square=True, ax=ax[1][1])
ax[1][1].set_title('Relationships with recreational \ndrug usage ever', fontsize=35)

plt.savefig('four_heatmaps.png')
