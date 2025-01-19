# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

import numpy as np
import pandas as pd

# set figure size
plt.figure(figsize=(8,8))

# plot polar axis
ax = plt.subplot(111, polar=True)

# remove grid
plt.axis('off')

# Set the coordinates limits
upperLimit = 100
lowerLimit = 0

# Compute max and min in the dataset
df = pd.DataFrame({
'Method': ['Absolute Reality', 'Realistic Vision', 'Juggernaul XI', 'Playground', 'SDXL', 'SDXL Lightning', 'Kandinsky 3', 'Flux', 'Realism Riiwa', 'Flux AntiBlur', 'Flux Ghibsky', 'Flux Realism', 'Flux Turbo', 'Open Flux', 'DALLE', 'DDPM', 'Guided Diffusion', 'Imporved Diffusion', 'Midjourney', 'ProGAN', 'BigGAN', 'CycleGAN', 'Real'],
'FID': [68.44, 66.83, 72.23, 80.84, 85.71, 69.11, 64.29, 72.72, 69.01, 69.20, 65.51, 70.27, 69.53, 109.72, 99.76, 94.20, 94.20, 115.13, 106.63, 185.92, 225.67, 225.67, 0]
})
max = df['FID'].max()

# Let's compute heights: they are a conversion of each item value in those new coordinates
# In our example, 0 in the dataset will be converted to the lowerLimit (10)
# The maximum will be converted to the upperLimit (100)
slope = (max - lowerLimit) / max
heights = slope * df.FID + lowerLimit

# Compute the width of each bar. In total we have 2*Pi = 360°
width = 2*np.pi / len(df.index)

# Compute the angle each bar is centered on:
indexes = list(range(1, len(df.index)+1))
angles = [element * width for element in indexes]

colors = ["#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", 
          "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", 
          "steelblue", "steelblue", "steelblue", "steelblue", "steelblue",
          "darkcyan", "darkcyan", "darkcyan", "slategray"]
# Draw bars
bars = ax.bar(
    x=angles, 
    height=heights, 
    width=width, 
    bottom=lowerLimit,
    linewidth=2, 
    edgecolor="white",
    color=colors,
)

# little space between the bar and the label
labelPadding = 4

# Add labels
for bar, angle, height, label in zip(bars,angles, heights, df["Method"]):

    # Labels are rotated. Rotation must be specified in degrees :(
    rotation = np.rad2deg(angle)

    # Flip some labels upside down
    alignment = ""
    if angle >= np.pi/2 and angle < 3*np.pi/2:
        alignment = "right"
        rotation = rotation + 180
    else: 
        alignment = "left"

    # Finally add the labels
    ax.text(
        x=angle, 
        y=lowerLimit + bar.get_height() + labelPadding, 
        s=label, 
        ha=alignment, 
        va='center', 
        rotation=rotation, 
        rotation_mode="anchor") 

from matplotlib.patches import Patch
custom_legend = [
    Patch(facecolor='#61a4b2', edgecolor='white', label='Ours'),
    Patch(facecolor='steelblue', edgecolor='white', label='CNNSpot'),
    Patch(facecolor='darkcyan', edgecolor='white', label='Diffusion'),
    Patch(facecolor='slategray', edgecolor='white', label='Real'),
]

plt.legend(handles=custom_legend, loc='lower left', bbox_to_anchor=(0.12, 0.1))
    
plt.show()