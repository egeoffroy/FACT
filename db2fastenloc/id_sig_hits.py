#!/usr/bin/python3

#create files that identify top ten RCP hits
import csv

input_file = '{}_gwasprefix.enloc.sig.out'.format(pop)
with open(input_file, 'r') as results:
    head =[next(results) for x in range(10)]
for line in head:
    data = csv.reader(head, delimiter='\t')
with open('significant_RCP.txt','w') as outfile:
    for i in data:
        outfile.write(i[5] + '\n')
