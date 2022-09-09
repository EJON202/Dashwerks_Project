import csv
  
employee_info = ['emp_id', 'emp_name', 'skills']
  
new_dict = {
'emp_id' : 456, 'emp_name' : 'George', 
}
  


with open('test4.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = employee_info)
    writer.writeheader()

    writer.writerows(new_dict)