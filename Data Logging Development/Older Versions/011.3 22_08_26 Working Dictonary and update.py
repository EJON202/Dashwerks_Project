import csv


serial_Input = [1, 0.1, 0, 0, 0, 0, 0, 0.0, 0.0, 'WATING']

system_Data = dict(
    entry_number = 0,
    gps_time = 0.0,
    rpm = 0,
    water_temp = 0,
    oil_pressure = 0,
    pyrometer_1 = 0,
    pyrometer_2 = 0,
    gps_longitude = 0.0,
    gps_latitude = 0.0,
    system_status= 'INITALIZING'   
)

excel_file_name = str(system_Data[gps_time] + ' Skunkworks Data Log')

with open(excel_file_name, 'w') as new_file:
    fieldnames = system_Data.keys

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

    csv_writer.writeheader()

csv.writer

system_Data.update(
    entry_number = serial_Input[0], 
    gps_time = serial_Input[1],
    rpm = serial_Input[2],
    water_temp = serial_Input[3],
    oil_pressure = serial_Input[4],
    pyrometer_1 = serial_Input[5],
    pyrometer_2 = serial_Input[6],
    gps_longitude = serial_Input[7],
    gps_latitude = serial_Input[8],
    system_status = serial_Input[9]'
)

print(system_Data)