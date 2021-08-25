"""Manage Suscription of Student: Things to consider
1. Check if the student is active or not, if it is active descount 1 day everyday of the suscription
2. tell the student when it is the actual day that the suscription ends according to the days left"""

import csv

# List where is going to be overwritten the csv file
new_file = [
    ['student_code', 'student_name', 'status', 'day_suscription_bought','days_left','day_suscription_ends']
    ]

# Open csv file and assign value to each variable
with open('students.csv') as csv_file:
    # Read the file as a dictionary
    reader = csv.DictReader(csv_file, delimiter=';')
    for dict_row in reader:
        student_code = dict_row['student_code']
        student_name = dict_row['student_name']
        status = dict_row['status']
        day_suscription_bought = dict_row['day_suscription_bought']
        days_left = int(dict_row['days_left'])
        day_suscription_ends = dict_row['day_suscription_ends']

        # If student is active discount 1 day to the days_left
        if status == 'active':
            days_left -= 1
            # build the structure with same variables and days_left -1
            overwritting_csv = "%s,%s,%s,%s,%s,%s" %(student_code,student_name,status,
            day_suscription_bought, days_left, day_suscription_ends)
            # Convert it to a list separeting values y ','
            overwritting_csv = overwritting_csv.split(sep=',')
            # append to the list that is going to be written to the csv
            new_file.append(overwritting_csv)
        
        # If student is unactive build the list with same values read
        else:
            overwritting_csv = "%s,%s,%s,%s,%s,%s" %(student_code,student_name,status,
            day_suscription_bought, days_left, day_suscription_ends)
            overwritting_csv = overwritting_csv.split(sep=',')
            new_file.append(overwritting_csv)

# Open the file to write the superlist new_file
with open('students.csv', 'w', newline='') as csv_file:
    # Each value in the list is going to be separate it by ';'
    writer_csv = csv.writer(csv_file, delimiter=';')
    for line in new_file:
        writer_csv.writerow(line)  
