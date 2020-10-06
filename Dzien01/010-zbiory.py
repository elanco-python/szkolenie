
"""
 Zbiory
"""
zbior1 = set()
zbior1 = {}
zbior1 = { 1, 2, True, 2 ,0 , False, None, 2, (1,0) }
print(zbior1)

zbior1.add(1)
#print(zbior1[0])
for x in zbior1:
    print(x)

lista = list( set([2,3,3,4,5,5]) )

zbiorA = set()
for x in range(1,11):
    zbiorA.add(x)

zbiorB = set()
for x in range(8,16):
    zbiorB.add(x)

print("A=",zbiorA)
print("B=",zbiorB)
print("unia:", zbiorA.union(zbiorB) )
print("czesc wsp.:", zbiorA.intersection(zbiorB) )
print("rozn. symetryczna:", zbiorA.symmetric_difference(zbiorB) )
print("roznica:", zbiorA.difference(zbiorB) )
