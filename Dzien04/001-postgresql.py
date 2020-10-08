
# Komunikacja z bazą danych

import datetime
#from dbutils import *
import dbutils

connection, cursor = dbutils.connect_db()

# SELECT
sql = " SELECT * FROM public.city WHERE city_id=92"
cursor.execute(sql)
row = cursor.fetchone()
print(row)

print("="*70)
sql = " SELECT * FROM public.city WHERE city_id<=10"
cursor.execute(sql)
rows = cursor.fetchall()
#rows = cursor.fetchone()
print(rows)

# INSERT
sql = "INSERT INTO public.city (city, last_update, country_id) VALUES ( %s, %s, 15 ) "
data = ( 'Nibylandia-MW', datetime.datetime.today() )
cursor.execute(sql, data)
connection.commit()

# UPDATE
sql = " UPDATE public.city SET city=%s WHERE city=%s "
data = ( 'Nibylandia2-MW', 'Nibylandia-MW'  )
cursor.execute(sql, data)
connection.commit()

# DELETER
sql = " DELETE FROM public.city WHERE city= %s"
data = ( 'Nibylandia2-MW',)
cursor.execute(sql, data)
connection.commit()

cursor.close()
connection.close()
