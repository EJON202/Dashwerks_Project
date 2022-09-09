import pandas as pd
from matplotlib import pyplot as plt
import csv

gps_time = 13.2

global entry_number
entry_number = 0

rpm = 10
water_temp = 190
oil_pressure = 100
fuel_pressure = 18

programRunning = True ##outside variable!!

latestData = [entry_number, gps_time, rpm, water_temp', oil_pressure, fuel_pressure, 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']

#path = r'C:\Users\Ethan\Desktop\sublime experement\1_1.csv'
new_file_name = (str(gps_time) + '.csv')
header = 'entry_number', 'gps_time', 'rpm', 'water temp', 'oil pressure', 'fuel_pressure', 'pyrometer 1', 'pyrometer 2', 'gps longitude', 'gps latitude', 'gps speed', 'gps acceleration', 'system down'
fieldnames = [header]

with open(new_file_name, 'w', newline='') as new_file: ## experement with this function it maybe it can live in the main loop statement with the
    writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writeheader()

    while entry_number <= 10: ### adjust!!

        entry_number = entry_number + 1

        #latestDataProcessing = list(latestData)

        latestData[0] = entry_number

        writer.writerow(latestData)

print(latestData)
print(entry_number)
#########################################


plt.style.use('seaborn')




fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=2, ncols=2)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

#latestData = [entry_number, gps_time, rpm,'water temp','oil pressure', 'fuel_pressure' 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']

ax1.plt.barh(latestData[2], color='#444444', label='rpm')
ax1.legend()
ax1.set_xlabel('RPM')


ax2.plt.barh(latestData[4], color='#444444', label='rpm')
ax2.legend()
ax2.set_xlabel('OIL Pressure')

ax3.plt.barh(latestData[3], color='#444444', label='rpm')
ax3.legend()
ax3.set_xlabel('WATER TEMP')

ax4.plt.barh(latestData[5], color='#444444', label='rpm')
ax4.legend()
ax4.set_xlabel('FUEL PRESSURE')

plt.tight_layout()

plt.show()
