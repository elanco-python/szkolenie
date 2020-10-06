
"""
 Instrukcja warunkowa
"""
wiek = 18
kasa = 21

if wiek>=18:
    print("mozna sprzedac alko")
    print("======")
    if kasa>20:
        print("Starczy na lubelską")
else:
    print("za malo lat")

print("="*80)
liczba = 15
if liczba%5==0 and liczba%3==0:
    print("przez 5 i 3 jednoczesnie")
elif liczba%5==0:
    print("tylko przez 5")
elif liczba%3==0:
    print("tylko przez 3")
else:
    print("coś innego")
