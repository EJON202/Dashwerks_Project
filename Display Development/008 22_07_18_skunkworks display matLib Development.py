#This script builds on v002 and creates text boxes on each of the current rectangles (that will later be bar graphs)

# In this version I begin to experiment with changing the sizes of the graphs over time. This will later lead to
# the bar graphs moving in live time relative to sensor read outs. I am concerned on how it will handle it.

## after testing I have determined that tkinter is not sutible for graphs that change size. It is however useful static items.
## mathLib seems to be much more promising.

import numpy as np
import matplotlib.pyplot as plt

# Define Data

#team = ['Team 1','Team 2','Team 3','Team 4','Team 5']
#emale = [5, 10, 15, 20, 25]
#ale = [15, 20, 30, 16, 13]

y_axis = 5

# Multi bar Chart

plt.barh(y_axis -0.6 ,female, height=0.2,label = 'Female')
plt.barh(y_axis -0.3 , male, height=.2, label = 'Female')
plt.barh(y_axis +0.0, male, height=.2, label = 'Female')
plt.barh(y_axis +0.3 ,male, height=.2, label = 'Female')
plt.barh(y_axis +0.6 ,male, height=.2, label = 'Female')

# Xticks

#lt.xticks(x_axis, team)

# Add legend

plt.legend()

# Display

plt.show()
