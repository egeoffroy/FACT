#!/usr/bin/python3
'''convert Matrix EQTL format to .dat
one .dat file for each phenotype,
include SNPs w/in 1Mb of each gene'''
import sys
import argparse
import os
from os import path

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Matrix EQTL to .dat format from .db SNP list')
    parser.add_argument('-g', '--geno',
                        help='input genotype file',
                        required='True'
                        )
    parser.add_argument('-p', '--pheno',
			help='input phenotype file',
			required='True'
			)
    parser.add_argument('-m', '--genemap',
                        help='gene position map',
                        required='True'
                        )
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    parser.add_argument('-o', '--outdir',
                        help='output .dat file directory',
                        required='True'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
genofile = args.geno
phenofile = args.pheno
genemapfile = args.genemap
outdir = args.outdir
pop = args.pop

#check if dir for output exists, if not make it
if path.isdir(outdir) == False:
    os.system('mkdir ' + outdir)

#make tuple list of (gene_id, start, end)
geneposlist = list()
for line in open(genemapfile):
    arr = line.strip().split()
    (chr, geneid, genename, start, end, type) = arr
    if type == "protein_coding": #mesa models only have protein_coding genes
        geneposlist.append((geneid, chr, start, end))

#make snplist for each gene
snplists = dict()
#keys (genes) : values (snp list) 1_1509034_T_C_b37 format (matches meqtl file)
#also make geno dict
genodict = dict()
for line in open(genofile):
    arr = line.strip().split()
    snp = arr[0]
    if snp == "id" or snp == "rsid":
        continue #skip header
    chr = snp.split("_")[0] #retrieve chromosome
    gts = arr[1:]
    genodict[snp] = gts
    pos = float(snp.split("_")[1]) #retrieve position
    for (gene, c, start, end) in geneposlist:
        left = float(start) - 1e6
        right = float(end) + 1e6
        if chr == c and pos > left and pos < right:
            if gene not in snplists:
                snplists[gene]=list()
            snplists[gene].append(snp)

#make pheno dict
phenodict = dict()
for line in open(phenofile):
    arr = line.strip().split()
    id = arr[0]
    pts = arr[1:]
    if id == "PROBE_ID":
        continue
    else:
        phenodict[id] = pts

#make list of genes on same chr as genotypes
phenos = list()
for (gene, c, start, end) in geneposlist:
    if c == chr:
        phenos.append(gene)

for p in phenos:
    if p in phenodict:
        with open(outdir + "/" + p + ".dat", 'w') as current_file:
            phenostr = "pheno " + p + " " + pop + " " +  " ".join(phenodict[p]) + "\n"
            current_file.write(phenostr)
            if p in snplists:
                snps = snplists[p] # get list of snps to retrieve gts
                for s in snps:
                    gts = genodict[s]
                    outstr = "geno " + s + " " + pop + " " + " ".join(gts) + "\n"
                    current_file.write(outstr)
                current_file.close()


