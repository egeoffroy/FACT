#!/usr/bin/python3
'''make file with batch commands to run dap-g scan for 1Mb SNPs within each gene'''
import os
datlist = os.listdir(path='AFA_all1Mb_sbams')

outfile = open("AFA_all1Mb_batch_scan.cmd","w")
for f in datlist:
    ens = f[:-4]
    outfile.write("/usr/local/bin/dap-g -d AFA_all1Mb_sbams/" + f + " --scan > AFA_all1Mb_scan_out/" + ens + ".bf\n")
outfile.close()
