from asyncio.windows_events import NULL
import csv
from msilib.schema import Class
import numbers




class readSerial:
    def __init__ (self):
    
    def retriveArduinoData():                   ##this opens a serial port on the pi to recive live data
        if __name__ == '__main__':              ##from on an arduino over the serial comms. The data comes in as
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  #a single string
            ser.reset_input_buffer()

        if ser.in_waiting > 0:
            rawInput = ser.readline().decode('utf-8').rstrip()
            return(rawInput)

        data_List = rawInput.split(',')

        return(data_List)

    data_List = retriveArduinoData():

    def write_Excel_Line(data_List):
        

class SystemData:

    def __init__(self, entry_number, gps_time="0:0:0", rpm=0, water_temp=-1,                    ####intake new data upon 
                     oil_pressure=-1, pyrometer_1=-1, pyrometer_2=-1, gps_longitude=-1,
                     system_status="Init"):
        self.entry_number = entry_number
        self.gps_time = gps_time
        self.rpm = rpm
        self.water_temp = water_temp
        self.system_status = system_status
        self.oil_pressure = oil_pressure
        self.pyrometer_1 = pyrometer_1
        self.pyrometer_2 = pyrometer_2
        self.gps_longitude = gps_longitude


        # TODO add rest of them..


######################## get and sets ######################
    def get_entry_number(self):
        return self.entry_number
    def set_entry_number(self, entry_number):
        self.entry_number = entry_number 

    # get and set
    def get_gps_time(self):
        return self.gps_time
    def set_gps_time(self, gps_time):
        self.gps_time = gps_time
        
    # get and set
    def get_rpm(self):
        return self.rpm
    def set_rpm(self, rpm):
        self.rpm = rpm 
    
    # get and set
    def get_water_temp(self):
        return self.water_temp
    def set_water_temp(self, water_temp):
        self.water_temp = water_temp

    # get and set
    def get_system_status(self):
        return self.system_status
    def set_system_status(self, system_status):
        self.system_status = system_status

    # get and set
    def get_oil_pressure(self):
        return self.oil_pressure
    def set_oil_pressure(self, oil_pressure):
        self.oil_pressure = oil_pressure

    # get and set
    def get_pyrometer_1(self):
        return self.pyrometer_1
    def set_pyrometer_1(self, pyrometer_1):
        self.pyrometer_1 = pyrometer_1

    # get and set
    def get_pyrometer_2(self):
        return self.pyrometer_2
    def set_pyrometer_2(self, pyrometer_2):
        self.pyrometer_2 = pyrometer_2

    # get and set
    def get_gps_longitude(self):
        return self.gps_longitude
    def set_gps_longitude(self, gps_longitude):
        self.gps_longitude = gps_longitude



    # class to string
    def __str__(self):
        sysString = f"{self.entry_number},{self.gps_time},{self.rpm},{self.water_temp},{self.oil_pressure},{self.pyrometer_1},{self.pyrometer_2},{self.gps_longitude},{self.system_status}"
        return sysString








import numpy as np
def main():
    # make fake data to test
    entry_number = 1
    nData = 100
    arr = np.empty(nData)

    for i in range(nData):
        arr[i] = SystemData(i)


   