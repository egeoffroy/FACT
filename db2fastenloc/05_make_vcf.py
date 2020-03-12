#!/usr/bin/python3
'''make "VCF" of SNPs for use with the fastenloc prep
script summarize_dap2enloc.pl
make sure ID is the same as SNP IDs used in db file,
column headers needed:
#CHROM POS ID REF ALT'''

import os
import gzip

gtdir = "/home/wheelerlab3/files_for_revisions_plosgen/en_v7/prepare_data/genotypes/"
outvcf = gzip.open("AFA_cposid.vcf.gz", "wb")
outvcf.write("#CHROM\tPOS\tID\tREF\tALT\n".encode('utf-8')) #encode for gzip
for i in range(1,23):
    for line in open(gtdir + "AFA_" + str(i) + "_annot.txt"):
        arr = line.strip().split()
        (chr, pos, id, ref, alt) = arr[0:5]
        if chr == "chr":
            continue
        outstr = chr + "\t" + pos + "\t" + id + "\t" + ref + "\t" + alt + "\n"
        outvcf.write(outstr.encode('utf-8'))
outvcf.close()
