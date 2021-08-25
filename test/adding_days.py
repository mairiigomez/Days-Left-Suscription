"""PART 1 PROJECT,  ACCORDING TO A 'X' AMOUNT OF DAYS LEFT IN A SUSCRIPTION
TELL THE STUDENT WHEN IS THE ACTUAL LAST DAY OF THE SUSCRIPTION IN THE PLATFORM"""

from datetime import datetime

# getting the actual date with the format m/d/y
now = datetime.now()
date_time = now.strftime("%m/%d/%y")

# Splitting the string given by the separator '/' and assigning to 
# each variable, then converting to integers
month, days, year = date_time.split(sep='/')
month = int(month)
days = int(days)
year = int(year)

# Choosing a random number of days left in the suscription 
# ****need to code how to come up with this***
days_left_suscription = 365

# simulating the days in each month starting from 0 - 11
months_list = [31,28,31,30,31,30,31,31,30,31,30,31]

# calculating how many days are left in the actual months to 
# move to the next month 'month-1' -> because  need to access to the
# actual days of the month by index 
days_left_actual_month = months_list[month-1] - days

# day left in total of the suscription after taking away the
# days of the actual month 
days_left = days_left_suscription - days_left_actual_month 

while True:
    # if day left are more than the days in a month discount and 
    # move to the next month when you get to '11' restart 
    # 11==decemeber after that there is no more indexs 
    if days_left > months_list[month]:
        days_left = days_left - months_list[month]
        if month < 11:
            month += 1
        elif month == 11:
            month = 0
            year += 1
    
    else:
        # this move to the next new month with the actual days left 
        month += 1
        break

date_end_suscription = f"{days_left}/{month}/{year}"
print(date_end_suscription)