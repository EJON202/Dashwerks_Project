import csv


## Change as Order of Data in Serial Channel changes during development
fieldNames = ['entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']
latestData = ['entry_number', 'gps_time', 'rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']


zipLists(feildNames, latestData):


liveDataDictonary = zipLists(fieldNames, latestData)

gps_time = 2000


new_file = (str(gps_time) + '.csv')



def dataLoggerInitalize(gps_time):

    with open(new_file, 'w') as new_file1:
    #writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
        csv_writer = csv.DictWriter(new_file1, 'w', fieldNames, delimiter='\t')
        csv_writer.writeheader()

        for i in range(10):
            csv_writer.writerow(liveDataDictonary.values())


liveDataDictonary = zipLists(fieldNames, latestData)



dataLoggerInitalize(gps_time)


#dataLogger()
