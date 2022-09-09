import csv



new_file_name = (str(gps_time) + '.csv')


with open(new_file_name, 'w', newline='') as new_file: ## experement with this function it maybe it can live in the main loop statement with the
    writer = csv.writer(new_file, delimiter=",")       ##initalization on top...
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writeheader()

    while entry_number <= 10: ### adjust!!

        entry_number = entry_number + 1

        #latestDataProcessing = list(latestData)

        latestData[0] = entry_number

        writer.writerow(latestData)

print(latestData)
#print(latestData[])
print(entry_number)
