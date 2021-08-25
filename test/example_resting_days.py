import datetime

now = datetime.datetime.now()
suscrption = '1-1-2021'

suscrption_date = datetime.datetime.strptime(suscrption, '%m-%d-%Y')

print(now,suscrption_date)


days_happened = (now - suscrption_date).days

result = now + datetime.timedelta(days=144)
print(days_happened, result)

