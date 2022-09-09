import serial
import csv
global entry_number

entry_number = 0
gps_time = 13.2
rpm = 10



################################Arduino Data Input##################################

#								Retrive retriveArduinoData should be in a constant loop, or just run when called. 
#								Would it work if only when called? 

def retriveArduinoData():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

            return(line)





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

unformattedLatestData = retriveArduinoData()

unformattedLatestData = response.decode('utf-8')

feild0, feild1, feild2, feild3, feild4 = my_str.splitlines()

dataLogger(latestData, fieldnames, entry_number)

print(latestData[int(gps_time)])
