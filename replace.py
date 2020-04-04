import os
import glob

fin = open("C:/Users/ebn/Desktop/opensupports.csv", "rt")
fout = open("C:/Users/ebn/Desktop/opensupports-new.csv", "wt")

for line in fin:
	fout.write(line.replace(';', ','))
	
fin.close()
fout.close()