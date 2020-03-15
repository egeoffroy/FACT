#!/usr/bin/python3
'''make "VCF" of SNPs for use with the fastenloc prep
script summarize_dap2enloc.pl
make sure ID is the same as SNP IDs used in db file,
column headers needed:
#CHROM POS ID REF ALT'''

import os
import gzip
import argparse
import sys
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Make VCF of SNPs')
    parser.add_argument('-g', '--geno',
                        help='input genotype folder',
                        required='True'
                        )
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
geno_folder = args.geno
pop = args.pop

gtdir = geno_folder
outvcf = gzip.open(pop+"_cposid.vcf.gz", "wb")
outvcf.write("#CHROM\tPOS\tID\tREF\tALT\n".encode('utf-8')) #encode for gzip
for i in range(1,23):
    for line in open(gtdir + pop +"_" + str(i) + "_annot.txt"):
        arr = line.strip().split()
        (chr, pos, id, ref, alt) = arr[0:5]
        if chr == "chr":
            continue
        outstr = chr + "\t" + pos + "\t" + id + "\t" + ref + "\t" + alt + "\n"
        outvcf.write(outstr.encode('utf-8'))
outvcf.close()
