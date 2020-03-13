#!/usr/bin/python3

#generate file needed for torus: SNP gene logBF
# *.bf output from scan_out includes snp, log10BF, beta, se, t-stat
import os
import argparse
import sys
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Make SNP gene logBF file for TORUS')
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    return parser.parse_args(args)
args = check_arg(sys.argv[1:])
pop = args.pop
datlist = os.listdir(path=pop+'_all1Mb_scan_out')

for f in datlist:
    ens = f[:-3]
    os.system("awk \'{print $1 \"\t" + ens + "\t\" $2}\' " + pop + "_all1Mb_scan_out/" + ens + ".bf > " + pop + "_all1Mb_scan_out/" + ens + ".bf2")
os.system("cat " + pop+ "_all1Mb_scan_out/*.bf2 | gzip - > " + pop + ".all1Mb.bf.gz")
