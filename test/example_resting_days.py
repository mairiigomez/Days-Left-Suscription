import datetime

now = datetime.datetime.now()
suscrption = '01/01/2021'

#suscrption_date = datetime.datetime.strptime(suscrption, '%m-%d-%Y')
suscrption_date = datetime.datetime.strptime(suscrption, '%m/%d/%Y')

print(now,'\n')
print(suscrption_date)


days_happened = (now - suscrption_date).days

result = now + datetime.timedelta(days=144)
print(days_happened, result)

