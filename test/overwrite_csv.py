import csv

new_file = []
with open('studenttest.csv') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=';')
    for row in reader_csv:
        print(row)
        if row[1] == 'active':
            print(True)
            days_left = int(row[2])
            days_left -= 1
            print(days_left)
            overwritting_csv = "%s,%s,%s,%s" %(row[0],row[1],days_left,row[3])
            overwritting_csv = overwritting_csv.split(sep=',')
            new_file.append(overwritting_csv)
        else:
            new_file.append(row)

print(new_file)

with open('students.csv', 'w', newline='') as csv_file:
    writer_csv = csv.writer(csv_file, delimiter=';')
    for line in new_file:
        writer_csv.writerow(line)        
        
 