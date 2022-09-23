from System_Data_02 import SystemData
# tester
import numpy as np

header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status"
#buffer = header

entry_Number = 0
buffer_Number = 0


class dataInput():
   
    def __init__():

    def __main__():
    
    
    def retriveArduinoData():                   ##this opens a serial port on the pi to recive live data
        if __name__ == '__main__':              ##from on an arduino over the serial comms. The data comes in as
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  #a single string
            ser.reset_input_buffer()

        if ser.in_waiting > 0:
            rawInput = ser.readline().decode('utf-8').rstrip()
            return(rawInput)
#           print(line)

#        self.rawData = rawInput

    
latest_Data_List = retriveArduinoData():



def writeToExcel()




def newDataEntry(buffer_Number,entry_Number):    ###makes new instance of sysData with updated information
    entry = entry_Number + 1        ###I want to reset the buffer number every time the buffer is 
    buffer = buffer_Number + 1

    tmp_SysData = SystemData(entry) ###offloaded????
    return(tmp_SysData)
    Buffer += f"{tmp_SysData}\n"

def write_To_File():
    fo.write(buffer)
    
    newDataEntry
    for i in range(buffer):     ####I want to make a buffer object to hold the values
        tmp_SysData = SystemData(i)   ## in to move around the values
        Buffer += f"{tmp_SysData}\n"
    

def main():
    # make fake data to test
    print("sterting feed..")
    entry_number = 1
    #nData = 100000
    header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status"

    for i in range(nData):
        tmp_SysData = SystemData(i)
        Buffer += f"{tmp_SysData}\n"
    fn = "C:\\Users\\ejmon\\sysData.csv"
    fo = open(fn, "w+")



    #input newest Data, makes a systemData instance "tmp_SysData",
    #and adds the entry number to the object. The instance
    #is then printed as a new line to the data log


    
    print("writing..")
    fo.write(Buffer)
    
    fo.close()
    print("done ...")

newDataEntry()