# OUTPUT_HISTOS.PY
# script that outputs histograms for each of the relevant metrics of reheats


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
from matplotlib.ticker import PercentFormatter
 
df = pd.read_csv('relight_count4.csv')
 
df['time_list'] = df['time_list'].apply(ast.literal_eval)

# Flatten 'time_list' column to account for multiple values
time_data = [float(item) for sublist in df['time_list'] for item in sublist]
 
df2 = pd.read_csv('stats2.csv')
 

# output histogram for each number of reheats per burn
fig, axs = plt.subplots(figsize = (10,4))
axs.hist(df['num_relights'], bins=range(int(min(df['num_relights'])), int(max(df['num_relights'])) + 2), edgecolor='black')
axs.set_xlabel('Number of Relights')
axs.set_ylabel('Frequency')
axs.set_title('Histogram of Number of Relights During a Single Burn')
ax2 = axs.twinx()
counts,bins = np.histogram(df['num_relights'],bins=30,range=(int(min(df['num_relights'])), int(max(df['num_relights'])) + 2))
percentages = counts / np.sum(counts) * 100
ax2.hist(df['num_relights'], bins=range(int(min(df['num_relights'])), int(max(df['num_relights'])) + 2), density=True, edgecolor='black')
ax2.yaxis.set_major_formatter(PercentFormatter(xmax=1))
print(counts)
print(percentages)
axs.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
axs.yaxis.tick_left()
axs.tick_params(labelright=False)
ax2.yaxis.tick_right()
ax2.set_ylabel('Percentage (%) of reheats')
plt.show()
 

# output histogram for each reheat duration
fig, axs = plt.subplots(figsize = (10,4))
axs.hist(time_data, bins=20, range = (int(min(time_data)), 330), edgecolor='black')
axs.set_xlabel('Time (sec)')
axs.set_ylabel('Frequency')
axs.set_title('Histogram of Length of each Relight')
ax2 = axs.twinx()
counts,bins = np.histogram(time_data,bins=20,range=(int(min(time_data)), 330))
percentages = counts / np.sum(counts) * 100
print(counts)
print(percentages)
ax2.set_yticks(np.linspace(0, 52, 6))
axs.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
axs.yaxis.tick_left()
axs.tick_params(labelright=False)
ax2.yaxis.tick_right()
ax2.set_ylabel('Percentage (%) of burns exhibiting reheats')
plt.show()
 

# output histogram for percentage of time per burn window spent in reheat
fig, axs = plt.subplots(figsize = (10,4))
axs.hist(df2['relight_time_frac'], bins=20, range=(0,0.02), edgecolor='black')
axs.set_xlabel('Fraction of Burn Time Spent in Relight')
axs.set_ylabel('Frequency')
axs.set_title('Histogram of Fraction of Burn Time Spent in Relight')
ax2 = axs.twinx()
counts,bins = np.histogram(df2['relight_time_frac'],bins=20,range=(0,0.02))
percentages = counts / np.sum(counts) * 100
ax2.hist(df2['relight_time_frac'], bins=20, range=(0,0.02), density=True, edgecolor='black')
ax2.yaxis.set_major_formatter(PercentFormatter(xmax=1000))
for bar, x in zip(axs.patches,np.linspace(0,0.2,20)):
    if abs(x-300) <= 20:
        bar.set_facecolor('green')
    else:
        bar.set_facecolor('red')

axs.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
axs.yaxis.tick_left()
axs.tick_params(labelright=False)
ax2.yaxis.tick_right()
ax2.set_ylabel('Percentage (%) of satellites')
plt.show()
 

# output histogram of fraction of burn windows using relight
fig, axs = plt.subplots(figsize = (10,4))
axs.hist(df2['relight_burn_frac'], bins=20, range=(0,1), edgecolor='black')
axs.set_xlabel('Fraction of Burns using Relight')
axs.set_ylabel('Frequency')
axs.set_title('Histogram of Fraction of Burns using Relight')
ax2 = axs.twinx()
counts,bins = np.histogram(df2['relight_burn_frac'],bins=20,range=(0,1))
percentages = counts / np.sum(counts) * 100
ax2.set_yticks(np.linspace(0, 60, 6))
print(counts)
print(percentages)
axs.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
axs.yaxis.tick_left()
axs.tick_params(labelright=False)
ax2.yaxis.tick_right()
ax2.set_ylabel('Percentage (%) of satellites')
plt.show()


# print statistics for each burn
print(f'Mean of relight time: {np.mean(time_data)}')
print(f'Average number of relights: {df['num_relights'].mean()}')
print(f'Fraction of sats using relights: {len(set(df['sat_num']))/1727}')
print(f'Average fraction of burn time spent in relight: {df2['relight_time_frac'].mean()}')
print(f'Average fraction of burns using relight: {df2['relight_burn_frac'].mean()}')


# output fraction of reheats that are unsuccessful due to timeout
num_anomaly = 0
good_anomaly = 0
for lst in df['time_list']:
    for elem in lst:
        if elem > 320 or elem < 280:
            num_anomaly+=1
        else:
            good_anomaly+=1
 
print(f'Number of burns that are not optimal time: {num_anomaly}')
print(f'Number of burns that are good time: {good_anomaly}')
print(f'Frac of bad anomaly time: {num_anomaly/(num_anomaly+good_anomaly)}')
