# create a dictionary of list
import csv

fieldNames = ['entry_number', 'gps_time','rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']
latestData = ['entry_number', 'gps_time', 'rpm','water temp','oil pressure', 'pyrometer 1','pyrometer 2','gps longitude','gps latitude','gps speed','gps acceleration', 'system down']

latestDataDictonary = {feildNames[i]: latestData[i] for i in range(len(feildNames))}
 