import csv
global entry_number

entry_number = 0
gps_time = 13.2
rpm = 10




programRunning = True ##outside variable!!

latestData = [entry_number, gps_time, rpm,'water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']


fieldnames = ['entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']



def dataLogger(latestData, feildnames, entry_number):
    new_file_name = (str(gps_time) + '.csv')
    with open(new_file_name, 'w', newline='') as new_file: ## experement with this function it maybe it can live in the main loop statement with the
        writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        while programRunning == True: ### adjust!!
            entry_number = entry_number + 1
            latestData[0] = entry_number
            writer.writerow(latestData)

dataLogger(latestData, fieldnames, entry_number)

print(latestData[int(gps_time)])
