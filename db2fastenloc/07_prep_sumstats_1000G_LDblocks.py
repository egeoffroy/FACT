#!/usr/bin/python3
'''
Using summary stats from GWAS catalog (must by hg19/b37 for MESA db's)
retrieve Z-scores for intersection SNPs with eQTL annotation file and
generate SNP Locus Z-score file for torus
(use LD locus blocks from an appropriate population)
'''
import sys
import argparse
import os
import gzip

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='GWAS summary stats to dap-g Z-score format')
    parser.add_argument('-l', '--ldblocks',
                        help='ld blocks locus file',
                        required='True'
                        )
    parser.add_argument('-s', '--sumstats',
                        help='input summary stats file',
                        required='True'
                        )
    parser.add_argument('-a', '--annot',
                        help='input fastenloc eQTL annot file',
                        required='True'
                        )
    parser.add_argument('-o', '--outprefix',
                        help='output prefix',
                        required='True'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
ldfile = args.ldblocks
sumstatsfile = args.sumstats
annotfile = args.annot
outprefix = args.outprefix

#get column names for beta and se from R function
column = open("column_numbers.csv").readlines()
beta_column = int(column[1].replace('\n', ''))
se_column = int(column[2].replace('\n', '')) #assign appropriate column numbers
chr_column = int(column[3].replace('\n', ''))
bp_column = int(column[4].replace('\n', ''))
oallele_column = int(column[5].replace('\n', ''))
eallele_column = int(column[6].replace('\n', ''))

#make Z-score (beta/se) dictionary from sumstats
#you may need to choose diff columns depending on sumstat format
zdict = dict()
for line in gzip.open(sumstatsfile):
    arr = line.strip().split()
    #convert bytes to str for each item in list
    arr = [x.decode("utf-8") for x in arr]
    #(chr, bp, oallele, eallele) = arr[0:4]
    beta = arr[beta_column] #pull columns
    oallele = arr[oallele_column]
    eallele = arr[eallele_column]
    chr = arr[chr_column]
    bp = arr[bp_column]
    #print(beta)
    se = arr[se_column]
    if beta == "beta" or beta == "Beta" or beta == 'NA' or se == 'NA' or se == 'standard_error': #skip header and extra rows
        continue
    zscore = float(beta)/float(se)
    snpid = chr + "_" + bp + "_" + str(oallele).capitalize() + "_" + str(eallele).capitalize() + "_b37"
    zdict[snpid] = zscore
print(snpid)
#store each LD block in a tuple list, i.e.
# [(Loc#, chr, start, stop), ...]
counter = 0
locuslist = list()
for line in open(ldfile):
    arr = line.strip().split()
    if arr[0] == "chr":
        continue #skip header
    counter += 1
    chr = arr[0][3:] #rm "chr"
    start = float(arr[1])
    stop = float(arr[2])
    locus = "Loc" + str(counter)
    locuslist.append((locus, chr, start, stop))


#generate Z-score file with LD block locus file for intersection SNPs
zout = open(outprefix + ".torus.zval.txt","w")
for line in gzip.open(annotfile):
    arr = line.strip().split()
    snp = arr[2].decode("utf-8")
    if snp in zdict:
        (chr, pos, ref, alt, build) = snp.split("_")
        pos = float(pos)
        for item in locuslist:
            (loc, c, start, stop) = item
            #start = float(start)
            #stop = float(stop)
            if chr == c and pos >= start and pos < stop:
                zout.write(snp + "\t" + loc + "\t" +  str(zdict[snp]) + "\n")


zout.close()
