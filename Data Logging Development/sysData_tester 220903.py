from System_Data_02 import SystemData
# tester
import numpy as np


###!!!system needs to save buffer more often to prevent loss during abrupt shut-downs.

def main():
    # make fake data to test
    print("starting feed..")
    entry_number = 1
    nData = 100000                        ## number of cycles in buffer
    header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status" 
    Buffer = header                       ##??
    fn = "C:\\Users\\ejmon\\sysData.csv"  ##Destination and name of new file

    for i in range(nData):                ##Runs as many times as specified
        tmp_SysData = SystemData(i)       ##
        Buffer += f"{tmp_SysData}\n"      ##Add new line 
        if i % 1000 == 0:
            print(" running ...")
    print("writing..")
    fo = open(fn, "w+")                   ## open the file -- how does it 
    fo.write(Buffer)                      ## write just the header??
    fo.close()                            ## close document
    print("done ...")

main()
