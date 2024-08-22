# Fast Reheats
Script that determines the prevalence of fast reheats in thruster burns and determines the new correct reheat time to allow for 90% burning in all windows

# Script: fr_df_analysis.py
Run to find reheat custom timeframes before fine step

# Script: process_fine_gr.py
Run to aggregate all statistics for each burn window: number of reheats and burn time

# Script: find_burn_frac.py
Run to output fraction of time burns in reheat

# Script: find_num_burns.py
Run to output information for all types of burns for each satellite

# Script: output_histos.py
Run to output histograms for each of the relevant metrics of reheats

# Script: line_plot.py
Run to show recommendation for shortening fast reheat time from 300 sec to 28 sec to provide 90% burning

# Installation python packages:
- pandas
- numpy
- matplotlib
- plotly.express
- ast
