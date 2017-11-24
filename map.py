import re
import csv
import string
import sys

fastq = sys.argv[1]
output = sys.argv[2]
file = open(fastq)
map = open(output,'w')
header = ['#SampleID','BarcodeSequence','LinkerPrimerSequence','Description','Length']
map.write("\t".join(header)+"\n")
line = file.readline()
while line:
	if line.startswith('@'):
		line = line[1:]
		row = re.split(' ',line)
		ex = [row[0],'','',row[1],row[2][7:]]
		map.write("\t".join(ex))
	line = file.readline()
		