import csv


with open('new_names.csv', 'w') as new_file:
    fieldnames = ['first_name', 'last_name']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

    csv_writer.writeheader()
