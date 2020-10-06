
# działania na listach

lista = list() # lista pusta
lista = [] # lista pusta
lista = [1, 2, "Ala ma kota", -123.45, None, (1,-1), ['A','B'], True, False  ]
print(len(lista))
lista[2] = -2
print(lista)

lista.append(None)
lista.extend([-10,-20,-30])
print(lista)
lista.insert(0, "START")
print(lista)

lista.remove(None)
print(lista)

print(lista.index("START"))
print(lista.pop(5))
print(lista)

lista2 = [1,6,-10,10]
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)

print("="*60)
lista_kopia = lista.copy()
lista_kopia[0] = "ALA MA KOTA"
print(lista_kopia)
print(lista)

s = "Ala ma kota i kot ma pchły".replace(" ","_")
print(s)
print(s[:4]) # 4 pierwsze znaki
print(s[-4:]) # ostatnie 4 znaki
print(s[4:6]) # ma
print(s[::-1]) # reverse