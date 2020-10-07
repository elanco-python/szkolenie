
# Operacje na plikach i folderach
import os
import sys
import shutil
import platform

print("Current dir:", os.getcwd())
print("Listowanie:", os.listdir("../Dzien02"))
if not os.path.exists("tmp"):
    os.mkdir("tmp")
else:
    os.removedirs("tmp")

curr_dir = os.getcwd()
file_name = curr_dir + "/" + "plik.txt"
file_name = curr_dir + os.sep + "plik.txt"
file_name = os.path.join( curr_dir , "plik.txt" )
print(file_name)

if os.path.exists("greq"):
    shutil.rmtree("greq")

import tempfile
print("Katalog tmp:", tempfile.gettempdir())
with tempfile.NamedTemporaryFile("wt", delete=True) as fd:
    print(fd.name)
    fd.write("Linia 1")
    fd.write("Linia 2")
    fd.flush()
    pass

with tempfile.TemporaryDirectory() as tmp_dir:
    print("katalog:", tmp_dir)
    file_name = os.path.join(tmp_dir, "log.txt")
    with open(file_name, "wt") as fd:
        fd.write("abcdefgh")
        fd.flush()

print("Folder tmp usunięty")

print(platform.system())
print(platform.architecture())
print(platform.processor())
print(platform.machine())

