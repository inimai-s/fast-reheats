# FIND_BURN_FRAC.PY
# script to output fraction of time burns are in reheat

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('relight_count_COMPLETE_iramp.csv')

fracs = []
burns = []

successes = 0
total = 0

# find fraction of burn times in reheat and full burn times
for i in range(len(df['burn_time'])):
    reheat_time = 0
    elems = df['time_list'].iloc[i].strip('[]').split(', ')
    int_list = [float(elem) for elem in elems]
    reheat_time += sum(int_list)
    frac = reheat_time/(reheat_time+df['burn_time'].iloc[i])
    if frac <= 0.1:
        successes+=1
    fracs.append(reheat_time/(reheat_time+df['burn_time'].iloc[i]))
    total += 1
    burns.append(reheat_time+df['burn_time'].iloc[i])

    new_fracs = [1-frac for frac in fracs]


# output histogram of fraction of time burns are in reheat
plt.figure(figsize=(10, 4))
plt.hist(new_fracs, bins=20,range = (0,1), edgecolor='black')
plt.xlabel('Fraction of time burns are in reheat')
plt.ylabel('Frequency')
plt.title('Histogram of Fraction of time burns are in reheat')
plt.show()
