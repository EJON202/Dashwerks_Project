import csv
import pandas as pd

gps_time = 13.2

global entry_number
entry_number = 0

programRunning = True ##outside variable!!


#path = r'C:\Users\Ethan\Desktop\sublime experement\1_1.csv'
new_file_name = (str(gps_time) + '.csv')
header = 'entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down'
fieldnames = [str(header)]

with open(new_file_name, 'w', newline='') as new_file: ## experement with this function it maybe it can live in the main loop statement with the 
    writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')  
    csv_writer.writeheader()

    while entry_number <= 10: ### adjust!!
    
        loopData = entry_number, gps_time, 'rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down'

        writer.writerow(loopData)

        entry_number = entry_number + 1

data = pd.read_csv('13.2.csv')
print(loopData)
print(data['rpm'])


        