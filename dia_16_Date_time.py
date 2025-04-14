from datetime import datetime, timedelta

# # # # # # # # #           DATE TIME          # # # # # # # # # #  

print()
print('Exercises')
print()

now = datetime.now()
print('now: ', now)
timestamp = now.timestamp()
print('timestamp: ', timestamp)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

print('anio', year)
print('mes', month)
print('dia', day)
print('hora', hour)
print('minutos: ', minute)
print('segundos: ', second)

new_year = datetime(2025, 1, 1)
print('nuevo anio' , new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second

print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

print()
t = now.strftime("%H:%M:%S")
print("time con strftime:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%B/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

from datetime import date

d = date(2020, 1, 1)
print()
print('Current date con uso de date:', d.today())
# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

today = date(year=2024, month=6, day=17)
new_year = date(
    year=2025, month=1, day=1
)  # no llama al new_year de arriba por q es de datetime, no se mezclan
time_left_for_newyear = new_year - today
print('time_left_for_newyear ', time_left_for_newyear)

# dias vividos
print()
t1 = datetime(year=1984, month=2, day=2, hour=3, minute=50, second=0)
#t2 = datetime(year = 2024, month = 6, day = 17, hour = 11, minute = 14, second = 0)
t2 = datetime.now()
diff = t2 - t1
print('dias vividos: ', diff)

future_10_days = t2 + timedelta(days=10)
past_40_days = t2 - timedelta(days=40)
print('future_10_days ', future_10_days)
print('past_40_days' , past_40_days)

print()
print('1-')
# 1    Get the current day, month, year, hour, minute and timestamp from datetime module

ahora = datetime.now()
print(ahora)
print('timestamp', now.timestamp())

# 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print('2-')
time_ahora = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_ahora)

# 3 Today is 5 December, 2020. Change this time string to time
print('3-')
date_string = "5 December, 2022"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 4 Calculate the time difference between now and new year.
print('4-')
tiempo_futuro = datetime(2025, 1, 1)
diferencia = tiempo_futuro - t2
print(diferencia)

# con date

today = date(year=2024, month=6, day=17)
new_year = date(year=2025, month=1, day=1)

print("diferencia al anio siguiente con date: ",new_year-today)

# 5 Calculate the time difference between 1 January 1970 and now.

print('5-')
seventys = date(1970, 1, 1)
print('valor timestamp', today - seventys)
seventys_date_time = datetime(1970, 1, 1)
print('con datetime', t2 - seventys_date_time)

# otros

print()
print('   ***  otros ejemplos con total_seconds:')
A = timedelta(days=2, hours=3, minutes=43, seconds=35)
print('total seconds: ', A.total_seconds())

a = datetime(2024, 5, 14, 5, 40, 20)
b = datetime(2024, 6, 25, 8, 48, 23)
c = b - a

print(c)
minutes = c.total_seconds() / 60
print('total minutos con total_seconds:', minutes)

print('diferencia de minutos del dia: ', c.seconds / 60)

fracc = divmod(c.total_seconds(), 60)
print('mas apropiado con divmod para acomodar la fraccion de tiempo: ',
      fracc[0], 'minutos', fracc[1], 'segundos')
