# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Make a random dataset:
height = [68.44, 66.83, 72.23, 80.84, 85.71, 69.11, 64.29, 72.72, 69.01, 69.20, 65.51, 70.27, 69.53, 109.72, 99.76, 94.20, 94.20, 115.13, 106.63, 165.92, 160.67, 160.67, 0]
bars = ('Absolute Reality', 'Realistic Vision', 'Juggernaul XI', 'Playground', 'SDXL', 'SDXL Lightning', 'Kandinsky 3', 'Flux', 'Realism Riiwa', 'Flux AntiBlur', 'Flux Ghibsky', 'Flux Realism', 'Flux Turbo', 'Open Flux', 'DALLE', 'DDPM', 'Guided Diffusion', 'Imporved Diffusion', 'Midjourney', 'ProGAN', 'BigGAN', 'CycleGAN', 'Real')
y_pos = np.arange(len(bars))

colors = ["#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", 
          "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", "#61a4b2", 
          "steelblue", "steelblue", "steelblue", "steelblue", "steelblue",
          "darkcyan", "darkcyan", "darkcyan", "slategray"]

# Create bars
plt.bar(y_pos, height, color=colors)
plt.ylim(0, 200)
plt.ylabel('FID Score', fontsize=12)
plt.xlabel('Methods', fontsize=12)
plt.xticks([])
for i, value in enumerate(height):
    plt.text(i, value + 2, f"{bars[i]}", ha='center', va='bottom', fontsize=10, rotation=90)


# Create names on the x-axis
# plt.xticks(y_pos, bars, rotation=90)

from matplotlib.patches import Patch
custom_legend = [
    Patch(facecolor='#61a4b2', edgecolor='white', label='Ours'),
    Patch(facecolor='steelblue', edgecolor='white', label='CNNSpot'),
    Patch(facecolor='darkcyan', edgecolor='white', label='Diffusion'),
    Patch(facecolor='slategray', edgecolor='white', label='Real'),
]

plt.legend(handles=custom_legend, loc='lower left', bbox_to_anchor=(0.04, 0.7))
    

# Show graphic
plt.show()