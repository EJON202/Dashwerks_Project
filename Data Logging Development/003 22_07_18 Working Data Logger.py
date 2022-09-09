import csv

gps_time = 13.2

global entry_number
entry_number = 0

rpm = 10
programRunning = True ##outside variable!!

latestData = entry_number, gps_time, rpm,'water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down'

#path = r'C:\Users\Ethan\Desktop\sublime experement\1_1.csv'
new_file_name = (str(gps_time) + '.csv')
header = 'entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down'
fieldnames = [str(header)]

with open(new_file_name, 'w', newline='') as new_file: ## experement with this function it maybe it can live in the main loop statement with the 
    writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')  
    csv_writer.writeheader()

    while entry_number <= 10: ### adjust!!

        entry_number = entry_number + 1

        latestDataProcessing = list(latestData)

        latestDataProcessing[0] = entry_number

        writer.writerow(latestDataProcessing)

        



print(latestData)
print(latestData[2])
print(entry_number)