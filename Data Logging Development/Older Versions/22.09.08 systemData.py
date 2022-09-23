from System_Data_02 import SystemData
# tester
import numpy as np

def main():
    # make fake data to test
    print("sterting feed..")
    entry_number = 1
    #nData = 100000
    header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status"
    Buffer = header
    fn = "C:\\Users\\ejmon\\sysData.csv"
    fo = open(fn, "w+")



    #input newest Data, makes a systemData instance "tmp_SysData",
    #and adds the entry number to the object. The instance
    #is then printed as a new line to the data log
    def newDataEntry(nData): 
        #I want to use this object for all data storage...
        i = entry_number + 1
        tmp_SysData = SystemData(i)
        Buffer += f"{tmp_SysData}\n"
        return(tmp_SysData)
    
    print("writing..")
    fo.write(Buffer)
    
    fo.close()
    print("done ...")
