
# Łańcuchy
s = " ala ma kota i kot ma pchły  "
print(s.strip())
print(s.upper())
print(s.lower())
print(s.strip().capitalize())
print(s.title())
print(s.center(80))
print(s.replace(" ","*", 3))
print(s.count("ma"))
print(s.lstrip().startswith("ala"))
print(s.rstrip().endswith("ły"))
print(s.index("ma"))
print("ma" in s)

if "ma" in s:
    print("Fraza 'ma' występuje")

lista = [2,-2,10]
if 10 in lista:
    print("jest 10")
