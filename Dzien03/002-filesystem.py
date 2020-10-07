
# Operacje na plikach i folderach
import os
import sys
import shutil

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

shutil.rmtree()

