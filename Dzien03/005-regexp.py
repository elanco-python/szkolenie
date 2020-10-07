
# Wyrażenia regularne
import re

"""
k...a - zaczyna sie od "k", a konczy na "a" i w srodku są 3 dowolne znaki
Ma.*k 
Ma.+k
Mar?k

^[0-9]{2}-[0-9]{3}$

[^0-9A-Za-z_]{3,}

[0-9] to samo co \d
 [^0-9] to samo co \D 
 \s - znaki biale
 \S
 \w - [0-9A-Za-z_]
 \W - [^0-9A-Za-z_]
"""
txt = "Mały Marek machał makatką trzymając trzy piwa"
result = re.findall("ma", txt.lower())
print(result)

zip_code = "02-111"
result = re.match("^[0-9]{2}-[0-9]{3}$", zip_code)
print(result)

cre = re.compile("\d")
result = cre.findall("Kwota do zaplaty 123,45, termin 7 dni")
print(result)

cre = re.compile("\d+")
result = cre.findall("Kwota do zaplaty 123,45, termin 7 dni")
print(result)

txt = "\n\rMały Marek \t machał makatką trzymając trzy piwa "
txt = re.sub("\s", "*", txt, 3)
print(txt)
