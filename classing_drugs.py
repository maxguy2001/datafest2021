# Importing relevant python packages

import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import matplotlib as mpl
import warnings 

path_uk =
uk_data = pd.read_csv(path_uk)
fent_users  = uk_data.loc[(uk_data['FENT_NMU'] == 1)]
meth_users  = uk_data.loc[(uk_data['METH_NMU'] == 1)]
morph_users = uk_data.loc[(uk_data['MORPH_NMU'] == 1)]
oxy_users   = uk_data.loc[(uk_data['OXY_NMU'] == 1)]
tap_users   = uk_data.loc[(uk_data['TAP_NMU'] == 1)]
hydm_users  = uk_data.loc[(uk_data['HYDM_NMU'] == 1)]
suf_users   = uk_data.loc[(uk_data['SUF_NMU'] == 1)]

prescription_A = pd.concat([fent_users, meth_users, morph_users, oxy_users, tap_users, hydm_users, suf_users])
prescription_A = pd.DataFrame(classA_prescription_drugs)

for column in uk_data.columns:
    print (column)
cod_users = uk_data.loc[(uk_data['COD_NMU'] == 1)]
dihy_users = uk_data.loc[(uk_data['DIHY_NMU'] == 1)]
stim_users = uk_data.loc[(uk_data['BEN_NMU'] == 1)]
thc_users = uk_data.loc[(uk_data['THC_NMU'] == 1)]
prescription_B = pd.concat([fent_users, meth_users, morph_users, oxy_users, tap_users, hydm_users, suf_users])
prescription_B = pd.DataFrame(prescription_B)

bup_users = uk_data.loc[(uk_data['BUP_NMU'] == 1)]
tram_users = uk_data.loc[(uk_data['DIHY_NMU'] == 1)]
benz_users = uk_data.loc[(uk_data['STIM_NMU'] == 1)]
prescription_C = pd.concat([fent_users, meth_users, morph_users, oxy_users, tap_users, hydm_users, suf_users])
prescription_C = pd.DataFrame(prescription_C)


dex_users = uk_data.loc[(uk_data['DEX_NMU'] == 1)]
diph_users = uk_data.loc[(uk_data['DIPH_NMU'] == 1)]
lop_users = uk_data.loc[(uk_data['LOP_NMU'] == 1)]
prescription_OTC = pd.concat([dex_users, diph_users, lop_users])
prescription_users = pd.concat([prescription_A, prescription_B, prescription_C, prescription_OTC])

coke_users = uk_data.loc[(uk_data['COKE_USE'] >= 1)]
crack_users = uk_data.loc[(uk_data['CRACK_USE'] >= 1)]
mdma_users = uk_data.loc[(uk_data['MDMA_USE'] >= 1)]
fent_users = uk_data.loc[(uk_data['NPFENT_USE'] >= 1)]
heroin_users = uk_data.loc[(uk_data['HEROIN_USE'] >= 1)]
lsd_users = uk_data.loc[(uk_data['LSD_USE'] >= 1)]
mush_users = uk_data.loc[(uk_data['MUSH_USE'] >= 1)]
recreational_A = pd.concat([coke_users, crack_users, mdma_users, fent_users, heroin_users, lsd_users, mush_users])

can_users = uk_data.loc[(uk_data['CAN_USE'] >= 1)]
speed_users = uk_data.loc[(uk_data['SPEED_USE'] >= 1)]
ket_users = uk_data.loc[(uk_data['KET_USE'] >= 1)]
meph_users = uk_data.loc[(uk_data['MEPH_USE'] >= 1)]
spice_users = uk_data.loc[(uk_data['SPICE_USE'] >= 1)]
recreational_B = pd.concat([can_users, speed_users, ket_users, meph_users, spice_users])

ghb_users = uk_data.loc[(uk_data['CAN_USE'] >= 1)]
ster_users = uk_data.loc[(uk_data['SPEED_USE'] >= 1)]
khat_users = uk_data.loc[(uk_data['KET_USE'] >= 1)]
recreational_C = pd.concat([ghb_users, ster_users, khat_users])

pop_users = uk_data.loc[(uk_data['POP_USE'] >= 1)]
sal_users = uk_data.loc[(uk_data['SAL_USE'] >= 1)]
recreational_legal = pd.concat([pop_users, sal_users])
recreational_users = pd.concat([recreational_A, recreational_B, recreational_C, recreational_legal])
    
    