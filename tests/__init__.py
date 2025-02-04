import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sys import path
path.append("./")
from lionplot.plot import lionplot

# Define the categories and the number of samples
categories = ['blue', 'green', 'orange']
num_samples = 6

# Generate the categorical variable x
x = np.asarray([category for i in range(num_samples//len(categories)) for category in categories])

# Generate the y variable from a Gaussian distribution with mean 10
y = np.random.normal(loc=10, scale=1, size=num_samples//2)
y = np.append(y, np.random.normal(loc=15, scale=1, size=num_samples//2))

# Generate the yerr variable from a Gaussian distribution with mean 1
yerr = np.random.normal(loc=1, scale=0.001, size=num_samples)

# Create a group value
group = ["A" for i in range(num_samples//2)]
group = group + ["B" for i in range(num_samples//2)]
group = np.asarray(group)

golden_ratio = (5**0.5 - 1) / 2
figsize = 5
    
fig, ax = plt.subplots(1, 1, figsize=(figsize / golden_ratio, figsize))
lionplot(
    x=x,
    y=y,
    ax=ax,
    yerr=yerr,
    hue_values=group,
)
ax.legend()
plt.savefig("./imgs/example.pdf")
plt.close()