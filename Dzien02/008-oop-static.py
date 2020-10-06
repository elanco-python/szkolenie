
# Klasa statyczna
from math import pi

class Planimetria:

    @staticmethod
    def oblicz_pole_kola(r):
        return pi*r**2

wynik = Planimetria.oblicz_pole_kola(5)
print(wynik)