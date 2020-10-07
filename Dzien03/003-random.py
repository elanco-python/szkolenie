
# Generator pseudolosowy
import random
import time
import uuid

random.seed(time.time())
print("Liczba pseudolosowa:", random.random())
print("Liczba za zakresu:", random.randint(-10, 10))
print("Liczba za zakresu z krokiem:", random.randrange(-10, 10, 2))
print("Liczba losowa na podst. rozkl. Gaussa:",
      random.gauss(10, 2) )

lista = [x for x in range(10, 101, 10)]
print(lista)
print("losowanie z listy=", random.choices(lista, k=4))
print("losowanie z listy=", random.sample(lista, k=4))

# UUID
print("UUID4=", uuid.uuid4())
print("UUID5=", uuid.uuid5(uuid.NAMESPACE_X500, "abcdef" ))

# pseudolosowosc w OS
import os
import binascii
secret = os.urandom(32)
print(binascii.hexlify(secret).decode())

# funkcje skrótu
import hashlib
print(hashlib.algorithms_available)
hash = hashlib.new("sha512")
hash.update("Ala ma kota".encode())
print(hash.hexdigest())

import matplotlib.pyplot as plt

# sprawdzanie czy Gauss
gaus_data = [random.gauss(10,2) for _  in range(50_000)]
plt.hist(gaus_data, bins=50, color="red")
plt.show()