import datetime

x = datetime.datetime.now()
print("full date", x)
print(" year",x.year)
print(" hour ", x.hour)
print(" minute", x.minute)
print(" day",x.day)
print(" month", x.month)
print("===================")
y = datetime.datetime.now()
print(y.strftime("%B"))