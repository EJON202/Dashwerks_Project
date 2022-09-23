from System_Data_02 import SystemData
# tester
import numpy as np
def main():
    # make fake data to test
    print("sterting feed..")
    entry_number = 1
    nData = 100000
    header = "entry_number,gps_time,rpm,water_temp,oil_pressure,pyrometer_1,pyrometer_2,gps_longitude,system_status"
    Buffer = header
    fn = "C:\\Users\\ejmon\\sysData.csv"

    for i in range(nData):
        tmp_SysData = SystemData(i)
        Buffer += f"{tmp_SysData}\n"
        if i % 1000 == 0:
            print(" running ...")
    print("writing..")
    fo = open(fn, "w+")
    fo.write(Buffer)
    fo.close()
    print("done ...")

main()
