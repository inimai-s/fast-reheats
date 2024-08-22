# FR_DF_ANALYSIS.PY
# script to find reheat custom timeframes before fine step

import pandas as pd

# Read CSV file into a DataFrame and preprocess it
df = pd.read_pickle('fr_jan_1600_on.pkl')

df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')


# find times where relight occur
def find_relight(df, id):
    relights = df[(df['satfc1x_prop_master1_current_state'] == 27) | (df['satfc1x_prop_master1_current_state'] == 26) | (df['satfc1x_prop_master1_current_state'] == 25)]
    relights.to_csv('fr_jan_1600_on.csv', mode='a', index=False, header=False)


id_list = set(df['sat_name'])
for id in id_list:
    filt_df = df[(df['sat_name'] == id)]
    find_relight(filt_df, id)
