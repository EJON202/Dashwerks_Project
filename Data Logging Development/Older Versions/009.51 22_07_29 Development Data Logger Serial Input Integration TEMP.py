import csv


serialInputList = [0] ##testing

dataDictonary = {'entry_number' : serialInputList[0], 'gps_time' : 0,'rpm' : 0,'water temp' : 0,'oil pressure' : 0, 'pyrometer 1' : 0,'pyrometer 2' : 0,'gps longitude' : 0,'gps latitude' : 0,'gps speed' : 0,'gps acceleration' : 0, 'system down' : 'OK'}

####Loop Dictonary Update from ArduinoSerial
#serialInputList = [4,2]
#dataDictonary.update({'entry_number' : serialInputList[1], 'gps_time' : 0,'rpm' : 0,'water temp' : 0,'oil pressure' : 0, 'pyrometer 1' : 0,'pyrometer 2' : 0,'gps longitude' : 0,'gps latitude' : 0,'gps speed' : 0,'gps acceleration' : 0, 'system down' : 'OK'})

print(dataDictonary)

#dataDictonary["entry_number"] = dataDictonary["entry_number"] + 1


with open('new_names1.csv', 'w') as new_file:

	CSV_writer = csv.writer(new_file)

	keys = dataDictonary.keys()

	CSV_writer.writerow(keys)

	#w.writeheader()

	#print(feildnames)
