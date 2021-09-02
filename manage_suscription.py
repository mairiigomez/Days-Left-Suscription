"""Manage Suscription of Student: Things to consider
1. Check if the student is active or not, if it is active descount 1 day everyday of the suscription
2. tell the student when it is the actual day that the suscription ends according to the days left

Next things to do: 
* let the suscription on hold be 00/00/0000/ for students that are active.
* asociate all the information to one student using classes and methods if
  the student wants to pause the suscription/unpaused 
* organize by functions a create modules with my code 
* a diferent module that ask the user for its code and ask if it want to 
  pause the suscription 

*** send an email if the student is active t mairiigomez@gmail.com with the info of the student
*** ask if they want to unactive the suscription 

"""

import csv
import datetime

todays_date = datetime.datetime.now()

# List where is going to be overwritten the csv file
new_file = [
    ['student_code', 'student_name', 'status', 'day_suscription_bought','days_left','suscription_on_hold','day_suscription_ends']
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
        suscription_on_hold = dict_row['suscription_on_hold']
        day_suscription_ends = dict_row['day_suscription_ends']

        # Change the format of variables to datetime to work with them
        day_suscription_bought = datetime.datetime.strptime(day_suscription_bought, '%m/%d/%Y')
        suscription_on_hold = datetime.datetime.strptime(suscription_on_hold, '%m/%d/%Y')

        # If student is active discount 1 day to the days_left
        if status == 'active':
        
            days_have_happened = (todays_date - day_suscription_bought).days
            days_left = 365 - days_have_happened 
            day_suscription_ends = todays_date + datetime.timedelta(days=days_left)

            # Convert the dates into a readable format before sending them to the csv
            day_suscription_ends = datetime.datetime.strftime(day_suscription_ends, '%m/%d/%Y')
            day_suscription_bought = datetime.datetime.strftime(day_suscription_bought, '%m/%d/%Y')
            suscription_on_hold = datetime.datetime.strftime(suscription_on_hold, '%m/%d/%Y')

            days_left -= 1
            # build the structure with same variables and days_left -1
            overwritting_csv = "%s,%s,%s,%s,%s,%s,%s" %(student_code,student_name,status,
            day_suscription_bought, days_left, suscription_on_hold, day_suscription_ends)
            # Convert it to a list separeting values y ','
            overwritting_csv = overwritting_csv.split(sep=',')
            # append to the list that is going to be written to the csv
            new_file.append(overwritting_csv)
        
        # If student is unactive build the list with same values read
        elif status == 'unactive':
            # Day that place the suscription on hold minus the day that bought it
            days_have_happened = (suscription_on_hold - day_suscription_bought).days
            days_left = 365 - days_have_happened
            day_suscription_ends = todays_date + datetime.timedelta(days=days_left)

            # convert dates to a readable format
            day_suscription_ends = datetime.datetime.strftime(day_suscription_ends, '%m/%d/%Y')
            day_suscription_bought = datetime.datetime.strftime(day_suscription_bought, '%m/%d/%Y')
            suscription_on_hold = datetime.datetime.strftime(suscription_on_hold, '%m/%d/%Y')

            overwritting_csv = "%s,%s,%s,%s,%s,%s,%s" %(student_code,student_name,status,
            day_suscription_bought, days_left, suscription_on_hold, day_suscription_ends)
            overwritting_csv = overwritting_csv.split(sep=',')
            new_file.append(overwritting_csv)

# Open the file to write the superlist new_file
with open('students.csv', 'w', newline='') as csv_file:
    # Each value in the list is going to be separate it by ';'
    writer_csv = csv.writer(csv_file, delimiter=';')
    for line in new_file:
        writer_csv.writerow(line)  


