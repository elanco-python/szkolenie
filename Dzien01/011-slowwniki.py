
# Słowniki

osoba = dict()
osoba = {
    "imie" : "Jan",
    "nazwisko" : "Kowalski",
    "wiek" : 44,
    "dostep" : ["101", "111", "123"]
}

print(osoba["imie"])
print(osoba.get("imie1","---"))

# ustawianie
osoba["wiek"] = 45
osoba.update({ "imie":"Pankracy", "wiek":50})
print(osoba)

#osoba.pop("dostep")
#del(osoba["wiek"])
#print(osoba)

print("klucze:", list(osoba.keys()))
print("wartosc:", osoba.values())
print("k/v:", osoba.items())
for elem in osoba.items():
    print(elem)

if "imie" in osoba:
    print("jest klucz 'imie'")

print(f"{osoba['imie']} ma dostęp: {', '.join(osoba['dostep'])}")