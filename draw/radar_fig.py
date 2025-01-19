# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
# df = pd.DataFrame({
# 'group': ['A','B','C','D'],
# 'var1': [38, 1.5, 30, 4],
# 'var2': [29, 10, 9, 34],
# 'var3': [8, 39, 23, 24],
# 'var4': [7, 31, 33, 14],
# 'var5': [28, 15, 32, 14]
# })


df = pd.DataFrame({
'group': ['Real','Ours','CNNSpot','NPR'],
'Content': [7.26290321, 6.76949705, 4.91950162, 5.71245728],
'Light': [7.63798602, 7.31858022, 4.96091501, 5.88451209],
'Dof': [7.77732309, 7.26465978, 5.14122923, 5.88314714],
'Emphasis': [10-2.50311161, 10 - 1.83763423, 10 - 6.01438125, 10-5.7684871],
'Color': [7.23446878, 7.02706429, 4.48064248, 5.74921799],
'Composition': [7.73606555, 7.53947343, 5.4694531, 6.24304914],
'Overall': [5.75662327, 5.28111054, 3.95514623, 5.01086736],
'FID': [8.10, 6.1071, 3.3693, 4.6742]
})
 
# ------- PART 1: Create background
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([3,6,9], ["3","6","9"], color="grey", size=7)
plt.ylim(0,8.2)
 

# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Real")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Ours")
ax.fill(angles, values, 'r', alpha=0.1)

# Ind2
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="CNNSpot")
ax.fill(angles, values, 'r', alpha=0.1)

# Ind2
values=df.loc[3].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Diffusion")
ax.fill(angles, values, 'r', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.10, 0.10), fontsize=7)

# Show the graph
plt.show()
