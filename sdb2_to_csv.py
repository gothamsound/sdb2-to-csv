import xml.etree.ElementTree as ET
import os
import sys

target = sys.argv[1]
print("Converting file " + target + "...\n")

tree = ET.parse(target)
root = tree.getroot()
out = target[:-4] +"csv"

print("Building file " + out + "...\n")

scan_length = len(root[0][0])
f = open(out, "w")
n = 0

print("Parsing sdb2 file...\n\n")

while (n < scan_length):
    freq = float(root[0][0][n].text)
    freq /= 1000

    line = str(freq) +"," +root[0][1][n].text
    f.write(line + "\n")
    print(line)
    n += 1

f.close()

