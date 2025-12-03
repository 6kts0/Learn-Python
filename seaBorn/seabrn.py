"""
Monthly plot of the number of passengers per year
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import default dataset 
flight_data = sns.load_dataset("flights")
flight_data.head()



fs_plot = sns.lineplot(
    data=flight_data,
    x="year",
    y="passengers",
    hue="month",
)

plt.show()




