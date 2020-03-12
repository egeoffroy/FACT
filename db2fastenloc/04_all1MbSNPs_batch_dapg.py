#!/usr/bin/python3
'''run dap-g using db SNPs for each gene'''
import os
datlist = os.listdir(path='AFA_all1Mb_sbams')

outfile = open("AFA_all1Mb_batch_dap.cmd","w")
os.system("mkdir AFA_all1Mb_dap_out")
for f in datlist:
    ens = f[:-4]
    outfile.write("/usr/local/bin/dap-g -d AFA_all1Mb_sbams/" + f + " -t 4 -p AFA_all1Mb_priors/" + ens + ".prior -o AFA_all1Mb_dap_out/" + ens + ".fm.out\n")

#consider adding -ld_control flag, default is -ld_control 0.25
