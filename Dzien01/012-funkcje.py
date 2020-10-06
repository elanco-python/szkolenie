
# Funkcje
#import math
from math import pi, sin, cosh

def foo():
    pass

zmienna_globalna =10

def oblicz_pole_kola(r : float) -> float:
    global zmienna_globalna
    tmp = 10
    zmienna_globalna = 20
    return r**2 * pi

def oblicz_obwod_kola(r):
    x = 2*pi*r
    return x

def oblicz_kolo(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)

pole, obwod = oblicz_kolo(3)
print(f"pole={pole:.3f}, obwod={obwod:.3f}")

# funkcja z parametrami domyslnymi
def nowy_pracownik(imie, nazwisko, telefon="222345678", email="biuro@firma.pl"):
    osoba = {
        "imie" : imie,
        "nazwisko" : nazwisko,
        "telefon" : telefon,
        "email" : email
    }
    return osoba

print(nowy_pracownik("Jan","Kowalski","60122233", "jk@firma.pl"))
print(nowy_pracownik("Jan","Kowalski"))
print(nowy_pracownik("Agata","Nowak", email="an@firma.pl"))
print(nowy_pracownik("Katarzyna","Nowak", email="an@host.pl", telefon="678111222" ))

def wiele_argumentow(imie, nazwisko, *args):
    print("arg1=",imie)
    print("arg2=",nazwisko)
    for arg in args:
        if type(arg) is int:
            print(arg)

print("="*80)
wiele_argumentow("Jan","Kowalski",1,2,-10,True)

print("="*100)
def funkcja_params(id, fallback="BRAK", **kwargs ):
    print("id=",id)
    print("imie=", kwargs.get("imie", fallback))
    print("nazwisko=", kwargs.get("nazwisko", fallback))
    print("wiek=", kwargs.get("wiek", fallback))

funkcja_params(101, imie="Jan", nazwisko="Kowalski")