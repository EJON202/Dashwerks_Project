


import serial
import csv

global entry_number
entry_number = 0

#programRunning = True

#latestData = [entry_number, gps_time, rpm,'water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']

fieldNames = ['entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']


def retriveArduinoData():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
        while True:
            if ser.in_waiting > 0:
                serialRawInput = ser.readline().decode('utf-8').rstrip()
                serialInputList = list(serialRawInput.split(" "))
                #print(line)
                return(serialInputList)


def zipLists(feildNames, serialInputList):
    processingLiveDataDictonary = zip(feildNames, serialInputList)
    liveDataDictonary = dict(processingLiveDataDictonary)
    return processingLiveDataDictonary


def dataLogger(serialInputList, feildNames, entry_number):
    new_file_name = (str(gps_time) + '.csv')
    with open(new_file_name, 'w', newline='') as new_file: ## experement with this function it maybe it can live in the main loop statement with the
        writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        while programRunning == True: ### adjust!!
            entry_number = entry_number + 1
            latestData[0] = entry_number
            writer.writerow(latestData)
