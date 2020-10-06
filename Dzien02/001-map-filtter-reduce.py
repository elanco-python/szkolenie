from functools import reduce

lista = [5, -2, 8, 10, 8, 9]

def kwadrat(x):
    return x**2

print(list( map( kwadrat , lista ) ))
print(list( map( lambda x:x**2, lista ) ))

print(list(filter( lambda x:x>0, lista)))

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8, 10]
print( list(  map( lambda a,b:a+b, lista2, lista1)  ) )

# reduce
print(sum(lista))
lista = [1,2,3,4,5]
print(reduce( lambda x,y: x*y, lista))