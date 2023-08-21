import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

# Simulated data
np.random.seed(0)
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
platforms = ['Facebook', 'Twitter', 'Reddit']

# Linear trends
negative_trend = np.linspace(0.9, 0.1, len(dates))
positive_trend = np.linspace(0.1, 0.9, len(dates))

df = pd.DataFrame({
    'Date': np.tile(dates, len(platforms)),
    'Platform': np.repeat(platforms, len(dates)),
    'Positive': np.tile(positive_trend, len(platforms)) + np.random.randint(-10, 10, len(dates) * len(platforms))/100,
    'Neutral': np.random.randint(0, 100, len(dates) * len(platforms))/100,
    'Negative': np.tile(negative_trend, len(platforms)) + np.random.randint(-10, 10, len(dates) * len(platforms))/100
})

# Calculate the proportions
df['Total'] = df['Positive'] + df['Neutral'] + df['Negative']
df['Positive'] /= df['Total']
df['Neutral'] /= df['Total']
df['Negative'] /= df['Total']




# Number of frames between original data points for interpolation
interp_steps = 100

# Calculate resampling frequency in hours
resample_freq = int(24 / interp_steps) if 24 % interp_steps == 0 else 24 / interp_steps
resample_str = f'{resample_freq}H' if isinstance(resample_freq, int) else f'{resample_freq:.2f}H'

# Upsample each platform's data separately
dfs = []
for platform in platforms:
    platform_df = df[df['Platform'] == platform].set_index('Date')
    upsampled = platform_df.resample(resample_str).asfreq().interpolate()
    upsampled['Platform'] = platform
    dfs.append(upsampled.reset_index())






df_interp = pd.concat(dfs, axis=0)



# Get the unique dates from the interpolated DataFrame
unique_dates = df_interp['Date'].unique()

# Bar width and locations for bar plot
width = 0.3
locations = np.array(range(len(platforms)))

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))


pastel_green = (0.6, 1, 0.6)    # Pastel green for Positive
pastel_yellow = (1, 1, 0.6)   # Pastel orange for Neutral
pastel_red = (1, 0.6, 0.6)      # Pastel red for Negative



def update(num):
    ax.clear()
    current_date = unique_dates[num]
    data_slice = df_interp[df_interp.Date == current_date]
    
    ax.bar(locations - width, data_slice['Positive'], width=width, label='Positive', color=pastel_green)
    ax.bar(locations, data_slice['Neutral'], width=width, label='Neutral', color=pastel_yellow)
    ax.bar(locations + width, data_slice['Negative'], width=width, label='Negative', color=pastel_red)
    
    ax.set_ylim(0, 1)
    ax.set_xticks(locations)
    ax.set_xticklabels(platforms)
    ax.set_title(f"Sentiment on {current_date.strftime('%Y-%m-%d %H:%M')}")
    ax.set_ylabel("Proportion of Sentiments Over Time")  # Setting the y-axis label
    ax.legend()



# Create the animation with adjusted interval
ani = FuncAnimation(fig, update, frames=len(unique_dates), repeat=False, interval=100)  # 100ms per frame

# plt.show()


# Save the animation as a GIF
writer = PillowWriter(fps=10)  # 10 frames per second
ani.save("sentiment_analysis.gif", writer=writer)

plt.show()