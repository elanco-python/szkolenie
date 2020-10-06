
# komentarz jednolinijkowy

"""
Komentarz linia 1
linia 2
linia 3
"""

x = 12
x = 12.34
x = "Ala ma \" kota"
x = 'Ala ma \' kota'
x = 'Ala ma \t \r\n \f " kota '
x = None

# krotka/tuple
krotka = (200, "OK")
krotka = (200, "OK", None)
krotka_1el = (200,)
_ = 1
kod = krotka[0]
komunikat = krotka[1]
info_extra = krotka[2]

kod, komunikat, info_extra = krotka
a, b = -10, 10
a, b = b, a
a = -10; b = 10;

#krotka[0] = 10
print(a, b, krotka, sep="|")



