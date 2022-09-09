import csv


global entry_number
entry_number = 0

gps_time = 14.2
rpm = 10
programRunning = True ##outside variable!!


latestData = [entry_number, gps_time, rpm,'water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']


new_file_name = (str(gps_time) + '.csv')
header = 'entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down'
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
#print(latestData[])
print(entry_number)
