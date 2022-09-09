from System_Data_02 import SystemData
# tester
import numpy as np
def main():
    # make fake data to test
    print("sterting feed..")

    ############ variables

    nData = 100000
    header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status"
    fn = "C:\\Users\\ejmon\\sysData.csv"
    
    Buffer = header #currently using this string to write header. Investigate.
    

####Experement
    entry_number = 1
    buffer_Number = 0

    header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status"
    
    fn = "C:\\Users\\ejmon\\sysData.csv"
    fo = open(fn, "w+")

    fo.write(header)
    
    tmp_SysData = SystemData(entry_number)  ## add line to buffer
    Buffer += f"{tmp_SysData}\n"


    if buffer_Number == 20:
        fo.write(Buffer)
        entry_number += 1
        buffer_Number = 0
        Buffer = ""

####


    for i in range(nData):  #############Run each time new data collected
        tmp_SysData = SystemData(i)
        Buffer += f"{tmp_SysData}\n"
        if i % 1000 == 0:
            print(" running ...")
    print("writing..")
    fo = open(fn, "w+") #########
    fo.write(Buffer)
    fo.close()
    print("done ..."    

main()

