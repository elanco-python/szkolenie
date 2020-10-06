"""
 BMI
"""
waga = int(input("Podaj wagę w kg: "))
wzrost = int(input("Podaj wzrost w cm: "))

bmi = waga / (wzrost/100)**2
s = "Twoje BMI=" + str( round(bmi,2) )
s = f"Twoje BMI={bmi:.0f}"
print(s)