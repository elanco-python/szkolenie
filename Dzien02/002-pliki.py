
# Obsługa plików

s = "c:\\temp\\plik.txt"
s = "c:/temp/plik.txt"
s = r"c:\tmp\plik.txt"

fd = None
try:
    # problematyczny kod
    fd = open("elan_us_d.csv", "rt")
    rows = fd.readlines()[1:]
    for row in rows:
        items = row.split(",")
        if len(items)<5:
            continue

        if float(items[4])>=35:
            print(row.strip())
except Exception as exc:
    print("Wystąpił wyjątek:", exc)
finally:
    if fd: fd.close()

print("="*80)
# context manager
with open("elan_us_d.csv", "rt") as fd:
    for index, row in enumerate(fd):
        if index==0: continue
        items = row.split(",")
        if len(items) < 5:
            continue

        if float(items[4]) >= 35:
            print(row.strip())

