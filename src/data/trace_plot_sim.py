import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter





# Simulated data
np.random.seed(0)
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
platforms = ['Facebook', 'Twitter', 'Reddit']

# Linear trends
negative_trend = np.linspace(90, 10, len(dates))
positive_trend = np.linspace(10, 90, len(dates))

df = pd.DataFrame({
    'Date': np.tile(dates, len(platforms)),
    'Platform': np.repeat(platforms, len(dates)),
    'Positive': np.tile(positive_trend, len(platforms)) + np.random.randint(-10, 10, len(dates) * len(platforms)),
    'Neutral': np.random.randint(0, 100, len(dates) * len(platforms)),
    'Negative': np.tile(negative_trend, len(platforms)) + np.random.randint(-10, 10, len(dates) * len(platforms))
})




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


# ... [All the previous code remains the same up to the point of plotting]

# Get the unique dates from the interpolated DataFrame
unique_dates = df_interp['Date'].unique()

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

pastel_green = (0.6, 1, 0.6)    # Pastel green for Positive
pastel_yellow = (1, 1, 0.6)   # Pastel yellow for Neutral
pastel_red = (1, 0.6, 0.6)      # Pastel red for Negative

# Define a dictionary for line styles for each platform
line_styles = {
    'Facebook': '--',  # dashed line
    'Twitter': '-',   # solid line
    'Reddit': ':',    # dotted line
}

# Create "dummy" lines for the legend
dummy_lines = []
for platform in platforms:
    style = line_styles[platform]
    dummy_lines.append(ax.plot([], [], linestyle=style, color=pastel_green, label=f'Positive {platform}')[0])
    dummy_lines.append(ax.plot([], [], linestyle=style, color=pastel_yellow, label=f'Neutral {platform}')[0])
    dummy_lines.append(ax.plot([], [], linestyle=style, color=pastel_red, label=f'Negative {platform}')[0])

ax.legend(handles=dummy_lines, loc='upper left')

def update(num):
    # Remove previous plot lines without clearing other elements like the legend
    for line in ax.lines[:]:
        if line not in dummy_lines:  # Preserve the dummy lines for legend
            line.remove()

    current_date = unique_dates[num]
    data_slice = df_interp[df_interp.Date <= current_date]  # We want to accumulate data up to current_date

    # Loop through each platform to apply different styles
    for platform in platforms:
        platform_slice = data_slice[data_slice['Platform'] == platform]
        style = line_styles[platform]
        
        ax.plot(platform_slice['Date'], platform_slice['Positive'], linestyle=style, color=pastel_green)
        ax.plot(platform_slice['Date'], platform_slice['Neutral'], linestyle=style, color=pastel_yellow)
        ax.plot(platform_slice['Date'], platform_slice['Negative'], linestyle=style, color=pastel_red)
    
    ax.set_ylim(0, 150)
    ax.set_title(f"Sentiment on {current_date.strftime('%Y-%m-%d %H:%M')}")

# Create the animation with adjusted interval
ani = FuncAnimation(fig, update, frames=len(unique_dates), repeat=False, interval=100)  # 100ms per frame

plt.show()

























































































