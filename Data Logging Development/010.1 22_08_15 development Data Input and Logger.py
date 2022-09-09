
## Here I am attempting to get the basic variables together to make the dictonary of live values. This dictonary will be updated live and act as the way of referencing the data. 
## Booleans can run to help alert processes and catch errors. The goal is to improve reliablity with these.



import serial

#Initalizing Variables

systemStarting = False
systemRunning = False
systemRecording = False
systemOK= False

newSerialData = False

fieldNames = ['entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']
latestData = ['NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY','NOT READY']

liveData = dict(zip(fieldNames, latestData))



def openArduinoSerial
def retriveArduinoData():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()