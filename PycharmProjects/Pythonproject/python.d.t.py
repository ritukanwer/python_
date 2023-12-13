#import datetime
#print(dir(datetime))


#from datetime import datetime
#now = datetime.now()
#print(now)
#day = now.day
#month = now.month
#year = now.year
#hour = now.hour
#minute = now.month
#second = now.second
#timestamp = now.timestamp
#print(day,month,year,hour,minute)
#print('timestamp','timestamp')
#print(f'{day}/{month}/{year}/{hour}:{minute}')

from datetime import datetime
new_year = (2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0


