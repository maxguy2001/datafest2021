import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/uk.csv")

cols_drug_use = [
    'FENT_USE',
    'BUP_USE',
    'METH_USE',
    'MORPH_USE',
    'OXY_USE',
    'TRAM_USE',
    'TAP_USE',
    'COD_USE',
    'DIHY_USE',
    'HYDM_USE',
    'SUF_USE',
    'STIM_USE',
    'BENZ_USE',
    'THC_USE',
    'DEX_USE',
    'DIPH_USE',
    'LOP_USE'
]

drug_names = [
    'Fentanyl',
    'Buprenorphine',
    'Methadone',
    'Morphine',
    'Oxycodone',
    'Tramadol',
    'Tapentadol',
    'Codeine',
    'Dihydrocodeine',
    'Hydromorphone',
    'Sufentanil',
    'Stimulands',
    'Benzodiazepines',
    'Cannabinoids',
    'Dextromethorphan',
    'Diphenhydramine',
    'Loperamide'
]

df_drug_use = df[cols_drug_use]
df_drug_use.columns = drug_names


def plot(df_drug_use):
    fig, ax = plt.subplots(1, 1, figsize=(15, 15))
    corr = df_drug_use.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    ax = sns.heatmap(corr, annot=True, mask=mask, linewidths=.5, cmap="YlGnBu", square=True)
    ax.set_title('Relationship between prescription \n& over-the-counter drug usage', fontsize=35)
    plt.savefig('drug_use_corr_heatmap.png')
