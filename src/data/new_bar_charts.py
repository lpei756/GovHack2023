import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a DataFrame
plot_df = pd.read_csv("C:/Users/adamg/some_Gov_Hack/predicted_sentiments_plot_data - predicted_sentiments.csv.csv")

# Pivot table so that sentiments are in separate columns
pivot_df = plot_df.pivot_table(index='platform', columns='Predicted_Sentiment', aggfunc=len, fill_value=0)
pivot_df.reset_index(inplace=True)

# Ensure all sentiment columns are present
for sentiment in ['positive', 'neutral', 'negative']:
    if sentiment not in pivot_df.columns:
        pivot_df[sentiment] = 0

# Calculate the proportions
pivot_df['total'] = pivot_df['positive'] + pivot_df['neutral'] + pivot_df['negative']
pivot_df['positive'] = pivot_df['positive'] / pivot_df['total']
pivot_df['neutral'] = pivot_df['neutral'] / pivot_df['total']
pivot_df['negative'] = pivot_df['negative'] / pivot_df['total']

# Bar width and locations for bar plot
width = 0.3
locations = np.array(range(len(pivot_df)))

# Define the pastel colors
pastel_green = (0.6, 1, 0.6)    # Pastel green for Positive
pastel_yellow = (1, 1, 0.6)     # Pastel yellow for Neutral
pastel_red = (1, 0.6, 0.6)      # Pastel red for Negative

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(locations - width, pivot_df['positive'], width=width, label='Positive', color=pastel_green)
ax.bar(locations, pivot_df['neutral'], width=width, label='Neutral', color=pastel_yellow)
ax.bar(locations + width, pivot_df['negative'], width=width, label='Negative', color=pastel_red)

ax.set_xticks(locations)
ax.set_xticklabels(pivot_df['platform'])
ax.set_title("Sentiment Distribution by Platform")
ax.set_ylabel("Proportion of Sentiments")
ax.set_xlabel("Platform")
ax.legend()

plt.show()
