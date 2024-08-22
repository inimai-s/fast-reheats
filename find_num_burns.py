# FIND_NUM_BURNS.PY
# output information for all types of burns for each satellite

import pandas as pd

begin_df = pd.read_csv('begin_burn_pull.csv')
end_df = pd.read_csv('end_burn_pull.csv')
df = pd.read_csv('relight_count4.csv')

begin_df['timestamp'] = pd.to_datetime(begin_df['timestamp'])
end_df['timestamp'] = pd.to_datetime(end_df['timestamp'])

sat_num_burn_fracs = {}

# output aggregate information for all burns for each satellite 
for i in range(len(begin_df['sat_name'])):
    loc = end_df.loc[end_df['sat_name'] == begin_df['sat_name'].iloc[i]]
    total_burns = loc['satfc1x_gnc_num_burn_attempts_i32'].iloc[0] - begin_df['satfc1x_gnc_num_burn_attempts_i32'].iloc[i]
    
    loc2 = df.loc[df['sat_num'] == begin_df['sat_name'].iloc[i]]
    relighted_burns = len(loc2['sat_num'])

    relight_burn_frac = relighted_burns/total_burns
    total_time = (loc['timestamp'].iloc[0] - begin_df['timestamp'].iloc[i]).total_seconds()

    burn_time = 0
    for lst in loc2['time_list']:
        elems = lst.strip('[]').split(', ')
        int_list = [float(elem) for elem in elems]
        burn_time += sum(int_list)

    relight_time_frac = burn_time/total_time

    row = {
        'total_burns':[total_burns],
        'relighted_burns' : [relighted_burns],
        'relight_burn_frac' : [relight_burn_frac],
        'total_time':[total_time],
        'burn_time':[burn_time],
        'relight_time_frac':[relight_time_frac],
        'sat_name':[begin_df['sat_name'].iloc[i]]
    }

    row_df = pd.DataFrame(row)
    row_df.to_csv('stats2.csv',header=None,mode='a',index=None)
