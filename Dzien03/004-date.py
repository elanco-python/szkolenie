
# Operowanie na dacie / czasie
from datetime import datetime

today = datetime.today()
print(today)

curr_time = datetime.now().time()
print(curr_time)

day_of_week = datetime.today().weekday()
print(day_of_week)

birth_day = datetime(1976, 8, 15, 6, 0 , 0)
print(birth_day.strftime("%m/%d/%Y"))

# formatowanie czasu
print(today.strftime("godz %H, min %M, sek %S"))

diff = today - birth_day
print(diff.days)

import time
print(time.time())
print(time.time_ns())