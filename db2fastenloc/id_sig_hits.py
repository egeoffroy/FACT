#!/usr/bin/python3

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
args = check_arg(sys.argv[1:])
pop = args.pop
import csv

input_file = '{}_{}.enloc.sig.out'.format(pop, args.prefix)
with open(input_file, 'r') as results:
    head =[next(results) for x in range(10)]
for line in head:
    data = csv.reader(head, delimiter='\t')
with open('significant_RCP.txt','w') as outfile:
    for i in data:
        outfile.write(i[5] + '\n')
