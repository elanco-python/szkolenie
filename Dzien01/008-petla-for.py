
# Pętla for

zakres = list( range(1, 11, 2) )
print(zakres)

for x in range(1,11):
    print(x**2)

print("="*80)
lista = ["A", 1, None, (1,"OK")]
counter = 1
for counter, x in enumerate(lista, 100):
    print(counter, x, sep=":")
