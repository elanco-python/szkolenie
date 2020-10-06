
# Zapis do pliku

with open("plik-zapis.txt", "wt") as fd:
    fd.write("To jest linia 1\n")
    fd.write("To jest linia 2\n")
    fd.writelines([ "Linia3\n", "Linia4\n" ])

bytes = bytearray()
for i in range(48,58):
    bytes.append(i)

with open("plik.bin", "wb") as fd:
    fd.write(bytes)