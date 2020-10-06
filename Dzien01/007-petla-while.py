import time

# Petla while

i = 10
while i>0:
    print(i, end="."*(i-1))
    time.sleep(1)
    i -= 1 # i = i - 1

print()
while True:
    x =int( input("Podaj liczbe >100 i podzielna przez 2: ") )
    if (x>100 and x%2==0) or x==-1:
        break

print("poza petlą")