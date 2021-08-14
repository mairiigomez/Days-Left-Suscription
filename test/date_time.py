from datetime import datetime

now = datetime.now()
date_time = now.strftime("%m/%d/%y")
#aplicar la funcion map por aqui y convertirlos todos a enteros
month, days, year = date_time.split(sep='/')
month = int(month)
days = int(days)
year = int(year)
days_left_suscription = 855 

months_dict = [
    {'jan':31}, {'feb':28}, {'mar':31}, {'apr':30}, {'may':31}, {'jun':30}, 
    {'jul':31}, {'ago':31}, {'sep':30}, {'oct':31}, {'nov':30}, {'dic':31}
    ]

months_list = [31,28,31,30,31,30,31,31,30,31,30,31]

days_left_actual_month = months_list[month-1] - days

days_left = days_left_suscription - days_left_actual_month 

months_suscription_ends = month + 1 
while True:
    if days_left > months_list[month]:
        days_left = days_left - months_list[month]
        months_suscription_ends += 1 
        if month < 11:
            month += 1
        elif month == 11:
            month = 0
            year += 1
    
    else:
        month += 1
        break

date_end_suscription = f"{days_left}/{month}/{year}"
print(date_end_suscription)