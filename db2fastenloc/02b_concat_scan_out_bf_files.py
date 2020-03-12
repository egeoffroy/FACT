#!/usr/bin/python3

#generate file needed for torus: SNP gene logBF
# *.bf output from scan_out includes snp, log10BF, beta, se, t-stat
import os
datlist = os.listdir(path='AFA_all1Mb_scan_out')

for f in datlist:
    ens = f[:-3]
    os.system("awk \'{print $1 \"\t" + ens + "\t\" $2}\' AFA_all1Mb_scan_out/" + ens + ".bf > AFA_all1Mb_scan_out/" + ens + ".bf2")
os.system("cat AFA_all1Mb_scan_out/*.bf2 | gzip - > AFA.all1Mb.bf.gz")
