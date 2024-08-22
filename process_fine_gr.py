# PROCESS_FINE_GR.PY
# script to aggregate all statistics for each burn window: number of reheats and burn time

import pandas as pd

df = pd.read_csv('fine_gr_pull_COMPLETE.csv')
df = df.drop(columns=([
        'Unnamed: 0']))


# return information for each burn window and characterize relights in the burn window
def process_burn(df):
    relight_time = 0
    can_accept_relight = True
    time_list = []
    burn_time = 0

    # count the number of relights per burn window
    for i in range(len(df['satfc1x_gnc_num_burn_attempts_i32'])):
        if df['satfc1x_prop_master1_current_state'].iloc[i] == 27 or df['satfc1x_prop_master1_current_state'].iloc[i] == 26 or df['satfc1x_prop_master1_current_state'].iloc[i] == 25:
            if can_accept_relight:
                can_accept_relight = False
            relight_time+=10
        else:
            if can_accept_relight == False:
                time_list.append(relight_time)
                relight_time = 0
                can_accept_relight = True

        # detect when burn is in argon supreme thrust
        if df['satfc1x_prop_master1_current_state'].iloc[i] == 22 or df['satfc1x_prop_master1_current_state'].iloc[i] == 23 or df['satfc1x_prop_master1_current_state'].iloc[i] == 20:
            burn_time+=10

    if df['satfc1x_gnc_burn_duration_f64'].shape[0] < 1:
        return len(time_list),time_list,burn_time,0

    return len(time_list),time_list,burn_time,df['satfc1x_gnc_burn_duration_f64'].iloc[0]

            
# find all information for each burn window for each satellite
def process_sat(df, sat):
    burn_set = set(df['satfc1x_gnc_num_burn_attempts_i32'])
    burn_list = list(burn_set)
    burn_list.sort()

    # add information for each burn
    for burn in burn_list:
        burn_df = df[(df['satfc1x_gnc_num_burn_attempts_i32'] == burn)]
        num_relights,time_list,burn_time,sched_burn_time = process_burn(burn_df)
        if num_relights == 0:
            continue

        row = {
                'burn_num': [burn],
                'num_relights': [num_relights],
                'time_list': [time_list],
                'sat_num': [sat],
                'burn_time':[burn_time],
                'sched_burn_time':[sched_burn_time]
            }
        row_df = pd.DataFrame(row)
        row_df.to_csv('relight_count_COMPLETE_iramp.csv', mode='a', index=False, header=False)



id_list = set(df['sat_name'])

for id in id_list:
    filt_df = df[(df['sat_name'] == id)]
    process_sat(filt_df, id)
