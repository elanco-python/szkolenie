
# Parsowanie linii polecen

import sys
import argparse

#print(sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="show output")
parser.add_argument("-n","--name", required=True, \
                            metavar="FILENAME", help="file name")
parser.add_argument("-d", type=int, default=2, metavar="2", help="digits")
parser.add_argument("-f", "--folder", nargs="+", default=".",
                    metavar="/path/to/folder", type=str)
parser.add_argument("-t","--time", type=float, default=10.0)

arguments = parser.parse_args()
print(arguments)
print("folder:",arguments.folder)