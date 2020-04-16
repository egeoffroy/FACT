#!/usr/bin/python3
import os
import sys
import shlex
import argparse
#create files that identify top ten RCP hits
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Matrix EQTL to .dat format from .db SNP list')
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    parser.add_argument('-prefix', '--prefix',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    
    return(parser.parse_args(args))
args = check_arg(sys.argv[1:])
pop = args.pop

import csv

input_file = '{}_all1Mb_{}.enloc.sig.out'.format(pop, args.prefix)
with open(input_file, 'r') as results:
    data2 =csv.reader(results, delimiter='\t')
    data = []
    for i in data2:
        for j in i:
            j = j.split()
        data.append(j)
    sortData = sorted(data, key=lambda x: float(x[5]), reverse=True)
with open('significant_RCP.txt','w') as outfile:
    for i in range(10):
        outfile.write(str('\t'.join([str(x) for x in sortData[i]]))+'\n')
outfile.close() 
