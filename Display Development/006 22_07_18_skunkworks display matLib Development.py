#This script builds on v002 and creates text boxes on each of the current rectangles (that will later be bar graphs)

# In this version I begin to experiment with changing the sizes of the graphs over time. This will later lead to
# the bar graphs moving in live time relative to sensor read outs. I am concerned on how it will handle it.

## after testing I have determined that tkinter is not sutible for graphs that change size. It is however useful static items.
## mathLib seems to be much more promising.

import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

rpm = 10
gps_time = 13

latestData = [entry_number, gps_time, rpm,'water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']

plt.style.use("fivethirtyeight") #cosmetic styling

data = pd.read_csv('13.2.csv') # reading data log -- will need to work with file structure in Beta

rpm = latestData[2] #pull individual values from log strings

plt.barh(rpm, 1)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("rpm")

#plt.tight_layout()

plt.show()
