"""Need to figure out how many days has passed since the day that
was bought the the suscription, then substract that from 365 and that is going
to return the days_left this can be done in a function"""

from datetime import date, datetime

now = datetime.now()
date_time = now.strftime("%m/%d/%y")
date_suscription_starts = '01/10/21'

month, day, year = date_time.split(sep='/')
month, day, year = int(month), int(day), int(year)

month_start, day_start, year_start = date_suscription_starts.split(sep='/')
month_start, day_start, year_start = int(month_start), int(day_start), int(year_start)

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# variable added to dont mess up with the actual month number
month_to_count_from = month_start

# Variable that is going to count how many days happened
days_happened = 0 

while month!=month_start and day!=day_start and year!=year_start:
    # days in the month we are analizing
    days_in_month_ = days_in_month[month_to_count_from-1]
    if day_start != days_in_month_:
        # adding days until it hits the days that has that month
        day_start = day_start + 1
        days_happened += 1
    # when the days are equal to the amount of days that that months has
    # reset days and move to the next month
    else: 
        # day_start == days_in_month
        day_start = 0
        month_to_count_from += 1
        # it goes adding on months  
        month_start += 1

print(days_happened)

     
    



