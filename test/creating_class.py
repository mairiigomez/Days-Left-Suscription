"""Create class for students, attributes are what we read from the csv 
- How do we assing it to an attriute"""

import csv 

class Students: 
    def __init__(self, name, status, days_left, end_date):
        self.name = name
        self.status = status
        self.days_left = days_left
        self.end_date = end_date
    
    def __repr__(self):
        return f"name {self.name}, status {self.status}, days {self.days_left}"
        #print(info)
         

with open('test\student_test.csv') as file:
    reader = csv.DictReader(file, delimiter=';')
    i = 0
    instances = []
    for dict_row in reader:
        i += 1 
        code = dict_row['code']
        student_name = dict_row['name']
        status = dict_row['status']
        day_left = dict_row['days_left']
        end_date = dict_row['end_date']

        # print(code)
        code = Students(student_name, status, day_left, end_date)
        instances.append(code)
        
        
        #print(code)

        # student_info = student_name.student_info
        # print(student_info)

print(instances)

# Cómo puedo trabbajar con el nomre de esa insstancia_??



        

    





    






