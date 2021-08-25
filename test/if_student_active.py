"""We need to read if the student is active or no in order to discount more days or not 
we need to check that in our csv file meanwhile less simulate that we know that the 
student is active"""
import datetime
import csv

#new_file = []

with open('students.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for dict_row in reader:
        if dict_row['status'] == 'active':
            print(dict_row)
            days_left = dict_row['days_left']
            days_left = int(days_left)
            days_left = days_left - 1
            
            # reader_as_list = csv.reader(csv_file, delimiter=';')
            # for line in reader_as_list:
            #     file = '%s,%s,%s,%s'
    
    with open('students.csv', 'w') as csv_file:
        fieldnames = ['name','status','days_left','end_date']
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
        #writer.writerow({'status':days_left})

        for line in reader: 
            writer.writerow(line)
    
# with open('students.csv') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     for line in reader:
#         if line 
#         new_file.append(line)




# status = True
# day_left = 200
# print(day_left)

# while day_left > 0:
#     if status == True:
#         day_left = day_left -1
#     print(day_left)

# print(day_left)
    

# csv files 
# name;status;days_left;end_date;
# mairi;active;160;10/08/2021
# jose;unactive;200;10/08/2021;