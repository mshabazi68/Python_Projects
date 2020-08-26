from datetime import date
import datetime
from dateutil.relativedelta import relativedelta

f_date = datetime.date(1977, 11, 13)
l_date = datetime.date(1989, 4, 11)

total = (l_date-f_date)

print("The age difference is " , total)
##print(type(total))

##datetime.datetime(year , month , day ,Hours ,min ,sec )
datetime1 = datetime.datetime(1977, 11, 13,15,30,50)
datetime2 = datetime.datetime(1989, 4, 11,23,10,58)
time_difference = relativedelta(datetime2, datetime1)

print ( time_difference.years , "Years" , time_difference.months, "Months", time_difference.days, "Days", time_difference.hours,"Hours", time_difference.minutes,"minutes", time_difference.seconds,"Seconds")

num_months = (datetime2.year - datetime1.year) * 12 + (datetime2.month - datetime1.month)
print(num_months," total months")

num_Days = ((datetime2.year-datetime1.year) * 12 + (datetime2.month-datetime1.month))*30 +(datetime2.day-datetime1.day)

print(num_Days,"total days")



